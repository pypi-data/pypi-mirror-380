import hashlib
import itertools
import json
from dataclasses import dataclass
from dataclasses import asdict, is_dataclass
from pydantic import BaseModel
from typing import Any, cast, Dict, List, Literal, NewType, Optional, Sequence, Union

import cbor2
from multidict import CIMultiDict

from .constants import DEFAULT_MAX_HISTORY, HEADER_LINK_BENCHMARK, MIME_CBOR, MIME_JSON, MIME_TEXT, MIME_YAML
from .types import ContentType, NodeID, SourceID, TopicNameS, TopicNameV, URLString
from .urls import join, parse_url_unescape, URL, url_to_string, URLIndexer
from .utils import pydantic_parse

__all__ = [
    "Bounds",
    "ChannelInfo",
    "ChannelInfoDesc",
    "ChannelMsgs",
    "Chunk",
    "Clocks",
    "ConnectionEstablished",
    "ConnectionJob",
    "ContentInfo",
    "DataDesc",
    "DataReady",
    "DataSaved",
    "Digest",
    "ErrorMsg",
    "FinishedMsg",
    "ForwardingStep",
    "History",
    "InsertNotification",
    "LinkBenchmark",
    "ListenURLEvents",
    "ListenerInfo",
    "Metadata",
    "MinMax",
    "ProxyJob",
    "PushResult",
    "RawData",
    "Registration",
    "ResourceAvailability",
    "SilenceMsg",
    "TopicProperties",
    "TopicReachability",
    "TopicRef",
    "TopicRefAdd",
    "TopicsIndex",
    "TopicsIndexWire",
    "TransportData",
    "WarningMsg",
    "get_digest",
    "is_image",
    "is_structure",
]


@dataclass
class LinkBenchmark:
    complexity: int  # 0 for local, 1 for using named unix socket, +2 for each network hop
    bandwidth: int  # B/s
    latency_ns: int  # seconds
    reliability_percent: int  # 0..100
    hops: int

    @classmethod
    def identity(cls) -> "LinkBenchmark":
        return LinkBenchmark(
            complexity=0, bandwidth=1_000_000_000, latency_ns=0, reliability_percent=100, hops=1
        )

    def __or__(self, other: "LinkBenchmark") -> "LinkBenchmark":
        complexity = self.complexity + other.complexity
        bandwidth = min(self.bandwidth, other.bandwidth)
        latency = self.latency_ns + other.latency_ns
        reliability = int(self.reliability_percent * other.reliability_percent / (100 * 100))
        hops = self.hops + other.hops
        return LinkBenchmark(
            complexity=complexity,
            bandwidth=bandwidth,
            latency_ns=latency,
            reliability_percent=reliability,
            hops=hops,
        )

    def fill_headers(self, headers: CIMultiDict[str]) -> None:
        # RTT = 2 * latency - in mseconds
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/RTT
        rtt_ns = self.latency_ns * 2
        rtt_ms = rtt_ns / 1_000_000.0
        headers["RTT"] = f"{rtt_ms:.2f}"
        # Downlink = bandwidth in Mbits/s
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Downlink
        mbs = self.bandwidth / (1024.0 * 1024.0)
        headers["Downlink"] = f"{mbs:.3f}"
        # everything as a json object
        headers[HEADER_LINK_BENCHMARK] = json.dumps(asdict(self))  # ok


@dataclass
class ForwardingStep:
    forwarding_node: NodeID
    forwarding_node_connects_to: URLString

    performance: LinkBenchmark


@dataclass
class TopicReachabilityWire:
    url: URLString
    answering: NodeID

    # mostly for debugging
    forwarders: List[ForwardingStep]

    benchmark: LinkBenchmark

    def to_internal(self, urlbase: URL) -> "TopicReachability":
        url = join(urlbase, self.url)
        return TopicReachability(
            url=url_to_string(url),
            answering=self.answering,
            forwarders=self.forwarders,
            benchmark=self.benchmark,
        )


