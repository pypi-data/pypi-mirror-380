from .utils import *


__all__ = [
    "EventManager",
]


_State = TypeVar("_State")
_Event = TypeVar("_Event")


class EventManager:
    
    def __init__(
        self,
        transfer_func: Callable[[_State, _Event], _State],
        snapshot_threshold: int,
        uid_length: int = 16,
    )-> None:
        
        self._transfer_func = transfer_func
        self._snapshot_threshold = snapshot_threshold
        
        self._uid_generator = UIDGenerator()
        self._uid_length = uid_length
        
        self._event_sequence: List[Dict[str, Any]] = []
        self._id_to_tick: Dict[str, int] = {}
        self._ids: Set[str] = set()
        self._next_tick = 0
        self._latest_snapshot_tick = -1
        
        
    def initialize(
        self,
        initial_state: Any,
    )-> None:
        
        _id = self._get_uid()
        
        self._event_sequence = [{
            "id": _id,
            "time": get_current_time(),
            "event": None,
            "state": initial_state,
        }]
        self._id_to_tick[_id] = 0
        self._ids = set({_id})
        self._next_tick = 1
        self._latest_snapshot_tick = 0

    
    def loads(
        self,
        file_path: str,
    )-> None:
        
        with open(file=file_path, mode="rb") as file_pointer:
            data = pickle.load(file_pointer)
        self._event_sequence = data["event_sequence"]
        self._id_to_tick = data["id_to_tick"]
        self._ids = data["ids"]
        
        self._uid_generator.update_existing_uids(self._ids)
        
        self._next_tick = len(self._event_sequence)
        self._latest_snapshot_tick = -1
        for i in range(self._next_tick - 1, -1, -1):
            state = self._event_sequence[i]["state"]
            if state is not None:
                self._latest_snapshot_tick = i; break
    

    def dumps(
        self,
        file_path: str,
    )-> None:
        
        data = {
            "event_sequence": self._event_sequence,
            "id_to_tick": self._id_to_tick,
            "ids": self._ids,
        }
        with open(file=file_path, mode="wb") as file_pointer:
            pickle.dump(data, file_pointer)
            
            
    def update(
        self,
        event: Any,
    )-> str:
        
        _id = self._get_uid()
        
        if self._next_tick % self._snapshot_threshold:
            state = self._fetch_latest_state()
            self._latest_snapshot_tick = self._next_tick
        else:
            state = None
            
        self._event_sequence.append({
            "id": _id,
            "time": get_current_time(),
            "event": event,
            "state": state,
        })
        self._id_to_tick[_id] = self._next_tick
        self._ids.add(_id)
        self._next_tick += 1
        
        return _id


    def fetch_latest_state(
        self,
    )-> Any:
        
        return self._fetch_latest_state()
    
    
    def _get_uid(
        self,
    )-> str:
        
        return self._uid_generator.generate(
            uid_length = self._uid_length
        )
    
    
    def _fetch_latest_state(
        self,
    )-> Any:
        
        if self._latest_snapshot_tick < 0: 
            raise RuntimeError
        
        state = self._event_sequence[self._latest_snapshot_tick]["state"]
        for tick in range(self._latest_snapshot_tick + 1, self._next_tick):
            event = self._event_sequence[tick]["event"]
            state = self._transfer_func(state, event)
        return state
    
    
    
    
    
    
    
    
    
    