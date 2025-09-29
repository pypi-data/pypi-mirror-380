from datetime import datetime

from vortex.Tuple import Tuple
from vortex.Tuple import TupleField
from vortex.Tuple import addTupleType

from peek_plugin_diagram._private.PluginNames import diagramTuplePrefix


@addTupleType
class DiagramProcessingStatusTuple(Tuple):
    __tupleType__ = diagramTuplePrefix + "DiagramProcessingStatusTuple"

    displayCompilerQueueStatus: bool = TupleField(False)
    displayCompilerQueueSize: int = TupleField(0)
    displayCompilerProcessedTotal: int = TupleField(0)
    displayCompilerLastError: str = TupleField()
    displayCompilerQueueLastUpdateDate: datetime = TupleField()
    displayCompilerQueueTableTotal: int = TupleField(0)
    displayCompilerQueueLastTableTotalUpdate: datetime = TupleField()

    gridCompilerQueueStatus: bool = TupleField(False)
    gridCompilerQueueSize: int = TupleField(0)
    gridCompilerProcessedTotal: int = TupleField(0)
    gridCompilerLastError: str = TupleField()
    gridCompilerQueueLastUpdateDate: datetime = TupleField()
    gridCompilerQueueTableTotal: int = TupleField(0)
    gridCompilerQueueLastTableTotalUpdate: datetime = TupleField()

    locationIndexCompilerQueueStatus: bool = TupleField(False)
    locationIndexCompilerQueueSize: int = TupleField(0)
    locationIndexCompilerProcessedTotal: int = TupleField(0)
    locationIndexCompilerLastError: str = TupleField()
    locationIndexCompilerQueueLastUpdateDate: datetime = TupleField()
    locationIndexCompilerQueueTableTotal: int = TupleField(0)
    locationIndexCompilerQueueLastTableTotalUpdate: datetime = TupleField()

    branchIndexCompilerQueueStatus: bool = TupleField(False)
    branchIndexCompilerQueueSize: int = TupleField(0)
    branchIndexCompilerProcessedTotal: int = TupleField(0)
    branchIndexCompilerLastError: str = TupleField()
    branchIndexCompilerQueueLastUpdateDate: datetime = TupleField()
    branchIndexCompilerQueueTableTotal: int = TupleField(0)
    branchIndexCompilerQueueLastTableTotalUpdate: datetime = TupleField()
