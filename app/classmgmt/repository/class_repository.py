from dojocommons.model.app_configuration import AppConfiguration
from dojocommons.repository.base_repository import BaseRepository
from classmgmt.model.classes import Class

class ClassRepository(BaseRepository[Class]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, Class, "class")