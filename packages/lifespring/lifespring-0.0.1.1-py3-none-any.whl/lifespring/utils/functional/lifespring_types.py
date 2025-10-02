from ..fundamental import *


__all__ = [
    "BucketData",
    "LifeSpringState",
    "LifeSpringEvent",
]


@dataclass
class BucketData:
    value: float
    value_unit: str
    bucket_type: str
    bucket_status: str


@dataclass
class LifeSpringState:
    bucket_to_data: Dict[str, BucketData]


@dataclass
class LifeSpringEvent:
    event_type: str
    note: str
    extra_info: str