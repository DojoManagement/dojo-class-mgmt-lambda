from dojocommons.model.app_configuration import AppConfiguration
from dojocommons.service.base_service import BaseService
from classmgmt.repository.class_repository import ClassRepository
from classmgmt.model.classes import Class

class ClassService(BaseService[Class]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, ClassRepository)