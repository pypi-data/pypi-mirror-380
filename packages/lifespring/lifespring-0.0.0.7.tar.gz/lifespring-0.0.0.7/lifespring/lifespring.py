from .utils import *
from .eventsourcing import *


__all__ = [
    "lifespring",
]


def lifespring_transfer_func(
    state: LifeSpringState,
    event: LifeSpringEvent,
)-> LifeSpringState:

    transfer_func_router = {
        "create_bucket": create_bucket_transfer_func,
        "revalue_bucket": revalue_bucket_transfer_func,
        "archive_bucket": archive_bucket_transfer_func,
        "produce_value": produce_value_transfer_func,
        "consume_value": consume_value_transfer_func,
        "transfer_value": transfer_value_transfer_func,
    }
    
    if event.event_type not in transfer_func_router:
        raise NotImplementedError
    
    return transfer_func_router[event.event_type](state, event)


class LifeSpring:
    
    def __init__(
        self,
        database_path: str,
        snapshot_threshold: int,
        uid_length: int,
    )-> None:
        
        self._database_path = database_path
        self._event_manager = EventManager(
            transfer_func = lifespring_transfer_func,
            snapshot_threshold = snapshot_threshold,
            uid_length = uid_length,
        )
        self._event_sourcing_path = f"{self._database_path}{seperator}event_sourcing.pickle"
        if os.path.exists(self._event_sourcing_path):
            self._event_manager.loads(file_path=self._event_sourcing_path)
        else:
            initial_state = LifeSpringState(
                bucket_to_data = {},
            )
            self._event_manager.initialize(initial_state=initial_state)
            self._event_manager.dumps(file_path=self._event_sourcing_path)

    
    def update(
        self,
        event: LifeSpringEvent,
    )-> None:

        self._event_manager.update(event=event)
        self._event_manager.dumps(file_path=self._event_sourcing_path)
        
        
    def list_buckets(
        self,
    )-> None:
        
        latest_state: LifeSpringState = self._event_manager.fetch_latest_state()
        bucket_to_data = latest_state.bucket_to_data
        
        if not len(bucket_to_data):
            print("You've got no buckets yet!")
            return
        
        print(f"Your buckets:")
        for no, (bucket, bucket_data) in enumerate(sorted(
            bucket_to_data.items(),
            key = lambda item: float("-inf") \
                if item[1].bucket_status != "alive" else item[1].value,
            reverse = True,
        )):
            value = bucket_data.value
            value_unit = bucket_data.value_unit
            bucket_type = bucket_data.bucket_type
            status_string = "      [Archived]" \
                if bucket_data.bucket_status != "alive" else ""
            print(f"    {no}. ({bucket_type}) {bucket}: {value:.2f} {value_unit}{status_string}")


lifespring = LifeSpring(
    database_path = "data",
    snapshot_threshold = 10,
    uid_length = 16,
)