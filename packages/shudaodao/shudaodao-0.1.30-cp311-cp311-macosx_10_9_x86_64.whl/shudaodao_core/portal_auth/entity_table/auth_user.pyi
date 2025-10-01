from .. import auth_registry as auth_registry, get_schema_name as get_schema_name
from _typeshed import Incomplete
from datetime import datetime
from pydantic import EmailStr as EmailStr, computed_field
from shudaodao_core.schemas.core_enum import UserStatus as UserStatus
from shudaodao_core.schemas.response import BaseResponse as BaseResponse
from shudaodao_core.services.enum_service import EnumService as EnumService
from shudaodao_core.utils.generate_unique_id import get_primary_id as get_primary_id
from sqlmodel import SQLModel
from typing import Any

class AuthUserBase(SQLModel, registry=auth_registry):
    auth_user_id: int | None
    username: str
    password: str
    email: EmailStr | None
    is_active: bool
    status: UserStatus | None

class AuthUser(AuthUserBase, table=True):
    __tablename__: str
    __table_args__: Incomplete
    last_login: datetime | None
    created_at: datetime
    updated_at: datetime

class AuthUserResponse(BaseResponse):
    username: str
    email: EmailStr | None
    is_active: bool
    status: UserStatus | None
    @computed_field
    @property
    def status_label(self) -> str: ...

class AuthLogin(SQLModel):
    username: str
    password: str

class AuthRegister(SQLModel):
    username: str
    password: str
    email: EmailStr | None
    status: int | None
    status_label: str | None
    def resolve_enums(cls, data: Any) -> Any: ...

class AuthPassword(SQLModel):
    old_password: str
    new_password: str
