from dojocommons.model.app_configuration import AppConfiguration
from classmgmt.controller.class_controller import ClassController
from classmgmt.model.event import Event
from classmgmt.model.response import Response
import json

def lambda_handler(event, _):
    print("[DEBUG][Lambda] Evento recebido:", json.dumps(event))
    try:
        event_obj = Event.model_validate(event)
        cfg = AppConfiguration()  # type: ignore
        controller = ClassController(cfg)
        response = controller.dispatch(event_obj)
    except ValueError as err:
        response = Response(status_code=400, body=str(err))

    return response.model_dump(by_alias=True, exclude_none=True)