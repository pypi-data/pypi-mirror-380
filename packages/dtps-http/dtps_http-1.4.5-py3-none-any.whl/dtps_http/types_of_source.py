import copy
import time
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, replace
from typing import Any, cast, Dict, List, Optional, Sequence, Tuple, TYPE_CHECKING, Union

import aiohttp
import cbor2
import jsonpatch
import jsonpointer  # type: ignore
from aiohttp import ClientResponse, web
from aiohttp.web_response import Response
from jsonpatch import JsonPatch

from . import logger
from .constants import (
    CONTENT_TYPE_DTPS_INDEX_CBOR,
    CONTENT_TYPE_PATCH_CBOR,
    DEFAULT_DATA_AVAILABILITY_TIMEOUT,
)
from .object_queue import PostResult, TransformError
from .structures import (
    Bounds,
    ContentInfo,
    DataReady,
    DataSaved,
    LinkBenchmark,
    RawData,
    ResourceAvailability,
    TopicProperties,
    TopicReachability,
    TopicRef,
    TopicsIndex,
)
from .types import ContentType, HTTPRequest, NodeID, SourceID, TopicNameV
from .urls import get_relative_url, join, parse_url_unescape, URL
from .utils import pydantic_parse

__all__ = [
    "ForwardedQueue",
    "Native",
    "NotAvailableYet",
    "NotFound",
    "OurQueue",
    "Source",
    "SourceComposition",
    "Transformed",
    "TypeOfSource",
]


@dataclass
class Native:
    ob: object


@dataclass
class NotAvailableYet:
    comment: str


@dataclass
class NotFound:
    comment: str


ResolvedData = Union[RawData, Native, NotAvailableYet, NotFound, Response]

if TYPE_CHECKING:
    from .server import DTPSServer
    from .client import DTPSClient


class Source(ABC):
    def resolve_extra(self, components: Tuple[str, ...], extra: Optional[str]) -> "Source":
        if not components:
            if extra is None:
                return self
            else:
                return self.get_inside_after(extra)
        else:
            first, *rest = components
            return self.get_inside(first).resolve_extra(tuple(rest), extra)

    @abstractmethod
    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        raise NotImplementedError(f"Source.get_properties() for {self}")

    @abstractmethod
    def get_inside_after(self, s: str) -> "Source": ...

    @abstractmethod
    def get_inside(self, s: str, /) -> "Source":
        """source / "a" / "b" """
        ...

    @abstractmethod
    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData": ...

    @abstractmethod
    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        raise NotImplementedError(f"Source.get_meta_info() for {self}")

    @abstractmethod
    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult": ...

    @abstractmethod
    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult": ...

    @abstractmethod
    async def delete(self, presented_as: str, server: "DTPSServer") -> "Optional[TransformError]": ...

    @abstractmethod
    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]: ...

    @abstractmethod
    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]: ...


class Transform(ABC):
    @abstractmethod
    def transform(self, data: "ResolvedData") -> "ResolvedData": ...

    def get_transform_inside(self, s: str) -> "Transform":
        raise NotImplementedError(f"Transform.get_transform_inside() for {self}")


@dataclass
class GetInside(Transform):
    components: Tuple[str, ...]

    def __post_init__(self):
        if ":meta" in self.components:
            raise ValueError(f"should have resolved :meta")

    def get_transform_inside(self, s: str) -> "Transform":
        return GetInside(self.components + (s,))

    def transform(self, data: "ResolvedData") -> "ResolvedData":
        if isinstance(data, RawData):
            ob = data.get_as_native_object()
            return Native(self.apply(ob))
        elif isinstance(data, Native):
            return Native(self.apply(data.ob))
        elif isinstance(data, NotAvailableYet):
            return data
        else:
            assert isinstance(data, NotFound)
            return data

        # raise NotImplementedError(f"Transform.transform() for {self}")

    def apply(self, ob: object) -> object:
        return get_inside(ob, (), ob, self.components)


def get_inside(
    original_ob: object, context: Tuple[Union[int, str], ...], ob: object, components: Sequence[str]
) -> object:
    if not components:
        return ob

    first, *rest = components

    if isinstance(ob, dict):
        ob = cast(Dict[str, Any], ob)
        if first not in ob:
            keys: List[Any] = list(ob.keys())  # type: ignore
            raise KeyError(
                f"cannot get_inside({components!r}) of dict with keys {keys!r}\ncontext: "
                f"{context!r}\noriginal:\n{original_ob!r}"
            )
        v: Any = ob[first]
        return get_inside(original_ob, context + (first,), v, rest)
    elif isinstance(ob, (list, tuple)):
        ob = cast(List[Any] | Tuple[Any, ...], ob)
        try:
            i = int(first)
        except ValueError:
            raise KeyError(f"cannot get_inside({components!r}) of {ob!r} in {context!r} in {original_ob!r}")
        if i < 0 or i >= len(ob):
            raise KeyError(f"index out of range")

        v = ob[i]
        return get_inside(original_ob, context + (i,), v, rest)

    else:
        raise KeyError(f"cannot get_inside({components!r}) of {ob!r} in {context!r} in {original_ob!r}")


