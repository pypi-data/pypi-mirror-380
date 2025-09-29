import { Observable, Subject } from "rxjs";
import { filter, first, takeUntil } from "rxjs/operators";
import { Injectable } from "@angular/core";
import {
    NgLifeCycleEvents,
    Payload,
    PayloadEnvelope,
    TupleOfflineStorageNameService,
    TupleOfflineStorageService,
    TupleSelector,
    TupleStorageBatchSaveArguments,
    TupleStorageFactoryService,
    VortexService,
    VortexStatusService,
} from "@synerty/vortexjs";

import {
    searchFilt,
    searchObjectCacheStorageName,
    searchTuplePrefix,
} from "../PluginNames";
import { EncodedSearchObjectChunkTuple } from "./EncodedSearchObjectChunkTuple";
import { SearchObjectUpdateDateTuple } from "./SearchObjectUpdateDateTuple";
import { SearchResultObjectTuple } from "../../SearchResultObjectTuple";
import { SearchResultObjectRouteTuple } from "../../SearchResultObjectRouteTuple";
import { SearchTupleService } from "../SearchTupleService";
import { SearchObjectTypeTuple } from "../../SearchObjectTypeTuple";
import {
    DeviceOfflineCacheService,
    OfflineCacheLoaderStatusTuple,
} from "@peek/peek_core_device";
import { SearchIndexUpdateDateTuple } from "@peek/peek_core_search/_private";

// ----------------------------------------------------------------------------

let clientSearchObjectWatchUpdateFromDeviceFilt = Object.assign(
    { key: "clientSearchObjectWatchUpdateFromDevice" },
    searchFilt,
);

const cacheAll = "cacheAll";

// ----------------------------------------------------------------------------
/** SearchObjectChunkTupleSelector
 *
 * This is just a short cut for the tuple selector
 */

class SearchObjectChunkTupleSelector extends TupleSelector {
    constructor(private chunkKey: string) {
        super(searchTuplePrefix + "SearchObjectChunkTuple", { key: chunkKey });
    }

    override toOrderedJsonStr(): string {
        return this.chunkKey.toString();
    }
}

// ----------------------------------------------------------------------------
/** UpdateDateTupleSelector
 *
 * This is just a short cut for the tuple selector
 */
class UpdateDateTupleSelector extends TupleSelector {
    constructor() {
        super(SearchObjectUpdateDateTuple.tupleName, {});
    }
}

// ----------------------------------------------------------------------------
/** hash method
 */
let OBJECT_BUCKET_COUNT = 8192;

function objectIdChunk(objectId: number): string {
    /** Object ID Chunk

     This method creates an int from 0 to MAX, representing the hash bucket for this
     object Id.

     This is simple, and provides a reasonable distribution

     @param objectId: The ID if the object to get the chunk key for

     @return: The bucket / chunkKey where you'll find the object with this ID

     */
    if (objectId == null) throw new Error("objectId None or zero length");

    return (objectId & (OBJECT_BUCKET_COUNT - 1)).toString();
}

// ----------------------------------------------------------------------------
/** SearchObject Cache
 *
 * This class has the following responsibilities:
 *
 * 1) Maintain a local storage of the index
 *
 * 2) Return DispKey searchs based on the index.
 *
 */
@Injectable()
export class PrivateSearchObjectLoaderService extends NgLifeCycleEvents {
    private UPDATE_CHUNK_FETCH_SIZE = 5;

    // Every 100 chunks from the server
    private SAVE_POINT_ITERATIONS = 100;

    // Saving the cache after each chunk is so expensive, we only do it every 20 or so
    private chunksSavedSinceLastIndexSave = 0;

    private index: SearchObjectUpdateDateTuple | null = null;
    private askServerChunks: SearchObjectUpdateDateTuple[] = [];

    private _hasLoaded = false;

    private _hasLoadedSubject = new Subject<void>();
    private storage: TupleOfflineStorageService;

    private _statusSubject = new Subject<OfflineCacheLoaderStatusTuple>();
    private _status = new OfflineCacheLoaderStatusTuple();

