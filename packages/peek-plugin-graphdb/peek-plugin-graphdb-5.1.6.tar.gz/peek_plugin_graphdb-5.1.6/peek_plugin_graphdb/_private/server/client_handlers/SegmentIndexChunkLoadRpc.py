import logging

from sqlalchemy import select
from vortex.Tuple import Tuple
from vortex.rpc.RPC import vortexRPC

from peek_abstract_chunked_index.private.server.client_handlers.ACIChunkLoadRpcABC import (
    ACIChunkLoadRpcABC,
)
from peek_plugin_base.PeekVortexUtil import peekBackendNames
from peek_plugin_base.PeekVortexUtil import peekServerName
from peek_plugin_base.storage.DbConnection import DbSessionCreator
from peek_plugin_graphdb._private.PluginNames import graphDbFilt
from peek_plugin_graphdb._private.storage.GraphDbEncodedChunk import (
    GraphDbEncodedChunk,
)
from peek_plugin_graphdb._private.storage.GraphDbModelSet import GraphDbModelSet
from peek_plugin_graphdb._private.tuples.SegmentIndexUpdateDateTuple import (
    SegmentIndexUpdateDateTuple,
)

logger = logging.getLogger(__name__)


class SegmentIndexChunkLoadRpc(ACIChunkLoadRpcABC):
    def __init__(self, dbSessionCreator: DbSessionCreator):
        self._dbSessionCreator = dbSessionCreator

    def makeHandlers(self):
        """Make Handlers

        In this method we start all the RPC handlers
        start() returns an instance of it's self so we can simply yield the result
        of the start method.

        """

        yield self.loadSegmentChunks.start(funcSelf=self)
        yield self.loadSegmentIndexDelta.start(funcSelf=self)
        logger.debug("RPCs started")

    # -------------
    @vortexRPC(
        peekServerName,
        acceptOnlyFromVortex=peekBackendNames,
        timeoutSeconds=120,
        additionalFilt=graphDbFilt,
        deferToThread=True,
    )
    def loadSegmentIndexDelta(self, indexEncodedPayload: bytes) -> bytes:
        return self.ckiChunkIndexDeltaBlocking(
            indexEncodedPayload,
            GraphDbEncodedChunk,
            SegmentIndexUpdateDateTuple,
        )

    # -------------
    @vortexRPC(
        peekServerName,
        acceptOnlyFromVortex=peekBackendNames,
        timeoutSeconds=120,
        additionalFilt=graphDbFilt,
        deferToThread=True,
    )
    def loadSegmentChunks(self, chunkKeys: list[str]) -> list[Tuple]:
        """Load Segment Chunks

        Allow the client to incrementally load the chunks.

        """
        chunkTable = GraphDbEncodedChunk.__table__
        msTable = GraphDbModelSet.__table__

        sql = (
            select(
                msTable.c.key,
                chunkTable.c.chunkKey,
                chunkTable.c.encodedData,
                chunkTable.c.encodedHash,
                chunkTable.c.lastUpdate,
            )
            .select_from(chunkTable.join(msTable))
            .where(chunkTable.c.chunkKey.in_(chunkKeys))
        )

        return self.ckiInitialLoadChunksPayloadBlocking(
            chunkKeys, GraphDbEncodedChunk, sql
        )
