import { addTupleType, Tuple } from "@synerty/vortexjs";
import { livedbTuplePrefix } from "@peek/peek_plugin_livedb/_private/PluginNames";

@addTupleType
export class AdminStatusTuple extends Tuple {
    public static readonly tupleName = livedbTuplePrefix + "AdminStatusTuple";

    rawValueQueueStatus: boolean;
    rawValueQueueSize: number;
    rawValueProcessedTotal: number;
    rawValueLastError: string;
    rawValueQueueLastUpdateDate: Date;

    // LiveDB Compiler Queue fields
    rawValueTableTotal: number;
    rawValueQueueLastTableTotalUpdate: Date;

    constructor() {
        super(AdminStatusTuple.tupleName);
    }
}
