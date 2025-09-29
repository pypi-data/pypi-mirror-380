from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_plugin_eventdb._private.PluginNames import eventdbTuplePrefix


@addTupleType
class AdminStatusTuple(Tuple):
    __tupleType__ = eventdbTuplePrefix + "AdminStatusTuple"

    lastUpdateDate: datetime = TupleField()

    addedEvents: int = TupleField(0)
    removedEvents: int = TupleField(0)
    updatedAlarmFlags: int = TupleField(0)
    lastActivity: datetime = TupleField()
