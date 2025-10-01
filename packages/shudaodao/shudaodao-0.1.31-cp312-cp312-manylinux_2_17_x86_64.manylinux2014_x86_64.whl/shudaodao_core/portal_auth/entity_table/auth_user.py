#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/9/2 下午4:24
# @Desc     ：

from datetime import datetime
from typing import Optional, Any

from pydantic import EmailStr, model_validator, computed_field
from sqlalchemy import BigInteger, Integer
from sqlmodel import SQLModel, Field

from .. import get_schema_name, auth_registry
from shudaodao_core.schemas.core_enum import UserStatus
from shudaodao_core.schemas.response import BaseResponse
from shudaodao_core.services.enum_service import EnumService
from shudaodao_core.utils.generate_unique_id import get_primary_id


class AuthUserBase(SQLModel, registry=auth_registry):
    auth_user_id: Optional[int] = Field(default_factory=get_primary_id, primary_key=True, sa_type=BigInteger)
    username: str = Field(unique=True, index=True, max_length=50)
    password: str
    email: Optional[EmailStr] = Field(default=None, nullable=True, max_length=100)
    is_active: bool = True
    status: Optional[UserStatus] = Field(default=None, nullable=True, sa_type=Integer)


class AuthUser(AuthUserBase, table=True):
    """ 数据模型 - 数据库表 T_Auth_User 结构模型 """
    __tablename__ = "t_auth_user"
    __table_args__ = {"schema": f"{get_schema_name()}", "comment": "鉴权用户表"}

    last_login: Optional[datetime] = Field(default_factory=lambda: datetime.now(), description="最后登录时间")
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())


class AuthUserResponse(BaseResponse):
    # auth_user_id: Optional[int] = Field(sa_type=BigInteger)
    username: str = Field(max_length=50)
    email: Optional[EmailStr] = Field(None, max_length=100)
    is_active: bool = True
    status: Optional[UserStatus]  # ← 枚举字段

    @computed_field
    @property
    def status_label(self) -> str:
        return self.status.label if self.status else None

    # @computed_field
    # @property
    # def status_description(self) -> str:
    #     return self.status.description


class AuthLogin(SQLModel):
    """ 登录模型 """
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=50)


class AuthRegister(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=50)
    email: Optional[EmailStr] = Field(default=None, max_length=50)

    # 输入字段：均为可选，且不设默认值
    status: Optional[int] = None
    status_label: Optional[str] = None

    # noinspection PyMethodParameters
    @model_validator(mode="before")
    def resolve_enums(cls, data: Any) -> Any:
        if isinstance(data, dict):
            EnumService.resolve_field(data, "status", UserStatus)
        return data


class AuthPassword(SQLModel):
    """ 修改密码模型 """
    old_password: str
    new_password: str = Field(min_length=6, max_length=50)
