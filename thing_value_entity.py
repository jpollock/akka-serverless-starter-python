"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from dataclasses import dataclass, field
from typing import MutableSet

from google.protobuf.empty_pb2 import Empty

from akkaserverless.value_context import ValueEntityCommandContext
from akkaserverless.value_entity import ValueEntity
from thing_domain_pb2 import (ThingState, DESCRIPTOR as DOMAIN_DESCRIPTOR)
from thing_api_value_entity_pb2 import (Thing, _GETTHINGCOMMAND, _THINGVALUESERVICE, DESCRIPTOR as API_DESCRIPTOR)


import statistics


def init(entity_id: str) -> ThingState:
    cs = ThingState()
    cs.name = ""
    return cs


entity = ValueEntity(_THINGVALUESERVICE, [API_DESCRIPTOR, DOMAIN_DESCRIPTOR], 'value_things', init)

@entity.command_handler("AddThing")
def add(state: ThingState, command: Thing, context: ValueEntityCommandContext):
    state.thing_id = command.thing_id
    state.name = command.name
    return state
    
@entity.command_handler("GetThing")
def get(state: ThingState):
    return state