@dataclass
class TopicReachability:
    url: URLString
    answering: NodeID

    # mostly for debugging
    forwarders: List[ForwardingStep]

    benchmark: LinkBenchmark

    def __post_init__(self) -> None:
        # s = url_to_string(self.url)
        if "///" in self.url:
            msg = f"Invalid URL: {self.url!r}"
            raise ValueError(msg)

    def to_wire(self) -> "TopicReachabilityWire":
        return TopicReachabilityWire(
            url=self.url,  # should I really do this?
            answering=self.answering,
            forwarders=self.forwarders,
            benchmark=self.benchmark,
        )


@dataclass
class TopicProperties:
    streamable: bool
    pushable: bool
    readable: bool
    immutable: bool
    has_history: bool

    patchable: bool
    droppable: bool

    @classmethod
    def streamable_readonly(cls) -> "TopicProperties":
        return TopicProperties(
            streamable=True,
            pushable=False,
            readable=True,
            immutable=False,
            has_history=True,
            patchable=False,
            droppable=False,
        )

    @classmethod
    def default(cls) -> "TopicProperties":
        return TopicProperties.rw_pushable()

    @classmethod
    def readonly(cls) -> "TopicProperties":
        return TopicProperties(
            streamable=False,
            pushable=False,
            readable=True,
            immutable=False,
            has_history=False,
            patchable=False,
            droppable=False,
        )

    @classmethod
    def rw_pushable(cls) -> "TopicProperties":
        return TopicProperties(
            streamable=True,
            pushable=True,
            readable=True,
            immutable=False,
            has_history=True,
            patchable=True,
            droppable=True,
        )

    @classmethod
    def patchable_only(cls) -> "TopicProperties":
        return TopicProperties(
            streamable=True,
            pushable=False,
            readable=True,
            immutable=False,
            has_history=True,
            patchable=True,
            droppable=False,
        )


Digest = NewType("Digest", str)

import xxhash


def get_digest_xxh128(s: bytes) -> Digest:
    x = xxhash.xxh128()
    x.update(s)
    d = x.hexdigest()
    return cast(Digest, f"xxh128:{d}")


def get_digest_xxh64(s: bytes) -> Digest:
    x = xxhash.xxh64()
    x.update(s)
    d = x.hexdigest()
    return cast(Digest, f"xxh64:{d}")


def get_digest_xxh32(s: bytes) -> Digest:
    x = xxhash.xxh32()
    x.update(s)
    d = x.hexdigest()
    return cast(Digest, f"xxh32:{d}")


def get_digest_sha256(s: bytes) -> Digest:
    d = hashlib.sha256(s).hexdigest()
    return cast(Digest, f"sha256:{d}")


def get_digest_sha1(s: bytes) -> Digest:
    d = hashlib.sha1(s).hexdigest()
    return cast(Digest, f"sha1:{d}")


def get_digest_blake2b(s: bytes) -> Digest:
    d = hashlib.blake2b(s).hexdigest()
    return cast(Digest, f"blake2b:{d}")


def get_digest_blake2s(s: bytes) -> Digest:
    d = hashlib.blake2b(s).hexdigest()
    return cast(Digest, f"blake2s:{d}")


def get_digest_md5(s: bytes) -> Digest:
    d = hashlib.md5(s).hexdigest()
    return cast(Digest, f"md5:{d}")


def get_digest(s: bytes) -> Digest:
    return get_digest_xxh128(s)


