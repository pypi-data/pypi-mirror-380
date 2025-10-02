from datetime import datetime
from enum import Enum
from typing import Annotated, Optional

from pydantic import AnyUrl, BaseModel, Field, HttpUrl


class EntTypes(str, Enum):
    discuss = "discussion"
    thread = "thread"
    user = "user"


class FileTypes(str, Enum):
    file = "file"
    image = "image"


class File(BaseModel):
    key: str
    name: str
    file_type: FileTypes
    size: int
    width: int = 0
    height: int = 0


class Button(BaseModel):
    text: str
    url: AnyUrl
    data: str


class Message(BaseModel):
    entity_type: EntTypes
    entity_id: int
    content: str
    files: list[File] = []
    buttons: list[Button] = []
    parent_message_id: Optional[int] = None
    display_avatar_url: Optional[AnyUrl] = None
    display_name: str = None
    skip_invite_mentions: bool = True
    link_preview: bool = False


class FileInfo(BaseModel):
    id: int
    key: str
    name: str
    file_type: FileTypes
    url: HttpUrl
    width: Optional[int] = None
    height: Optional[int] = None


class Thread(BaseModel):
    id: int
    chat_id: int


class Forwarding(BaseModel):
    original_message_id: int
    original_chat_id: int
    author_id: int
    original_created_at: datetime
    original_thread_id: Optional[int] = None
    original_thread_message_id: Optional[int] = None
    original_thread_parent_chat_id: Optional[int] = None


class MessageInfo(BaseModel):
    id: int
    entity_type: EntTypes
    entity_id: int
    chat_id: int
    content: str
    user_id: int
    created_at: datetime
    url: HttpUrl
    files: Optional[list[FileInfo]] = []
    buttons: Optional[list[Button]] = []
    thread: Optional[Thread] = None
    forwarding: Optional[Forwarding] = None
    parent_message_id: Optional[int] = None
    display_avatar_url: Optional[AnyUrl] = None
    display_name: Optional[str] = None


class React(BaseModel):
    code: str


class ReactInfo(React):
    user_id: int
    created_at: datetime


class QueryParams(BaseModel):
    per: int = 25
    page: int = 1


class SortFields(str, Enum):
    sort_id = "sort[id]"


class BaseSignFile(BaseModel):
    content_disposition: Annotated[str, Field(str, alias="Content-Disposition")]
    acl: str
    policy: str
    x_amz_credential: Annotated[str, Field(str, alias="x-amz-credential")]
    x_amz_algorithm: Annotated[str, Field(str, alias="x-amz-algorithm")]
    x_amz_date: Annotated[str, Field(str, alias="x-amz-date")]
    x_amz_signature: Annotated[str, Field(str, alias="x-amz-signature")]
    key: str


class SignFileInfo(BaseSignFile):
    direct_url: HttpUrl


class SignFile(BaseSignFile):
    file: bytes
