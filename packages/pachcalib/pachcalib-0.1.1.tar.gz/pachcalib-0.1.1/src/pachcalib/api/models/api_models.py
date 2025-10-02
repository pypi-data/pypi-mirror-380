from pydantic import BaseModel

from .base_models import (
    Message,
    MessageInfo,
    QueryParams,
    React,
    ReactInfo,
    SignFile,
    SignFileInfo,
    SortFields,
)


class APIMessage(BaseModel):
    message: Message


class APIMessageInfo(BaseModel):
    data: MessageInfo


class ListAPIMessageInfo(BaseModel):
    data: list[MessageInfo]


class APIReact(React):
    pass


class APIReactInfo(BaseModel):
    data: ReactInfo


class APIQueryMessageURIParams(QueryParams):
    chat_id: int
    sort: SortFields = SortFields.sort_id


class APIQueryURIParams(QueryParams):
    pass


class APISignFile(SignFile):
    pass


class APISignFileInfo(SignFileInfo):
    pass


class ListAPIReactInfo(BaseModel):
    data: list[ReactInfo]
