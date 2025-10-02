from types import MappingProxyType
from typing import Callable, Optional, Tuple, Type

from aiohttp import ClientError, ClientResponse, ClientSession
from pydantic import BaseModel, ValidationError

from .ipachca import IPachca
from .models.api_models import (
    APIMessage,
    APIMessageInfo,
    APIQueryMessageURIParams,
    APIReact,
    APISignFile,
    APISignFileInfo,
    ListAPIMessageInfo,
    ListAPIReactInfo,
)
from .models.base_models import QueryParams


class PachcaImpl(IPachca):
    def __init__(self, session: ClientSession):
        self._session = session

    async def _get(
        self, url: str, query_params: dict = MappingProxyType({})
    ) -> dict | ClientError:
        async with self._session.get(url, params=query_params) as resp:
            err = await self._wrap_http_errors(resp)

            if err is not None:
                return err

            return await resp.json()

    async def _post(
        self, url: str, json_payload: dict = MappingProxyType({})
    ) -> dict | ClientError:
        async with self._session.post(url, json=json_payload) as resp:
            err = await self._wrap_http_errors(resp)

            if err is not None:
                return err

            return await resp.json()

    async def _post_resp(self, url: str, json_payload: dict):
        async with self._session.post(url, json=json_payload) as resp:
            return resp

    async def _delete_resp(self, url: str, query_params: dict = MappingProxyType({})):
        async with self._session.delete(url, params=query_params) as resp:
            return resp

    @staticmethod
    async def _wrap_http_errors(resp: ClientResponse) -> Optional[ClientError]:
        try:
            resp.raise_for_status()
        except ClientError as e:
            return e

    @staticmethod
    async def try_cast(
        obj_dict: dict, model: Type[BaseModel]
    ) -> Tuple[Optional[ValidationError], Optional[BaseModel]]:
        try:
            return None, model.model_validate(obj_dict)
        except ValidationError as e:
            return e, None

    async def send_message(
        self, mes: APIMessage
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APIMessageInfo]]:
        return await self.try_cast(
            await self._post(
                f"{self._base_url}/messages", json_payload=mes.model_dump()
            ),
            APIMessageInfo,
        )

    async def get_message(
        self, msg_id: int
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APIMessageInfo]]:
        return await self.try_cast(
            await self._get(f"{self._base_url}/messages/{msg_id}"), APIMessageInfo
        )

    async def get_messages(
        self, query_params: APIQueryMessageURIParams
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[ListAPIMessageInfo]]:
        return await self.try_cast(
            await self._get(
                f"{self._base_url}/messages", query_params=query_params.model_dump()
            ),
            ListAPIMessageInfo,
        )

    async def set_react(
        self, msg_id: int, react: APIReact
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        resp = await self._post_resp(
            f"{self._base_url}/messages/{msg_id}/reactions",
            json_payload=react.model_dump(),
        )

        if resp.status != 201:
            return await self._wrap_http_errors(resp), None

        return None, None

    async def get_reacts(
        self, msg_id: int, query_params: QueryParams = QueryParams()
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[ListAPIReactInfo]]:
        return await self.try_cast(
            await self._get(
                f"{self._base_url}/messages/{msg_id}/reactions",
                query_params=query_params.model_dump(),
            ),
            ListAPIReactInfo,
        )

    async def get_credentials_for_file(
        self,
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APISignFile]]:
        return await self.try_cast(
            await self._post(f"{self._base_url}/uploads"), APISignFile
        )

    async def upload_file(
        self, credentials: APISignFileInfo
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        resp = await self._post_resp(
            str(credentials.direct_url), json_payload=credentials.model_dump()
        )

        if resp.status != 204:
            return await self._wrap_http_errors(resp), None

        return None, None

    async def delete_message(
        self, msg_id: int
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        resp = await self._delete_resp(f"{self._base_url}/messages/{msg_id}")

        if resp.status == 404:
            return await self._wrap_http_errors(resp), None

        return None, None

    async def get_read_members(
        self, msg_id: int, query_params: QueryParams = QueryParams()
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[list[int]]]:
        ans = await self._get(
            f"{self._base_url}/messages/{msg_id}/read_member_ids",
            query_params=query_params.model_dump(),
        )

        if isinstance(ans, ClientError):
            return ans, None

        return None, ans["data"]


class PachcaManager(PachcaImpl):
    """Для взаимодействия в рамках одной сессии с Пачкой используй PachcaManager"""

    def __init__(self, token):
        self._session = ClientSession(headers={"Authorization": f"Bearer {token}"})
        super().__init__(self._session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()
