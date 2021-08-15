"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from akkaserverless.akkaserverless_service import AkkaServerlessService
from thing_eventsourced_entity import entity as thing_eventsourced_entity
from thing_value_entity import entity as thing_value_entity
from thing_view_value import view as thing_view_value
from thing_view_eventsourced import view as thing_view_eventsourced
from thing_action import action as thing_action
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    # create service and add components
    service = AkkaServerlessService()
    service.add_component(thing_value_entity)
    service.add_component(thing_view_value)
    service.add_component(thing_eventsourced_entity)
    service.add_component(thing_view_eventsourced)
    service.add_component(thing_action)
    service.start()
