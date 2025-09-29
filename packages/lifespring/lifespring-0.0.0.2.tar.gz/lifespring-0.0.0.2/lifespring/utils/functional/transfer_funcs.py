from ..fundamental import *
from .lifespring_types import *


__all__ = [
    "create_bucket_transfer_func",
    "revalue_bucket_transfer_func",
    "archive_bucket_transfer_func",
    "produce_value_transfer_func",
    "consume_value_transfer_func",
    "transfer_value_transfer_func",
]


def create_bucket_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    bucket = extra_info_dict["bucket"]
    bucket_type = extra_info_dict["bucket_type"]
    value_unit = extra_info_dict["value_unit"]

    bucket_to_data[bucket] = BucketData(
        value = 0.0,
        value_unit = value_unit,
        bucket_type = bucket_type,
        bucket_status = "alive",
    )
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )


def revalue_bucket_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    bucket = extra_info_dict["bucket"]
    value = extra_info_dict["value"]
    value_unit = bucket_to_data[bucket].value_unit
    bucket_type = bucket_to_data[bucket].bucket_type
    bucket_status = bucket_to_data[bucket].bucket_status
    
    bucket_to_data[bucket] = BucketData(
        value = value,
        value_unit = value_unit,
        bucket_type = bucket_type,
        bucket_status = bucket_status,
    )
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )


def archive_bucket_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    bucket = extra_info_dict["bucket"]
    value = bucket_to_data[bucket].value
    value_unit = bucket_to_data[bucket].value_unit
    bucket_type = bucket_to_data[bucket].bucket_type
    
    bucket_to_data[bucket] = BucketData(
        value = value,
        value_unit = value_unit,
        bucket_type = bucket_type,
        bucket_status = "archived",
    )
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )


def produce_value_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    bucket = extra_info_dict["bucket"]
    value = bucket_to_data[bucket].value + extra_info_dict["value"]
    value_unit = bucket_to_data[bucket].value_unit
    bucket_type = bucket_to_data[bucket].bucket_type
    bucket_status = bucket_to_data[bucket].bucket_status
    
    bucket_to_data[bucket] = BucketData(
        value = value,
        value_unit = value_unit,
        bucket_type = bucket_type,
        bucket_status = bucket_status,
    )
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )


def consume_value_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    bucket = extra_info_dict["bucket"]
    value = bucket_to_data[bucket].value - extra_info_dict["value"]
    value_unit = bucket_to_data[bucket].value_unit
    bucket_type = bucket_to_data[bucket].bucket_type
    bucket_status = bucket_to_data[bucket].bucket_status
    
    bucket_to_data[bucket] = BucketData(
        value = value,
        value_unit = value_unit,
        bucket_type = bucket_type,
        bucket_status = bucket_status,
    )
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )


def transfer_value_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:
    
    bucket_to_data = deepcopy(state.bucket_to_data)
    extra_info_dict = deserialize_json(event.extra_info)
    
    source_bucket = extra_info_dict["source_bucket"]
    destination_bucket = extra_info_dict["destination_bucket"]
    value = extra_info_dict["value"]
    exchange_rate = extra_info_dict["exchange_rate"]
    
    source_bucket_data = BucketData(
        value = bucket_to_data[source_bucket].value - value,
        value_unit = bucket_to_data[source_bucket].value_unit,
        bucket_type = bucket_to_data[source_bucket].bucket_type,
        bucket_status = bucket_to_data[source_bucket].bucket_status
    )
    destination_bucket_data = BucketData(
        value = bucket_to_data[destination_bucket].value + value * exchange_rate,
        value_unit = bucket_to_data[destination_bucket].value_unit,
        bucket_type = bucket_to_data[destination_bucket].bucket_type,
        bucket_status = bucket_to_data[destination_bucket].bucket_status
    )
    
    bucket_to_data[source_bucket] = source_bucket_data
    bucket_to_data[destination_bucket] = destination_bucket_data
    
    return LifeSpringState(
        bucket_to_data = bucket_to_data,
    )