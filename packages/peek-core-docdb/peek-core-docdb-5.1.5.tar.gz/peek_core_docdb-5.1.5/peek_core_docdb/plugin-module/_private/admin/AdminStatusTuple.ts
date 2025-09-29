import { addTupleType, Tuple } from "@synerty/vortexjs";
import { docDbTuplePrefix } from "../PluginNames";

@addTupleType
export class AdminStatusTuple extends Tuple {
    public static readonly tupleName = docDbTuplePrefix + "AdminStatusTuple";

    documentCompilerQueueStatus: boolean;
    documentCompilerQueueSize: number;
    documentCompilerQueueProcessedTotal: number;
    documentCompilerQueueLastError: string;
    documentCompilerQueueLastUpdateDate: Date;

    documentCompilerQueueTableTotal: number;
    documentCompilerQueueLastTableTotalUpdate: Date;

    constructor() {
        super(AdminStatusTuple.tupleName);
    }
}