@dataclass
class OurQueue(Source):
    topic_name: TopicNameV

    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]:
        return server.node_id

    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        oq = server.get_oq(self.topic_name)
        tr = oq.tr

        url_supposed = self.topic_name.as_relative_url()
        url_relative = get_relative_url(url_supposed, presented_as)

        reachability = TopicReachability(
            url=url_relative, answering=server.node_id, forwarders=[], benchmark=LinkBenchmark.identity()
        )

        tr = replace(tr, reachability=[reachability])
        return TopicsIndex(topics={TopicNameV.root(): tr})

    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        oq = server.get_oq(self.topic_name)
        return oq.tr.properties

    def get_inside_after(self, s: str) -> "Source":
        raise KeyError(f"get_inside_after({s!r}) not implemented for {self!r}")

    def get_inside(self, s: str, /) -> "Source":
        if s == ":meta":
            return MetaInfo(self)
        return Transformed(self, GetInside((s,)))

    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData":
        oq = server.get_oq(self.topic_name)
        if oq.serve is not None and request is not None:
            return await oq.serve(request)
        if not oq.stored:
            return NotAvailableYet(f"no data yet for {self.topic_name.as_dash_sep()}")
        return oq.last_data()

    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult":
        oq = server.get_oq(self.topic_name)

        otr = await oq.publish(rd, get_data=True)
        return otr

    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]:
        oq = server.get_oq(self.topic_name)

        otr = await oq.publish(rd, get_data=True)
        if isinstance(otr, TransformError):
            return otr
        else:
            # return oq.blob_manager.get_blob(otr.digest)
            return oq.last_data()

    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult":
        oq = server.get_oq(self.topic_name)
        tr = oq.tr.properties
        if not tr.patchable:
            msg = f"Cannot patch {self.topic_name.as_dash_sep()}"
            logger.error(msg)
            raise web.HTTPBadRequest(reason=msg)

        last_data = oq.last_data()
        ob = last_data.get_as_native_object()
        try:
            # noinspection PyTypeChecker,PydanticTypeChecker
            ob2 = patch.apply(ob)  # type: ignore
        except (jsonpatch.JsonPatchException, jsonpointer.JsonPointerException) as e:
            msg = f"Cannot apply patch {patch} to {ob}"
            logger.error(msg + f": {e}")
            raise web.HTTPBadRequest(reason=msg) from e

        if not isinstance(ob2, dict):
            msg = f"Patch {patch} applied to {ob} gives {ob2} which is not a dict"
            logger.error(msg)
            raise web.HTTPBadRequest(reason=msg)
        ob2 = cast(Dict[str, Any], ob2)
        rd = RawData.json_from_native_object(ob2)
        otr = await oq.publish(rd, get_data=True)
        return otr

    async def delete(self, presented_as: str, server: "DTPSServer") -> "Optional[TransformError]":
        oq = server.get_oq(self.topic_name)
        tr = oq.tr.properties
        if not tr.droppable:
            msg = f"Cannot patch {self.topic_name.as_dash_sep()}"
            logger.error(msg)
            return TransformError(401, msg)
        await server.remove_oq(self.topic_name)
        return None


