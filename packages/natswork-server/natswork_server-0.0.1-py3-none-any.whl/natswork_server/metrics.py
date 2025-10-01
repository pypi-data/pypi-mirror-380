import threading
import time
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class MetricPoint:
    name: str
    value: float
    timestamp: datetime
    labels: Dict[str, str] = field(default_factory=dict)


class MetricsCollector(ABC):

    @abstractmethod
    def increment_counter(self, name: str, labels: Dict[str, str] = None, value: float = 1.0):
        pass

    @abstractmethod
    def record_gauge(self, name: str, value: float, labels: Dict[str, str] = None):
        pass

    @abstractmethod
    def record_histogram(self, name: str, value: float, labels: Dict[str, str] = None):
        pass

    @abstractmethod
    def get_metrics(self) -> List[MetricPoint]:
        pass


class InMemoryMetricsCollector(MetricsCollector):

    def __init__(self, max_points: int = 10000):
        self.max_points = max_points
        self._counters: Dict[str, float] = defaultdict(float)
        self._gauges: Dict[str, float] = {}
        self._histograms: Dict[str, deque] = defaultdict(lambda: deque(maxlen=1000))
        self._metrics_history: deque = deque(maxlen=max_points)
        self._lock = threading.Lock()

    def increment_counter(self, name: str, labels: Dict[str, str] = None, value: float = 1.0):
        with self._lock:
            key = self._make_key(name, labels)
            self._counters[key] += value

            self._metrics_history.append(MetricPoint(
                name=name,
                value=self._counters[key],
                timestamp=datetime.utcnow(),
                labels=labels or {}
            ))

    def record_gauge(self, name: str, value: float, labels: Dict[str, str] = None):
        with self._lock:
            key = self._make_key(name, labels)
            self._gauges[key] = value

            self._metrics_history.append(MetricPoint(
                name=name,
                value=value,
                timestamp=datetime.utcnow(),
                labels=labels or {}
            ))

    def record_histogram(self, name: str, value: float, labels: Dict[str, str] = None):
        with self._lock:
            key = self._make_key(name, labels)
            self._histograms[key].append(value)

            self._metrics_history.append(MetricPoint(
                name=name,
                value=value,
                timestamp=datetime.utcnow(),
                labels=labels or {}
            ))

    def get_metrics(self) -> List[MetricPoint]:
        with self._lock:
            return list(self._metrics_history)

    def get_counter(self, name: str, labels: Dict[str, str] = None) -> float:
        key = self._make_key(name, labels)
        return self._counters.get(key, 0.0)

    def get_histogram_stats(self, name: str, labels: Dict[str, str] = None) -> Dict[str, float]:
        key = self._make_key(name, labels)
        values = list(self._histograms.get(key, []))

        if not values:
            return {}

        values.sort()
        n = len(values)

        return {
            "count": n,
            "sum": sum(values),
            "avg": sum(values) / n,
            "min": values[0],
            "max": values[-1],
            "p50": values[n // 2],
            "p95": values[int(n * 0.95)] if n > 0 else 0,
            "p99": values[int(n * 0.99)] if n > 0 else 0,
        }

    def _make_key(self, name: str, labels: Dict[str, str] = None) -> str:
        if not labels:
            return name

        label_str = ",".join(f"{k}={v}" for k, v in sorted(labels.items()))
        return f"{name}[{label_str}]"


class WorkerMetrics:

    def __init__(self, metrics_collector: MetricsCollector):
        self.metrics = metrics_collector
        self._worker_start_time = time.time()

    def record_worker_started(self, worker_id: str, queue: str):
        labels = {"worker_id": worker_id, "queue": queue}
        self.metrics.increment_counter("workers_started", labels)
        self.metrics.record_gauge("worker_uptime", 0, labels)

    def record_worker_stopped(self, worker_id: str, queue: str):
        labels = {"worker_id": worker_id, "queue": queue}
        uptime = time.time() - self._worker_start_time

        self.metrics.increment_counter("workers_stopped", labels)
        self.metrics.record_gauge("worker_uptime", uptime, labels)

    def update_worker_stats(self, worker_id: str, queue: str, stats: Dict[str, Any]):
        labels = {"worker_id": worker_id, "queue": queue}

        for metric_name, value in stats.items():
            if isinstance(value, (int, float)):
                self.metrics.record_gauge(f"worker_{metric_name}", float(value), labels)


class PrometheusMetricsCollector(MetricsCollector):
    """Prometheus-compatible metrics collector (optional, requires prometheus_client)"""

    def __init__(self):
        try:
            from prometheus_client import REGISTRY, Counter, Gauge, Histogram
            self.Counter = Counter
            self.Gauge = Gauge
            self.Histogram = Histogram
            self._registry = REGISTRY
            self._metrics = {}
        except ImportError:
            raise ImportError(
                "prometheus_client is required for PrometheusMetricsCollector. "
                "Install with: pip install prometheus_client"
            )

    def increment_counter(self, name: str, labels: Dict[str, str] = None, value: float = 1.0):
        metric = self._get_or_create_counter(name, labels)
        if labels:
            metric.labels(**labels).inc(value)
        else:
            metric.inc(value)

    def record_gauge(self, name: str, value: float, labels: Dict[str, str] = None):
        metric = self._get_or_create_gauge(name, labels)
        if labels:
            metric.labels(**labels).set(value)
        else:
            metric.set(value)

    def record_histogram(self, name: str, value: float, labels: Dict[str, str] = None):
        metric = self._get_or_create_histogram(name, labels)
        if labels:
            metric.labels(**labels).observe(value)
        else:
            metric.observe(value)

    def get_metrics(self) -> List[MetricPoint]:
        # Prometheus manages its own metrics registry
        return []

    def _get_or_create_counter(self, name: str, labels: Dict[str, str] = None):
        key = f"counter_{name}"
        if key not in self._metrics:
            label_names = list(labels.keys()) if labels else []
            self._metrics[key] = self.Counter(
                f"natswork_{name}_total",
                f"NatsWork {name} counter",
                label_names
            )
        return self._metrics[key]

    def _get_or_create_gauge(self, name: str, labels: Dict[str, str] = None):
        key = f"gauge_{name}"
        if key not in self._metrics:
            label_names = list(labels.keys()) if labels else []
            self._metrics[key] = self.Gauge(
                f"natswork_{name}",
                f"NatsWork {name} gauge",
                label_names
            )
        return self._metrics[key]

    def _get_or_create_histogram(self, name: str, labels: Dict[str, str] = None):
        key = f"histogram_{name}"
        if key not in self._metrics:
            label_names = list(labels.keys()) if labels else []
            self._metrics[key] = self.Histogram(
                f"natswork_{name}_duration_seconds",
                f"NatsWork {name} histogram",
                label_names
            )
        return self._metrics[key]


_default_metrics_collector: MetricsCollector = InMemoryMetricsCollector()


def get_default_metrics_collector() -> MetricsCollector:
    return _default_metrics_collector


def set_default_metrics_collector(collector: MetricsCollector):
    global _default_metrics_collector
    _default_metrics_collector = collector
