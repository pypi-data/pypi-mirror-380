from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_plugin_graphdb._private.PluginNames import graphDbTuplePrefix


@addTupleType
class ServerStatusTuple(Tuple):
    __tupleType__ = graphDbTuplePrefix + "ServerStatusTuple"

    segmentCompilerQueueStatus: bool = TupleField(False)
    segmentCompilerQueueSize: int = TupleField(0)
    segmentCompilerQueueProcessedTotal: int = TupleField(0)
    segmentCompilerQueueTableTotal: int = TupleField(0)
    segmentCompilerQueueLastError: str = TupleField()
    segmentCompilerQueueLastUpdateDate: datetime = TupleField()
    segmentCompilerQueueLastTableTotalUpdate: datetime = TupleField()

    itemKeyIndexCompilerQueueStatus: bool = TupleField(False)
    itemKeyIndexCompilerQueueSize: int = TupleField(0)
    itemKeyIndexCompilerQueueProcessedTotal: int = TupleField(0)
    itemKeyIndexCompilerQueueTableTotal: int = TupleField(0)
    itemKeyIndexCompilerQueueLastError: str = TupleField()
    itemKeyIndexCompilerQueueLastUpdateDate: datetime = TupleField()
    itemKeyIndexCompilerQueueLastTableTotalUpdate: datetime = TupleField()
