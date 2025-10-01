from datetime import datetime
from typing import Any, Dict, List, Tuple, Union


class ArgumentSerializer:

    @staticmethod
    def serialize(args: List, kwargs: Dict) -> Union[List, Dict]:
        if not kwargs:
            return args

        result = {"args": args}
        result.update(kwargs)
        return result

    @staticmethod
    def deserialize(data: Union[List, Dict]) -> Tuple[List, Dict]:
        if isinstance(data, list):
            return data, {}
        elif isinstance(data, dict):
            args = data.get("args", [])
            kwargs = {k: v for k, v in data.items() if k != "args"}
            return args, kwargs
        else:
            return [], {}

    @staticmethod
    def serialize_value(value: Any) -> Any:
        if isinstance(value, (str, int, float, bool, type(None))):
            return value
        elif isinstance(value, (list, tuple)):
            return [ArgumentSerializer.serialize_value(item) for item in value]
        elif isinstance(value, dict):
            return {k: ArgumentSerializer.serialize_value(v) for k, v in value.items()}
        elif isinstance(value, datetime):
            return {"__datetime__": value.isoformat()}
        elif hasattr(value, "__dict__"):
            return {
                "__class__": f"{value.__class__.__module__}.{value.__class__.__name__}",
                "__data__": value.__dict__
            }
        else:
            return {"__repr__": repr(value)}

    @staticmethod
    def deserialize_value(data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        if "__datetime__" in data:
            return datetime.fromisoformat(data["__datetime__"])
        elif "__class__" in data and "__data__" in data:
            return data["__data__"]
        elif "__repr__" in data:
            return data["__repr__"]
        else:
            return {k: ArgumentSerializer.deserialize_value(v) for k, v in data.items()}
