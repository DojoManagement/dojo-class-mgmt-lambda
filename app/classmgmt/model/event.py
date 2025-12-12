from dojocommons.model.base_event import BaseEvent

from classmgmt.model.resource import Resource


class Event(BaseEvent):
    resource: str
