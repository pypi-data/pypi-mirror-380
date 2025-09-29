import { addTupleType, Tuple } from "@synerty/vortexjs";
import { searchTuplePrefix } from "../../PluginNames";

@addTupleType
export class AdminStatusTuple extends Tuple {
    public static readonly tupleName = searchTuplePrefix + "AdminStatusTuple";

    searchIndexCompilerQueueStatus: boolean;
    searchIndexCompilerQueueSize: number;
    searchIndexCompilerQueueProcessedTotal: number;
    searchIndexCompilerQueueLastError: string;
    searchIndexCompilerQueueLastUpdateDate: Date;
    searchIndexCompilerQueueTableTotal: number;
    searchIndexCompilerQueueLastTableTotalUpdate: Date;

    searchObjectCompilerQueueStatus: boolean;
    searchObjectCompilerQueueSize: number;
    searchObjectCompilerQueueProcessedTotal: number;
    searchObjectCompilerQueueLastError: string;
    searchObjectCompilerQueueLastUpdateDate: Date;
    searchObjectCompilerQueueTableTotal: number;
    searchObjectCompilerQueueLastTableTotalUpdate: Date;

    constructor() {
        super(AdminStatusTuple.tupleName);
    }
}