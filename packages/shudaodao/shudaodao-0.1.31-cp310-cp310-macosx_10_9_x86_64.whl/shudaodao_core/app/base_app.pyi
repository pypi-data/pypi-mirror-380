import abc
from ..auth.auth_router import AuthRouter as AuthRouter
from ..config.app_config import AppConfig as AppConfig
from ..config.schemas.routers import RouterConfigSetting as RouterConfigSetting
from ..engine.database_engine import DatabaseEngine as DatabaseEngine
from ..logger.logging_ import logging as logging
from ..portal_auth import auth_registry as auth_registry
from ..services.casbin_service import PermissionService as PermissionService
from ..tools.class_scaner import ClassScanner as ClassScanner
from ..utils.core_utils import CoreUtil as CoreUtil
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from fastapi import FastAPI

class BaseApplication(ABC, metaclass=abc.ABCMeta):
    app: Incomplete
    def __init__(self) -> None: ...
    @abstractmethod
    def application_init(self, app: FastAPI) -> None: ...
    @abstractmethod
    async def application_load(self) -> None: ...
    @abstractmethod
    async def application_unload(self): ...
