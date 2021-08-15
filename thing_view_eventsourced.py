"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from dataclasses import dataclass, field
from typing import MutableSet

from google.protobuf.empty_pb2 import Empty

from akkaserverless.view import View
from thing_view_eventsourced_pb2 import (_THINGVIEW, DESCRIPTOR as FILE_DESCRIPTOR)

view = View(_THINGVIEW,[FILE_DESCRIPTOR])
