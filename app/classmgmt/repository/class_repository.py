from dojocommons.model.app_configuration import AppConfiguration
from dojocommons.repository.base_repository import BaseRepository
from classmgmt.model.classes import Classes

class ClassRepository(BaseRepository[Classes]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, Classes, "classes")