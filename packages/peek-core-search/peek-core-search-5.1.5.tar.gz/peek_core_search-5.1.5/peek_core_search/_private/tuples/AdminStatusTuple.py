from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_core_search._private.PluginNames import searchTuplePrefix


@addTupleType
class AdminStatusTuple(Tuple):
    __tupleType__ = searchTuplePrefix + "AdminStatusTuple"

    searchIndexCompilerQueueStatus: bool = TupleField(False)
    searchIndexCompilerQueueSize: int = TupleField(0)
    searchIndexCompilerQueueProcessedTotal: int = TupleField(0)
    searchIndexCompilerQueueTableTotal: int = TupleField(0)
    searchIndexCompilerQueueLastError: str = TupleField()
    searchIndexCompilerQueueLastUpdateDate: datetime = TupleField()
    searchIndexCompilerQueueLastTableTotalUpdate: datetime = TupleField()

    searchObjectCompilerQueueStatus: bool = TupleField(False)
    searchObjectCompilerQueueSize: int = TupleField(0)
    searchObjectCompilerQueueProcessedTotal: int = TupleField(0)
    searchObjectCompilerQueueTableTotal: int = TupleField(0)
    searchObjectCompilerQueueLastError: str = TupleField()
    searchObjectCompilerQueueLastUpdateDate: datetime = TupleField()
    searchObjectCompilerQueueLastTableTotalUpdate: datetime = TupleField()
