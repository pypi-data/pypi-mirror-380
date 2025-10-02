from abc import ABC, abstractmethod
from typing import Optional, Tuple, Type

from aiohttp import ClientError
from pydantic_core import ValidationError

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


class IPachca(ABC):
    _base_url = "https://api.pachca.com/api/shared/v1"

    @abstractmethod
    async def send_message(
        self, mes: APIMessage
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APIMessageInfo]]:
        pass

    @abstractmethod
    async def get_message(
        self, msg_id: int
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APIMessageInfo]]:
        pass

    @abstractmethod
    async def get_messages(
        self, query_params: APIQueryMessageURIParams
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[ListAPIMessageInfo]]:
        pass

    @abstractmethod
    async def set_react(
        self, msg_id: int, react: APIReact
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        pass

    @abstractmethod
    async def get_reacts(
        self, msg_id: int, query_params: QueryParams = QueryParams()
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[ListAPIReactInfo]]:
        pass

    @abstractmethod
    async def get_credentials_for_file(
        self,
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[APISignFileInfo]]:
        pass

    @abstractmethod
    async def upload_file(
        self, credentials: APISignFile
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        pass

    @abstractmethod
    async def delete_message(
        self, msg_id: int
    ) -> Tuple[Optional[ClientError | ValidationError], None]:
        pass

    @abstractmethod
    async def get_read_members(
        self, msg_id: int, query_params: QueryParams = QueryParams()
    ) -> Tuple[Optional[ClientError | ValidationError], Optional[list[int]]]:
        pass
