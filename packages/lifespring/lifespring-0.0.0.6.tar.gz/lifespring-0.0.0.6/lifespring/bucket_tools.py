from .utils import *
from .lifespring import lifespring


__all__ = [
    "create_bucket",
    "revalue_bucket",
    "archive_bucket",
    "produce_value",
    "consume_value",
    "transfer_value",
    "list_buckets",
]


def create_bucket(
    bucket: str,
    bucket_type: str,
    value_unit: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "create_bucket",
            note = note,
            extra_info = serialize_json({
                "bucket": bucket,
                "bucket_type": bucket_type,
                "value_unit": value_unit,
            })
        )
    )


def revalue_bucket(
    bucket: str,
    value: float,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "revalue_bucket",
            note = note,
            extra_info = serialize_json({
                "bucket": bucket,
                "value": value,
            })
        )
    )


def archive_bucket(
    bucket: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "archive_bucket",
            note = note,
            extra_info = serialize_json({
                "bucket": bucket,
            })
        )
    )


def produce_value(
    value: float,
    bucket: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "produce_value",
            note = note,
            extra_info = serialize_json({
                "bucket": bucket,
                "value": value,
            })
        )
    )


def consume_value(
    value: float,
    bucket: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "consume_value",
            note = note,
            extra_info = serialize_json({
                "bucket": bucket,
                "value": value,
            })
        )
    )


def transfer_value(
    value: float,
    source_bucket: str,
    destination_bucket: str,
    exchange_rate: float = 1.0,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "transfer_value",
            note = note,
            extra_info = serialize_json({
                "source_bucket": source_bucket,
                "destination_bucket": destination_bucket,
                "value": value,
                "exchange_rate": exchange_rate,
            })
        )
    )
    
    
def list_buckets(
):
    
    lifespring.list_buckets()