@dataclass
class ForwardedQueue(Source):
    topic_name: TopicNameV

    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]:
        return server._forwarded[self.topic_name].origin_node

    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        raise NotImplementedError(f"get_meta_info() for {self}")  # XXX:

    def get_inside_after(self, s: str) -> "Source":
        raise KeyError(f"get_inside_after({s!r}) not implemented for {self!r}")  # XXX:

    def get_inside(self, s: str, /) -> "Source":
        raise KeyError(f"get_inside({s!r}) not implemented for {self!r}")  # XXX:

    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        fd = server._forwarded[self.topic_name]
        return fd.properties

    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData":
        url_data = server._forwarded[self.topic_name].forward_url_data
        from dtps_http import my_raise_for_status

        async with server._client() as dtpsclient:
            async with dtpsclient.my_session(url_data) as (session2, use_url2):
                async with session2.get(use_url2) as resp_data:
                    await my_raise_for_status(resp_data, url_data)
                    content = await resp_data.read()
                    content_type = ContentType(resp_data.content_type)
                    data = RawData(content_type=content_type, content=content)
                    return data

    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult":
        url_post = server._forwarded[self.topic_name].forward_url_data
        async with server._client() as dtpsclient:
            session2: aiohttp.ClientSession
            data = cbor2.dumps(patch.patch)
            content_type = CONTENT_TYPE_PATCH_CBOR
            async with dtpsclient.my_session(url_post) as (session2, use_url2):
                headers = {"content-type": content_type}
                async with session2.patch(use_url2, data=data, headers=headers) as resp_data:
                    if not resp_data.ok:
                        return TransformError(resp_data.status, resp_data.reason or "")  # TODO: read error
                    else:
                        return await load_datasaved_resp(
                            server, url_post, dtpsclient, resp_data, presented_as
                        )

    async def delete(self, presented_as: str, server: "DTPSServer") -> "Optional[TransformError]":
        url_post = server._forwarded[self.topic_name].forward_url_data

        async with server._client() as dtpsclient:
            session2: aiohttp.ClientSession
            async with dtpsclient.my_session(url_post) as (session2, use_url2):
                async with session2.delete(use_url2) as resp_data:
                    if not resp_data.ok:
                        body = await resp_data.read()
                        return TransformError(resp_data.status, body)

    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult":
        url_post = server._forwarded[self.topic_name].forward_url_data
        async with server._client() as dtpsclient:
            session2: aiohttp.ClientSession
            async with dtpsclient.my_session(url_post) as (session2, use_url2):
                headers = {"content-type": rd.content_type}
                async with session2.post(use_url2, data=rd.content, headers=headers) as resp_data:
                    if not resp_data.ok:
                        return TransformError(resp_data.status, resp_data.reason or "")  # TODO: read error
                    else:
                        return await load_datasaved_resp(
                            server, url_post, dtpsclient, resp_data, presented_as
                        )

    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]:
        url_post = server._forwarded[self.topic_name].forward_url_data
        async with server._client() as dtpsclient:
            session2: aiohttp.ClientSession
            async with dtpsclient.my_session(url_post) as (session2, use_url2):
                headers = {"content-type": rd.content_type}
                async with session2.post(use_url2, data=rd.content, headers=headers) as resp_data:
                    if not resp_data.ok:
                        return TransformError(resp_data.status, resp_data.reason or "")  # TODO: read error
                    else:
                        dr = await load_datasaved_resp(server, url_post, dtpsclient, resp_data, presented_as)

                        return await dtpsclient.get(
                            parse_url_unescape(dr.availability[0].url), accept=dr.content_type
                        )


async def load_datasaved_resp(
    server: "DTPSServer", base_url: URL, client: "DTPSClient", resp_data: ClientResponse, presented_as: str
) -> DataReady:
    content = await resp_data.read()
    content_type = ContentType(resp_data.content_type)
    data = RawData(content_type=content_type, content=content)

    s: Any = data.get_as_native_object()
    ds = pydantic_parse(DataSaved, s)
    locations = resp_data.headers.getall("location")

    dr = DataReady.from_data_saved(ds)
    for location in locations:
        url = join(base_url, location)

        rd = await client.get(url, accept=ds.content_type)
        availability_s = DEFAULT_DATA_AVAILABILITY_TIMEOUT
        available_until = time.time() + availability_s

        the_url = server.blob_manager.get_use_once_link_store(
            dr.digest, rd.content, dr.content_type, availability_s
        )

        dr.availability.append(ResourceAvailability(url=the_url, available_until=available_until))
        break
    else:
        # TODO: how to deal with failure?
        raise ValueError(f"no location in {locations}")

    return dr


@dataclass
class SourceComposition(Source):
    topic_name: TopicNameV
    sources: Dict[TopicNameV, Source]
    unique_id: SourceID
    origin_node: NodeID

    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]:
        return self.origin_node

    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        topics: Dict[TopicNameV, TopicRef] = {}
        for prefix, source in self.sources.items():
            x = await source.get_meta_info(presented_as, server)

            for a, b in x.topics.items():
                topics[prefix + a] = b

        supposed = self.topic_name.as_relative_url()
        url_relative = get_relative_url(supposed, presented_as)
        reachability = TopicReachability(
            url=url_relative, answering=server.node_id, forwarders=[], benchmark=LinkBenchmark.identity()
        )

        content_info = ContentInfo.simple(CONTENT_TYPE_DTPS_INDEX_CBOR)
        topics[TopicNameV.root()] = TopicRef(
            unique_id=self.unique_id,
            origin_node=self.origin_node,
            app_data={},
            reachability=[reachability],
            created=0,
            properties=self.get_properties(server),
            content_info=content_info,
            bounds=Bounds.unbounded(),  # TODO: warn?
        )
        return TopicsIndex(topics=topics)

    async def delete(self, presented_as: str, server: "DTPSServer") -> "None":
        raise NotImplementedError(f"delete() for {self}")

    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        immutable = True
        streamable = False
        pushable = False
        readable = True

        for _k, v in self.sources.items():
            p = v.get_properties(server)

            immutable = immutable and p.immutable
            streamable = streamable or p.streamable
            readable = readable and p.readable

        return TopicProperties(
            streamable=streamable,
            pushable=pushable,
            readable=readable,
            immutable=immutable,
            has_history=False,
            patchable=False,
            droppable=False,
        )

    def get_inside_after(self, s: str) -> "Source":
        raise KeyError(f"get_inside_after({s!r}) not implemented for {self!r}")

    def get_inside(self, s: str, /) -> "Source":
        raise KeyError(f"get_inside({s!r}) not implemented for {self!r}")

    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData":
        data = await self.get_meta_info(presented_as, server)
        as_cbor = cbor2.dumps(asdict(data.to_wire()))
        return RawData(content_type=CONTENT_TYPE_DTPS_INDEX_CBOR, content=as_cbor)

    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult":
        return TransformError(400, "Cannot patch SourceComposition")  # TODO: this can be done in principle

    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult":
        return TransformError(400, "Cannot post to SourceComposition")

    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]:
        return TransformError(400, "Cannot call SourceComposition")