    constructor(
        private vortexService: VortexService,
        private vortexStatusService: VortexStatusService,
        storageFactory: TupleStorageFactoryService,
        private tupleService: SearchTupleService,
        private deviceCacheControllerService: DeviceOfflineCacheService,
    ) {
        super();

        this._status.pluginName = "peek_core_search";
        this._status.indexName = "Object Index";

        this.storage = new TupleOfflineStorageService(
            storageFactory,
            new TupleOfflineStorageNameService(searchObjectCacheStorageName),
        );

        this.setupVortexSubscriptions();

        this.deviceCacheControllerService.offlineModeEnabled$
            .pipe(takeUntil(this.onDestroyEvent))
            .pipe(filter((v) => v))
            .pipe(first())
            .subscribe(() => {
                this.initialLoad();
            });

        this.deviceCacheControllerService.triggerCachingStartObservable
            .pipe(takeUntil(this.onDestroyEvent))
            .pipe(filter((v) => v))
            .subscribe(() => {
                this.askServerForUpdates();
                this._notifyStatus();
            });

        this.deviceCacheControllerService.triggerCachingResumeObservable
            .pipe(takeUntil(this.onDestroyEvent))

            .subscribe(() => {
                this._notifyStatus();
                this.askServerForNextUpdateChunk();
            });
    }

    isReady(): boolean {
        return this._hasLoaded;
    }

    isReadyObservable(): Observable<void> {
        return this._hasLoadedSubject;
    }

    statusObservable(): Observable<OfflineCacheLoaderStatusTuple> {
        return this._statusSubject;
    }

    status(): OfflineCacheLoaderStatusTuple {
        return this._status;
    }

    get offlineEnabled(): boolean {
        return this.index.initialLoadComplete;
    }

    /** Get Objects
     *
     * Get the objects with matching keywords from the index..
     *
     */
    getObjects(
        objectTypeId: number | null,
        objectIds: number[],
    ): Promise<SearchResultObjectTuple[]> {
        if (objectIds == null || objectIds.length == 0) {
            throw new Error("We've been passed a null/empty objectIds");
        }

        if (this.isReady())
            return this.getObjectsWhenReady(objectTypeId, objectIds);

        return this.isReadyObservable()
            .pipe(first())
            .toPromise()
            .then(() => this.getObjectsWhenReady(objectTypeId, objectIds));
    }

    private _notifyReady(): void {
        if (this._hasLoaded) this._hasLoadedSubject.next();
    }

    private _notifyStatus(paused: boolean = false): void {
        this._status.lastCheckDate = new Date();
        this._status.paused = paused;
        this._status.initialFullLoadComplete = this.index.initialLoadComplete;

        this._status.loadingQueueCount = 0;
        for (let chunk of this.askServerChunks) {
            this._status.loadingQueueCount += Object.keys(
                chunk.updateDateByChunkKey,
            ).length;
        }

        this._statusSubject.next(this._status);
        this.deviceCacheControllerService.updateLoaderCachingStatus(
            this._status,
        );
    }

    /** Initial load
     *
     * Load the dates of the index buckets and ask the server if it has any updates.
     */
    private initialLoad(): void {
        this.storage
            .loadTuples(new UpdateDateTupleSelector())
            .then((tuplesAny: any[]) => {
                let tuples: SearchObjectUpdateDateTuple[] = tuplesAny;
                if (tuples.length === 0) {
                    this.index = new SearchObjectUpdateDateTuple();
                } else {
                    this.index = tuples[0];

                    if (this.index.initialLoadComplete) {
                        this._hasLoaded = true;
                        this._notifyReady();
                    }
                }

                this._notifyStatus();
            });
    }

    private setupVortexSubscriptions(): void {
        // Services don't have destructors, I'm not sure how to unsubscribe.
        this.vortexService
            .createEndpointObservable(
                this,
                clientSearchObjectWatchUpdateFromDeviceFilt,
            )
            .pipe(takeUntil(this.onDestroyEvent))
            .subscribe((payloadEnvelope: PayloadEnvelope) => {
                this.processChunksFromServer(payloadEnvelope);
            });
    }

    private areWeTalkingToTheServer(): boolean {
        return (
            this.deviceCacheControllerService.offlineModeEnabled &&
            this.vortexStatusService.snapshot.isOnline
        );
    }