@dataclass
class RawData:
    content: bytes
    content_type: ContentType

    def short_description(self) -> str:
        return f"RawData({self.content_type}; {len(self.content)} bytes)"

    @classmethod
    def simple_string(cls, s: str) -> "RawData":
        return cls(content=s.encode("utf-8"), content_type=MIME_TEXT)

    @classmethod
    def cbor_from_native_object(cls, ob: object) -> "RawData":
        """
        One-pass CBOR serialiser that calls `model_dump()` or `asdict()` **exactly once**.
        """
        if isinstance(ob, BaseModel):
            payload = ob.model_dump(mode="python", round_trip=False)
            # at this point *all* nested models are already plain dict/list/str/int
            cbor_bytes = cbor2.dumps(payload)
            return cls(content=cbor_bytes, content_type=MIME_CBOR)

        if is_dataclass(ob):
            payload = asdict(ob)          # one dataclass → plain containers
            cbor_bytes = cbor2.dumps(payload)
            return cls(content=cbor_bytes, content_type=MIME_CBOR)

        # fallback – only hit for non-model, non-dataclass roots
        def _default(o):
            if isinstance(o, BaseModel):
                return o.model_dump(mode="python", round_trip=False)
            if is_dataclass(o):
                return asdict(o)
            raise TypeError(f"{type(o).__name__} not CBOR-serialisable")

        cbor_bytes = cbor2.dumps(ob, default=_default)
        return cls(content=cbor_bytes, content_type=MIME_CBOR)

    @classmethod
    def json_from_native_object(cls, ob: object) -> "RawData":
        return cls(content=json.dumps(ob).encode(), content_type=MIME_JSON)  # ok

    @classmethod
    def yaml_from_native_object(cls, ob: object) -> "RawData":
        import yaml

        data = yaml.safe_dump(ob)

        return cls(content=data.encode(), content_type=MIME_YAML)

    def digest(self) -> Digest:
        return get_digest(self.content)

    def get_as_yaml(self) -> str:
        ob = self.get_as_native_object()
        import yaml

        return yaml.safe_dump(ob)

    def get_as_native_object(self) -> object:
        if is_plain_text(self.content_type):
            return self.content.decode("utf-8")

        if not is_structure(self.content_type):
            msg = (
                f"Cannot convert non-structure content to native object (content_type="
                f"{self.content_type!r})\n"
                f"data = {self.content!r}"
            )
            raise ValueError(msg)

        if is_yaml(self.content_type):
            import yaml

            return yaml.safe_load(self.content)
        if is_json(self.content_type):
            import json

            return json.loads(self.content)
        if is_cbor(self.content_type):
            import cbor2

            return cbor2.loads(self.content)
        raise ValueError(f"cannot convert {self.content_type!r} to native object")

    def as_cbor(self) -> "RawData":
        no = self.get_as_native_object()
        return RawData.cbor_from_native_object(no)

    def as_json(self) -> "RawData":
        no = self.get_as_native_object()
        return RawData.json_from_native_object(no)

    def as_yaml(self) -> "RawData":
        no = self.get_as_native_object()

        return RawData.yaml_from_native_object(no)

    def get_as(self, content_type: str) -> "RawData":
        content_types_split: List[List[str]] = [ct.split(",") for ct in content_type.split(";")]
        content_types: List[str] = list(itertools.chain.from_iterable(content_types_split))
        if MIME_JSON in content_types:
            return self.as_json()
        if MIME_CBOR in content_types:
            return self.as_cbor()
        if MIME_YAML in content_types:
            return self.as_yaml()
        # MUST leave most general case to the end
        if "*/*" in content_types:
            return self
        raise ValueError(f"Cannot convert to {content_type!r}")


def is_structure(content_type: str) -> bool:
    return is_yaml(content_type) or is_json(content_type) or is_cbor(content_type)


def is_image(content_type: str) -> bool:
    return "image" in content_type


def is_yaml(content_type: str) -> bool:
    return "yaml" in content_type


def is_plain_text(content_type: str) -> bool:
    return "text/plain" in content_type


def is_json(content_type: str) -> bool:
    return "json" in content_type


def is_cbor(content_type: str) -> bool:
    return "cbor" in content_type


@dataclass
class DataDesc:
    content_type: ContentType
    jschema: Optional[object]
    examples: List[RawData]


@dataclass
class MinMax:
    min: int
    max: int


@dataclass
class Clocks:
    logical: Dict[str, MinMax]
    wall: Dict[str, MinMax]

    @classmethod
    def empty(cls) -> "Clocks":
        return Clocks(logical={}, wall={})


@dataclass(frozen=True)
class Bounds:
    min_size: int
    min_time_ms: int
    min_bytes: int

    max_size: Optional[int]
    max_time_ms: Optional[int]
    max_bytes: Optional[int]

    @classmethod
    def unbounded(cls) -> "Bounds":
        return cls(min_size=0, min_time_ms=0, max_size=None, max_time_ms=None, min_bytes=0, max_bytes=None)

    @classmethod
    def max_length(cls, n: int) -> "Bounds":
        return cls(min_size=0, min_time_ms=0, max_size=n, max_time_ms=None, min_bytes=0, max_bytes=None)

    @classmethod
    def default(cls) -> "Bounds":
        return cls.max_length(DEFAULT_MAX_HISTORY)


