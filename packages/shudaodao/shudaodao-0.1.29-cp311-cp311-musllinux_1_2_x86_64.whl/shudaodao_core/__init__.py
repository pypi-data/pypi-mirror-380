#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @License  ：(C)Copyright 2025, 数道智融科技
# @Author   ：李锋
# @Software ：PyCharm
# @Date     ：2025/8/26 下午12:11
# @Desc     ：

from fastapi import Depends as _Depends
from sqlalchemy.engine import Engine as _Engine
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlmodel import create_engine as _create_engine
from sqlmodel.ext.asyncio.session import AsyncSession as _AsyncSession

from .app.base_app import BaseApplication
from .auth.auth_router import AuthRouter
from .config.app_config import AppConfig
from .config.running_config import RunningConfig
from .engine.database_engine import DatabaseEngine
from .engine.disk_engine import DiskEngine
from .engine.redis_engine import RedisEngine
from .exception.register_handlers import register_exception_handlers
from .exception.service_exception import (
    AuthException,
    LoginException,
    PermissionException,
    ServiceErrorException,
    DataNotFoundException
)
from .generate.config import GeneratorConfig
from .logger.logging_ import logging
from .schemas.query_request import QueryRequest
from .schemas.response import BaseResponse
from .services.auth_service import AuthService
from .services.data_service import DataService
from .services.db_engine_service import DBEngineService
from .services.generate_service import GeneratorService
from .services.enum_service import EnumService
from .utils.core_utils import CoreUtil
from .utils.generate_unique_id import get_primary_str, get_primary_id
from .utils.response_utils import ResponseUtil

AsyncSession = _AsyncSession
Engine = _Engine
create_engine = _create_engine
create_async_engine = _create_async_engine
Depends = _Depends
