from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_plugin_livedb._private.PluginNames import livedbTuplePrefix


@addTupleType
class AdminStatusTuple(Tuple):
    __tupleType__ = livedbTuplePrefix + "AdminStatusTuple"

    rawValueQueueStatus: bool = TupleField(False)
    rawValueQueueSize: int = TupleField(0)
    rawValueProcessedTotal: int = TupleField(0)
    rawValueLastError: str = TupleField()
    rawValueQueueLastUpdateDate: datetime = TupleField()
    rawValueTableTotal: int = TupleField(0)
    rawValueQueueLastTableTotalUpdate: datetime = TupleField()
