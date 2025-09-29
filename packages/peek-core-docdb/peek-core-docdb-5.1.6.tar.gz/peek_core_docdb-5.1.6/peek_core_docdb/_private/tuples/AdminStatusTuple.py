from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_core_docdb._private.PluginNames import docDbTuplePrefix


@addTupleType
class AdminStatusTuple(Tuple):
    __tupleType__ = docDbTuplePrefix + "AdminStatusTuple"

    documentCompilerQueueStatus: bool = TupleField(False)
    documentCompilerQueueSize: int = TupleField(0)
    documentCompilerQueueProcessedTotal: int = TupleField(0)
    documentCompilerQueueTableTotal: int = TupleField(0)
    documentCompilerQueueLastError: str = TupleField()
    documentCompilerQueueLastUpdateDate: datetime = TupleField()
    documentCompilerQueueLastTableTotalUpdate: datetime = TupleField()