    /** Ask Server For Updates
     *
     * Tell the server the state of the chunks in our index and ask if there
     * are updates.
     *
     */
    private askServerForUpdates() {
        if (!this.areWeTalkingToTheServer()) return;

        // If we're still caching, then exit
        if (this.askServerChunks.length != 0) {
            this.askServerForNextUpdateChunk();
            return;
        }

        this.tupleService.observer
            .pollForTuples(new UpdateDateTupleSelector())
            .then((tuplesAny: any) => {
                let serverIndex: SearchObjectUpdateDateTuple = tuplesAny[0];
                let keys = Object.keys(serverIndex.updateDateByChunkKey);
                let keysNeedingUpdate: string[] = [];

                this._status.totalLoadedCount = keys.length;

                // Tuples is an array of strings
                for (let chunkKey of keys) {
                    if (
                        !this.index.updateDateByChunkKey.hasOwnProperty(
                            chunkKey,
                        )
                    ) {
                        this.index.updateDateByChunkKey[chunkKey] = null;
                        keysNeedingUpdate.push(chunkKey);
                    } else if (
                        this.index.updateDateByChunkKey[chunkKey] !=
                        serverIndex.updateDateByChunkKey[chunkKey]
                    ) {
                        keysNeedingUpdate.push(chunkKey);
                    }
                }
                this.queueChunksToAskServer(keysNeedingUpdate);
            });
    }

    /** Queue Chunks To Ask Server
     *
     */
    private queueChunksToAskServer(keysNeedingUpdate: string[]) {
        if (!this.areWeTalkingToTheServer()) return;

        this.askServerChunks = [];

        let count = 0;
        let indexChunk = new SearchObjectUpdateDateTuple();

        for (let key of keysNeedingUpdate) {
            indexChunk.updateDateByChunkKey[key] =
                this.index.updateDateByChunkKey[key] || "";
            count++;

            if (count == this.UPDATE_CHUNK_FETCH_SIZE) {
                this.askServerChunks.push(indexChunk);
                count = 0;
                indexChunk = new SearchObjectUpdateDateTuple();
            }
        }

        if (count) this.askServerChunks.push(indexChunk);

        this.askServerForNextUpdateChunk();

        this._status.lastCheckDate = new Date();
    }

    private askServerForNextUpdateChunk() {
        if (!this.areWeTalkingToTheServer()) return;

        if (this.askServerChunks.length == 0) return;

        if (this.deviceCacheControllerService.isOfflineCachingPaused) {
            this.saveChunkCacheIndex(true) //
                .catch((e) => console.log(`ERROR saveChunkCacheIndex: ${e}`));
            this._notifyStatus(true);
            return;
        }

        let indexChunk: SearchObjectUpdateDateTuple =
            this.askServerChunks.pop();
        let filt = Object.assign(
            {},
            clientSearchObjectWatchUpdateFromDeviceFilt,
        );
        filt[cacheAll] = true;
        let pl = new Payload(filt, [indexChunk]);
        this.vortexService.sendPayload(pl);

        this._status.lastCheckDate = new Date();
        this._notifyStatus();
    }

    /** Process SearchObjects From Server
     *
     * Process the grids the server has sent us.
     */
    private async processChunksFromServer(
        payloadEnvelope: PayloadEnvelope,
    ): Promise<void> {
        if (payloadEnvelope.result != null && payloadEnvelope.result != true) {
            console.log(`ERROR: ${payloadEnvelope.result}`);
            return;
        }

        const tuplesToSave: EncodedSearchObjectChunkTuple[] = <
            EncodedSearchObjectChunkTuple[]
        >payloadEnvelope.data;

        try {
            await this.storeChunkTuples(tuplesToSave);
        } catch (e) {
            console.log(`SearchObjectCache.storeSearchObjectPayload: ${e}`);
        }

        if (this.askServerChunks.length == 0) {
            this.index.initialLoadComplete = true;
            await this.saveChunkCacheIndex(true);
            this._hasLoaded = true;
            this._hasLoadedSubject.next();
        } else if (payloadEnvelope.filt[cacheAll] == true) {
            this.askServerForNextUpdateChunk();
        }

        this._notifyStatus();
    }

    /** Store Index Bucket
     * Stores the index bucket in the local db.
     */
    private async storeChunkTuples(
        tuplesToSave: EncodedSearchObjectChunkTuple[],
    ): Promise<void> {
        // noinspection BadExpressionStatementJS
        const Selector = SearchObjectChunkTupleSelector;

        if (tuplesToSave.length == 0) return;

        const batchStore: TupleStorageBatchSaveArguments[] = [];
        for (const tuple of tuplesToSave) {
            batchStore.push({
                tupleSelector: new Selector(tuple.chunkKey),
                vortexMsg: tuple.encodedData,
            });
        }

        await this.storage.batchSaveTuplesEncoded(batchStore);

        for (const tuple of tuplesToSave) {
            this.index.updateDateByChunkKey[tuple.chunkKey] = tuple.lastUpdate;
        }
        await this.saveChunkCacheIndex(true);
    }

