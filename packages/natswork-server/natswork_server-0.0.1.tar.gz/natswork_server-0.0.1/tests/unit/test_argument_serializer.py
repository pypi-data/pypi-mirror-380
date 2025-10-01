from datetime import datetime

from natswork_server.argument_serializer import ArgumentSerializer


def test_serialize_args_only():
    args = [1, 2, 3]
    kwargs = {}
    result = ArgumentSerializer.serialize(args, kwargs)
    assert result == [1, 2, 3]


def test_serialize_with_kwargs():
    args = [1, 2]
    kwargs = {"key": "value"}
    result = ArgumentSerializer.serialize(args, kwargs)
    assert result == {"args": [1, 2], "key": "value"}


def test_deserialize_list():
    data = [1, 2, 3]
    args, kwargs = ArgumentSerializer.deserialize(data)
    assert args == [1, 2, 3]
    assert kwargs == {}


def test_deserialize_dict():
    data = {"args": [1, 2], "key": "value"}
    args, kwargs = ArgumentSerializer.deserialize(data)
    assert args == [1, 2]
    assert kwargs == {"key": "value"}


def test_serialize_value_primitive():
    assert ArgumentSerializer.serialize_value(42) == 42
    assert ArgumentSerializer.serialize_value("hello") == "hello"
    assert ArgumentSerializer.serialize_value(True) is True
    assert ArgumentSerializer.serialize_value(None) is None


def test_serialize_value_list():
    result = ArgumentSerializer.serialize_value([1, "two", 3.0])
    assert result == [1, "two", 3.0]


def test_serialize_value_dict():
    result = ArgumentSerializer.serialize_value({"a": 1, "b": 2})
    assert result == {"a": 1, "b": 2}


def test_serialize_value_datetime():
    dt = datetime(2024, 1, 1, 12, 0, 0)
    result = ArgumentSerializer.serialize_value(dt)
    assert "__datetime__" in result
    assert result["__datetime__"] == dt.isoformat()


def test_deserialize_value_datetime():
    data = {"__datetime__": "2024-01-01T12:00:00"}
    result = ArgumentSerializer.deserialize_value(data)
    assert isinstance(result, datetime)
    assert result == datetime(2024, 1, 1, 12, 0, 0)


def test_serialize_value_object():
    class TestClass:
        def __init__(self):
            self.foo = "bar"

    obj = TestClass()
    result = ArgumentSerializer.serialize_value(obj)
    assert "__class__" in result
    assert "__data__" in result
    assert result["__data__"]["foo"] == "bar"


def test_deserialize_empty():
    args, kwargs = ArgumentSerializer.deserialize([])
    assert args == []
    assert kwargs == {}


def test_roundtrip():
    original_args = [1, "test", 3.14]
    original_kwargs = {"key": "value", "num": 42}

    serialized = ArgumentSerializer.serialize(original_args, original_kwargs)
    args, kwargs = ArgumentSerializer.deserialize(serialized)

    assert args == original_args
    assert kwargs == original_kwargs