@dataclass
class Transformed(Source):
    source: Source
    transform: Transform

    async def delete(self, presented_as: str, server: "DTPSServer") -> "Optional[TransformError]":
        raise NotImplementedError(f"delete() for {self}")

    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]:
        return await self.source.get_source_node_id(server)

    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        raise NotImplementedError(f"OurQueue.get_meta_info() for {self}")  # XXX

    def get_inside_after(self, s: str) -> "Source":
        raise KeyError(f"get_inside_after({s!r}) not implemented for {self!r}")  # XXX

    def get_inside(self, s: str, /) -> "Source":
        return Transformed(self.source, self.transform.get_transform_inside(s))

    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData":
        data = await self.source.get_resolved_data(presented_as, server, request)
        return self.transform.transform(data)

    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        return self.source.get_properties(server)

    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult":
        # logger.debug(f"Transformed.patch() {self} {patch}")
        if isinstance(self.transform, GetInside):
            patch2 = add_prefix_to_patch(self.transform.components, patch)
            return await self.source.patch(presented_as, server, patch2)
        else:
            raise NotImplementedError(f"patch() for {self}")

    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult":
        if isinstance(self.transform, GetInside):
            native = rd.get_as_native_object()
            path = "".join("/" + o for o in self.transform.components)
            ops = [{"op": "replace", "path": path, "value": native}]
            patch = JsonPatch(ops)  # type: ignore

            return await self.source.patch(presented_as, server, patch)
        else:
            raise NotImplementedError(f"patch() for {self}")

    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]:
        return TransformError(400, "Cannot call Transformed")


def add_prefix_to_patch(prefix: Tuple[str, ...], patch: JsonPatch) -> JsonPatch:
    patch2 = copy.deepcopy(patch.patch)
    pref = "".join("/" + o for o in prefix)
    for op in patch2:
        if "path" in op:
            op["path"] = pref + op["path"]

    return JsonPatch(patch2)


@dataclass
class MetaInfo(Source):
    source: Source

    async def delete(self, presented_as: str, server: "DTPSServer") -> "Optional[TransformError]":
        return TransformError(400, "Cannot delete MetaInfo")

    async def get_source_node_id(self, server: "DTPSServer") -> Optional[NodeID]:
        return await self.source.get_source_node_id(server)

    async def get_meta_info(self, presented_as: str, server: "DTPSServer") -> "TopicsIndex":
        raise KeyError(f"OurQueue.get_meta_info() for a meta info")

    def get_properties(self, server: "DTPSServer") -> TopicProperties:
        return TopicProperties.readonly()

    def get_inside_after(self, s: str) -> "Source":
        raise KeyError(f"get_inside_after({s!r}) not implemented for {self!r}")

    def get_inside(self, s: str, /) -> "Source":
        raise KeyError(f"get_inside({s!r}) not implemented for {self!r}")

    async def get_resolved_data(
        self, presented_as: str, server: "DTPSServer", request: Optional[HTTPRequest]
    ) -> "ResolvedData":
        res = await self.source.get_meta_info(presented_as, server)
        w = res.to_wire()
        rd = RawData.cbor_from_native_object(asdict(w))
        return rd

    async def patch(self, presented_as: str, server: "DTPSServer", patch: JsonPatch) -> "PostResult":
        return TransformError(400, "Cannot PATCH MetaInfo")

    async def publish(self, presented_as: str, server: "DTPSServer", rd: RawData) -> "PostResult":
        return TransformError(400, "Cannot POST MetaInfo")

    async def call(
        self, presented_as: str, server: "DTPSServer", rd: RawData
    ) -> Union[RawData, TransformError]:
        return TransformError(400, "Cannot call MetaInfo")


TypeOfSource = Union[OurQueue, ForwardedQueue, SourceComposition, Transformed]