@dataclass
class DataSaved:
    origin_node: NodeID
    unique_id: SourceID
    index: int
    time_inserted: int
    digest: Digest
    content_type: ContentType
    content_length: int
    clocks: "Clocks"


@dataclass
class ResourceAvailability:
    url: URLString
    available_until: float  # timestamp


@dataclass
class DataReady:
    origin_node: NodeID
    unique_id: SourceID
    index: int
    time_inserted: int
    digest: Digest
    content_type: ContentType
    content_length: int
    clocks: Clocks

    availability: List[ResourceAvailability]
    chunks_arriving: int

    @classmethod
    def from_json_string(cls, s: str) -> "DataReady":
        struct = json.loads(s)
        return cls(**struct)

    @classmethod
    def from_cbor(cls, s: bytes) -> "DataReady":
        struct = cbor2.loads(s)
        if not isinstance(struct, dict):
            raise ValueError(f"Expected a dictionary here: {s!r}\n{struct}")
        return cls(**struct)

    def as_data_saved(self) -> DataSaved:
        return DataSaved(
            origin_node=self.origin_node,
            unique_id=self.unique_id,
            index=self.index,
            time_inserted=self.time_inserted,
            digest=self.digest,
            content_type=self.content_type,
            content_length=self.content_length,
            clocks=self.clocks,
        )

    @classmethod
    def from_data_saved(cls, ds: DataSaved) -> "DataReady":
        return DataReady(
            origin_node=ds.origin_node,
            unique_id=ds.unique_id,
            index=ds.index,
            time_inserted=ds.time_inserted,
            digest=ds.digest,
            content_type=ds.content_type,
            content_length=ds.content_length,
            clocks=ds.clocks,
            availability=[],
            chunks_arriving=0,
        )


@dataclass
class ContentInfo:
    accept: Dict[str, DataDesc]
    storage: DataDesc
    produces_content_type: List[ContentType]

    @classmethod
    def simple(cls, ct: ContentType, jschema: Optional[object] = None, examples: Sequence[RawData] = ()):
        dd = DataDesc(content_type=ct, jschema=jschema, examples=list(examples))

        return ContentInfo(
            accept={"": dd},
            storage=dd,
            produces_content_type=[ct],
        )


@dataclass
class TopicRefWire:
    unique_id: SourceID  # unique id for the stream
    origin_node: NodeID  # unique id of the node that created the stream
    app_data: Dict[str, bytes]
    reachability: List[TopicReachabilityWire]
    created: int
    properties: TopicProperties
    content_info: ContentInfo
    bounds: Bounds

    def to_internal(self, where_available: List[URL], /) -> "TopicRef":
        reachability: list[TopicReachability] = []
        for r in self.reachability:
            for w in where_available:
                reachability.append(r.to_internal(w))
        return TopicRef(
            unique_id=self.unique_id,
            origin_node=self.origin_node,
            app_data=self.app_data,
            reachability=reachability,
            created=self.created,
            properties=self.properties,
            content_info=self.content_info,
            bounds=self.bounds,
        )


@dataclass
class TopicRef:
    unique_id: SourceID  # unique id for the stream
    origin_node: NodeID  # unique id of the node that created the stream
    app_data: Dict[str, bytes]
    reachability: List[TopicReachability]
    created: int
    properties: TopicProperties
    content_info: ContentInfo
    bounds: Bounds

    def to_wire(self) -> "TopicRefWire":
        reachability: list[TopicReachabilityWire] = []
        for r in self.reachability:
            reachability.append(r.to_wire())
        return TopicRefWire(
            unique_id=self.unique_id,
            origin_node=self.origin_node,
            app_data=self.app_data,
            reachability=reachability,
            created=self.created,
            properties=self.properties,
            content_info=self.content_info,
            bounds=self.bounds,
        )


@dataclass
class TopicRefAdd:
    app_data: Dict[str, bytes]
    properties: TopicProperties
    content_info: ContentInfo
    bounds: Bounds

    @classmethod
    def from_json(cls, s: Any) -> "TopicRefAdd":
        return pydantic_parse(cls, s)


