import { addTupleType, Tuple } from "@synerty/vortexjs";
import { diagramTuplePrefix } from "@peek/peek_plugin_diagram/_private/PluginNames";

@addTupleType
export class DiagramProcessingStatusTuple extends Tuple {
    public static readonly tupleName =
        diagramTuplePrefix + "DiagramProcessingStatusTuple";

    displayCompilerQueueStatus: boolean;
    displayCompilerQueueSize: number;
    displayCompilerProcessedTotal: number;
    displayCompilerLastError: string;
    displayCompilerQueueLastUpdateDate: Date;

    displayCompilerQueueTableTotal: number;
    displayCompilerQueueLastTableTotalUpdate: Date;

    gridCompilerQueueStatus: boolean;
    gridCompilerQueueSize: number;
    gridCompilerProcessedTotal: number;
    gridCompilerLastError: string;
    gridCompilerQueueLastUpdateDate: Date;

    gridCompilerQueueTableTotal: number;
    gridCompilerQueueLastTableTotalUpdate: Date;

    locationIndexCompilerQueueStatus: boolean;
    locationIndexCompilerQueueSize: number;
    locationIndexCompilerProcessedTotal: number;
    locationIndexCompilerLastError: string;
    locationIndexCompilerQueueLastUpdateDate: Date;

    locationIndexCompilerQueueTableTotal: number;
    locationIndexCompilerQueueLastTableTotalUpdate: Date;

    branchIndexCompilerQueueStatus: boolean;
    branchIndexCompilerQueueSize: number;
    branchIndexCompilerProcessedTotal: number;
    branchIndexCompilerLastError: string;
    branchIndexCompilerQueueLastUpdateDate: Date;

    branchIndexCompilerQueueTableTotal: number;
    branchIndexCompilerQueueLastTableTotalUpdate: Date;

    constructor() {
        super(DiagramProcessingStatusTuple.tupleName);
    }
}
