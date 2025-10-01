from natswork_server.metrics import InMemoryMetricsCollector, WorkerMetrics


def test_increment_counter():
    collector = InMemoryMetricsCollector()

    collector.increment_counter("test_counter", {"label": "value"}, 5.0)
    counter_value = collector.get_counter("test_counter", {"label": "value"})

    assert counter_value == 5.0


def test_record_gauge():
    collector = InMemoryMetricsCollector()

    collector.record_gauge("test_gauge", 42.0, {"label": "value"})
    metrics = collector.get_metrics()

    assert len(metrics) == 1
    assert metrics[0].value == 42.0


def test_record_histogram():
    collector = InMemoryMetricsCollector()

    for i in range(10):
        collector.record_histogram("test_histogram", float(i), {"label": "value"})

    stats = collector.get_histogram_stats("test_histogram", {"label": "value"})

    assert stats["count"] == 10
    assert stats["min"] == 0.0
    assert stats["max"] == 9.0
    assert stats["avg"] == 4.5


def test_worker_metrics():
    collector = InMemoryMetricsCollector()
    worker_metrics = WorkerMetrics(collector)

    worker_metrics.record_worker_started("worker-1", "default")

    counter = collector.get_counter("workers_started", {"worker_id": "worker-1", "queue": "default"})
    assert counter == 1.0


def test_make_key_with_labels():
    collector = InMemoryMetricsCollector()

    key1 = collector._make_key("metric", {"a": "1", "b": "2"})
    key2 = collector._make_key("metric", {"b": "2", "a": "1"})

    assert key1 == key2