@dataclass
class TopicsIndex:
    topics: Dict[TopicNameV, TopicRef]

    def __post_init__(self) -> None:
        for k, v in self.topics.items():
            if not v.reachability:
                msg = f"Topic {k.as_dash_sep()!r} has no reachability"
                raise AssertionError(msg)

    def to_wire(self) -> "TopicsIndexWire":
        topics: Dict[TopicNameS, TopicRefWire] = {}
        for k, v in self.topics.items():
            topics[k.as_dash_sep()] = v.to_wire()

        return TopicsIndexWire(topics=topics)


@dataclass
class TopicsIndexWire:
    topics: Dict[TopicNameS, TopicRefWire]

    @classmethod
    def from_json(cls, s: Any) -> "TopicsIndexWire":
        return pydantic_parse(cls, s)

    def to_internal(self, where_this_available: List[URL]) -> "TopicsIndex":
        topics: Dict[TopicNameV, TopicRef] = {}

        for k, tr0 in self.topics.items():
            topic = TopicNameV.from_dash_sep(k)

            topics[topic] = tr0.to_internal(where_this_available)

        return TopicsIndex(topics=topics)


@dataclass
class ChannelInfoDesc:
    sequence: int
    time_inserted: int


@dataclass
class ChannelInfo:
    queue_created: int
    num_total: int
    newest: Optional[ChannelInfoDesc]
    oldest: Optional[ChannelInfoDesc]

    @classmethod
    def from_cbor(cls, s: bytes) -> "ChannelInfo":
        struct = cbor2.loads(s)
        return pydantic_parse(cls, struct)


@dataclass
class Chunk:
    digest: str
    i: int
    n: int
    index: int
    data: bytes

    @classmethod
    def from_cbor(cls, s: bytes) -> "Chunk":
        struct = cbor2.loads(s)
        return pydantic_parse(cls, struct)


@dataclass
class InsertNotification:
    data_saved: DataSaved
    raw_data: RawData


History = Dict[int, DataReady]


@dataclass
class ConnectionEstablished:
    comment: str


@dataclass
class WarningMsg:
    comment: str


@dataclass
class ErrorMsg:
    comment: str


@dataclass
class FinishedMsg:
    comment: str


@dataclass
class SilenceMsg:
    dt: float
    comment: str


@dataclass
class TransportData:
    canonical_url: str
    alternative_urls: List[str]


@dataclass
class Metadata:
    sequence: int
    generated_ns: int


@dataclass
class Registration:
    switchboard_url: "URLIndexer"
    topic: TopicNameV
    namespace: TopicNameV


ChannelMsgs = Union[ChannelInfo, DataReady, Chunk, FinishedMsg, ErrorMsg, WarningMsg, SilenceMsg]
ListenURLEvents = Union[
    ConnectionEstablished,
    InsertNotification,
    WarningMsg,
    ErrorMsg,
    FinishedMsg,
    SilenceMsg,
]


@dataclass
class ProxyJob:
    node_id: Optional[NodeID]
    urls: List[URLString]
    mask_origin: bool

    @classmethod
    def from_json(cls, s: Any) -> "ProxyJob":
        return pydantic_parse(cls, s)

    def __post_init__(self) -> None:
        if not self.urls:
            msg = "Empty urls"
            raise ValueError(msg)
        for u in self.urls:
            parse_url_unescape(u)


@dataclass(frozen=True)
class PushResult:
    result: bool
    message: str

    @classmethod
    def from_json(cls, s: Any) -> "PushResult":
        return pydantic_parse(cls, s)


MsgWebsocketPushServerToClient = PushResult
MsgWebsocketPushClientToServer = RawData

ServiceMode = Literal["BestEffort", "AllMessages", "AllMessagesSinceStart"]


@dataclass
class ConnectionJob:
    source: TopicNameV
    target: TopicNameV
    service_mode: ServiceMode

    def to_wire(self):
        return ConnectionJobWire(
            source=self.source.as_dash_sep(), target=self.target.as_dash_sep(), service_mode=self.service_mode
        )


@dataclass
class ConnectionJobWire:
    source: TopicNameS
    target: TopicNameS
    service_mode: ServiceMode


@dataclass
class ListenerInfo:
    num_listeners: int
    max_frequency: Optional[float]
