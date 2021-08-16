"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from dataclasses import dataclass, field
from typing import MutableSet

from google.protobuf.empty_pb2 import Empty

from akkaserverless.event_sourced_context import EventSourcedCommandContext
from akkaserverless.event_sourced_entity import EventSourcedEntity
from akkaserverless.value_context import ValueEntityCommandContext
from akkaserverless.value_entity import ValueEntity
from thing_domain_pb2 import (ThingState, DESCRIPTOR as DOMAIN_DESCRIPTOR)
from thing_api_eventsourced_entity_pb2 import (Thing, _GETTHINGCOMMAND, _THINGEVENTSOURCEDSERVICE, DESCRIPTOR as API_DESCRIPTOR)
#ThingAdded

import statistics


def init(entity_id: str) -> ThingState:
    cs = ThingState()
    cs.name = ""
    return cs


entity = EventSourcedEntity(_THINGEVENTSOURCEDSERVICE, [API_DESCRIPTOR, DOMAIN_DESCRIPTOR], 'event_things', init)

'''
# Event Sourced
'''

@entity.command_handler("AddThing")
def add(state: ThingState, command: Thing, context: EventSourcedCommandContext):
    np = ThingState(thing_id= command.thing_id, name=command.name)
    context.emit(np)
    return Empty()

@entity.command_handler("GetThing")
def get(state: ThingState):
    return state

@entity.event_handler(ThingState)
def added(state: ThingState, event: ThingState ):
    state.thing_id = event.thing_id
    state.name = event.name
    return state