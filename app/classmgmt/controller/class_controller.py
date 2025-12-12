from dojocommons.controller.base_controller import BaseController
from dojocommons.model.app_configuration import AppConfiguration
from classmgmt.service.class_service import ClassService
from classmgmt.model.classes import Classes
from classmgmt.model.resource import Resource


class ClassController(BaseController[Classes]):
    def __init__(self, cfg: AppConfiguration):
        super().__init__(cfg, ClassService, Resource.CLASSES.value, Classes)