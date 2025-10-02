from .utils import *
from .lifespring import lifespring


__all__ = [
    "set_database_path",
    "create_bucket",
    "list_buckets",
    "revalue_bucket",
    "archive_bucket",
    "dearchive_bucket",
    "produce_value",
    "consume_value",
    "transfer_value",
]


def set_database_path(
    database_path: str,
):
    
    lifespring.set_database_path(database_path)


def create_bucket(
    bucket: str,
    bucket_type: str,
    value_unit: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "create_bucket",
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
                "bucket_type": str(bucket_type),
                "value_unit": str(value_unit),
            })
        )
    )


def list_buckets(
):
    
    lifespring.list_buckets()


def revalue_bucket(
    bucket: str,
    value: float,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "revalue_bucket",
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
                "value": float(value),
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
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
            })
        )
    )
    
    
def dearchive_bucket(
    bucket: str,
    note: str = "",
):
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "dearchive_bucket",
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
            })
        )
    )


def produce_value(
    value: float,
    bucket: str,
    tags: List[str] = [],
    note: str = "",
):
    
    safe_tags = [str(tag) for tag in tags]
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "produce_value",
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
                "value": float(value),
                "tags": safe_tags,
            })
        )
    )


def consume_value(
    value: float,
    bucket: str,
    tags: List[str] = [],
    note: str = "",
):
    
    safe_tags = [str(tag) for tag in tags]
    
    lifespring.update(
        event = LifeSpringEvent(
            event_type = "consume_value",
            note = str(note),
            extra_info = serialize_json({
                "bucket": str(bucket),
                "value": float(value),
                "tags": safe_tags,
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
            note = str(note),
            extra_info = serialize_json({
                "source_bucket": str(source_bucket),
                "destination_bucket": str(destination_bucket),
                "value": float(value),
                "exchange_rate": float(exchange_rate),
            })
        )
    )