    /** Store Chunk Cache Index
     *
     * Updates our running tab of the update dates of the cached chunks
     *
     */
    private async saveChunkCacheIndex(force = false): Promise<void> {
        if (
            this.chunksSavedSinceLastIndexSave <= this.SAVE_POINT_ITERATIONS &&
            !force
        ) {
            return;
        }

        this.chunksSavedSinceLastIndexSave = 0;

        await this.storage.saveTuples(new UpdateDateTupleSelector(), [
            this.index,
        ]);
    }

    /** Get Objects When Ready
     *
     * Get the objects with matching keywords from the index..
     *
     */
    private getObjectsWhenReady(
        objectTypeId: number | null,
        objectIds: number[],
    ): Promise<SearchResultObjectTuple[]> {
        let objectIdsByChunkKey: { [key: number]: number[] } = {};
        let chunkKeys: string[] = [];

        for (let objectId of objectIds) {
            let chunkKey: string = objectIdChunk(objectId);
            if (objectIdsByChunkKey[chunkKey] == null)
                objectIdsByChunkKey[chunkKey] = [];
            objectIdsByChunkKey[chunkKey].push(objectId);
            chunkKeys.push(chunkKey);
        }

        let promises = [];
        for (let chunkKey of chunkKeys) {
            let objectIds = objectIdsByChunkKey[chunkKey];
            promises.push(
                this.getObjectsForObjectIds(objectTypeId, objectIds, chunkKey),
            );
        }

        const objectIdsAdded = new Set<number>();
        return Promise.all(promises).then(
            (listOfObjectLists: SearchResultObjectTuple[][]) => {
                let objectsToReturn: SearchResultObjectTuple[] = [];
                for (let listOfObjects of listOfObjectLists) {
                    for (let objectTuple of listOfObjects) {
                        if (!objectIdsAdded.has(objectTuple.id)) {
                            objectIdsAdded.add(objectTuple.id);
                            objectsToReturn.push(objectTuple);
                        }
                    }
                }
                return objectsToReturn;
            },
        );
    }

    /** Get Objects for Object ID
     *
     * Get the objects with matching keywords from the index.
     *
     */
    private getObjectsForObjectIds(
        objectTypeId: number | null,
        objectIds: number[],
        chunkKey: string,
    ): Promise<SearchResultObjectTuple[]> {
        if (!this.index.updateDateByChunkKey.hasOwnProperty(chunkKey)) {
            console.log(`ObjectIDs: ${objectIds} doesn't appear in the index`);
            return Promise.resolve([]);
        }

        let retPromise: any;
        retPromise = this.storage
            .loadTuplesEncoded(new SearchObjectChunkTupleSelector(chunkKey))
            .then((vortexMsg: string) => {
                if (vortexMsg == null) {
                    return [];
                }

                return Payload.fromEncodedPayload(vortexMsg)
                    .then((payload: Payload) => JSON.parse(<any>payload.tuples))
                    .then((chunkData: { [key: number]: string }) => {
                        let foundObjects: SearchResultObjectTuple[] = [];

                        for (let objectId of objectIds) {
                            // Find the keyword, we're just iterating
                            if (!chunkData.hasOwnProperty(objectId)) {
                                console.log(
                                    `WARNING: ObjectID ${objectId} is missing from index,` +
                                        ` chunkKey ${chunkKey}`,
                                );
                                continue;
                            }

                            // Reconstruct the data
                            let objectProps: {} = JSON.parse(
                                chunkData[objectId],
                            );

                            // Get out the object type
                            let thisObjectTypeId = objectProps["_otid_"];
                            delete objectProps["_otid_"];

                            // If the property is set, then make sure it matches
                            if (
                                objectTypeId != null &&
                                objectTypeId != thisObjectTypeId
                            )
                                continue;

                            // Get out the routes
                            let routes: string[][] = objectProps["_r_"];
                            delete objectProps["_r_"];

                            // Get the key
                            let objectKey: string = objectProps["key"];

                            // Create the new object
                            let newObject = new SearchResultObjectTuple();
                            foundObjects.push(newObject);

                            newObject.id = objectId;
                            newObject.key = objectKey;
                            newObject.objectType = new SearchObjectTypeTuple();
                            newObject.objectType.id = thisObjectTypeId;
                            newObject.properties = objectProps;

                            for (let route of routes) {
                                let newRoute =
                                    new SearchResultObjectRouteTuple();
                                newObject.routes.push(newRoute);

                                newRoute.title = route[0];
                                newRoute.path = route[1];
                            }
                        }

                        return foundObjects;
                    });
            });

        return retPromise;
    }
}
