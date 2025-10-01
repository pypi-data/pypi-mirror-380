import asyncio
import logging
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING, AsyncIterator, Callable, Dict, List, Optional

from nats.aio.client import Client as NATS
from nats.errors import NoRespondersError
from nats.errors import TimeoutError as NatsTimeout
from nats.js import JetStreamContext
from nats.js.api import (
    ConsumerConfig,
    DiscardPolicy,
    RetentionPolicy,
    StorageType,
    StreamConfig,
)
from nats.js.errors import APIError

if TYPE_CHECKING:
    from nats.aio.msg import Msg

logger = logging.getLogger(__name__)

class NatsError(Exception):
    """Base exception for NATS-related errors"""
    pass

class NatsConnectionError(NatsError):
    """Connection-related errors"""
    pass

class NatsTimeoutError(NatsError):
    """Timeout-related errors"""
    pass

class NatsPublishError(NatsError):
    """Publishing-related errors"""
    pass

class NatsConnectionManager:
    """Manages NATS connections with pooling and reconnection"""

    def __init__(self, servers: List[str] = None, options: Dict = None):
        self.servers = servers or ["nats://localhost:4222"]
        self.options = options or {}
        self._connection: Optional[NATS] = None
        self._js: Optional[JetStreamContext] = None
        self._lock = asyncio.Lock()
        self._connected = False
        self._reconnect_attempts = 0
        self._max_reconnect_attempts = 10

    async def connect(self) -> NATS:
        """Establish connection to NATS"""
        async with self._lock:
            if self._connected and self._connection:
                return self._connection

            self._connection = NATS()

            # Configure connection options
            connect_options = {
                "servers": self.servers,
                "max_reconnect_attempts": self._max_reconnect_attempts,
                "reconnect_time_wait": 2,
                "error_cb": self._error_callback,
                "disconnected_cb": self._disconnected_callback,
                "reconnected_cb": self._reconnected_callback,
                **self.options
            }

            try:
                await self._connection.connect(**connect_options)
                self._js = self._connection.jetstream()
                self._connected = True
                self._reconnect_attempts = 0

                logger.info(f"Connected to NATS servers: {self.servers}")
                return self._connection
            except Exception as e:
                raise NatsConnectionError(f"Failed to connect to NATS: {e}")

    async def disconnect(self):
        """Close NATS connection"""
        async with self._lock:
            if self._connection and self._connected:
                await self._connection.close()
                self._connected = False
                logger.info("Disconnected from NATS")

    async def _error_callback(self, e):
        logger.error(f"NATS connection error: {e}")

    async def _disconnected_callback(self):
        self._connected = False
        logger.warning("NATS connection lost")

    async def _reconnected_callback(self):
        self._connected = True
        logger.info("NATS connection restored")

class CoreNatsClient:
    """Core NATS operations for request-reply messaging"""

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager

    async def request(self, subject: str, data: bytes, timeout: float = 5.0) -> bytes:
        """Send request and wait for reply"""
        nc = await self.connection_manager.connect()

        try:
            msg = await nc.request(subject, data, timeout=timeout)
            return msg.data
        except asyncio.TimeoutError:
            raise NatsTimeoutError(f"Request to {subject} timed out after {timeout}s")
        except NoRespondersError:
            raise NatsError(f"No responders for request to {subject}")
        except Exception as e:
            raise NatsError(f"Request failed: {e}")

    async def publish(self, subject: str, data: bytes, reply_to: str = None):
        """Publish message to subject"""
        nc = await self.connection_manager.connect()
        await nc.publish(subject, data, reply=reply_to)

    async def subscribe(self, subject: str, callback: Callable, queue: str = None):
        """Subscribe to subject with callback"""
        nc = await self.connection_manager.connect()

        async def message_handler(msg):
            try:
                await callback(msg)
            except Exception as e:
                logger.error(f"Error handling message on {subject}: {e}")

        if queue:
            sub = await nc.subscribe(subject, queue=queue, cb=message_handler)
        else:
            sub = await nc.subscribe(subject, cb=message_handler)

        logger.info(f"Subscribed to {subject}" + (f" (queue: {queue})" if queue else ""))
        return sub

class JetStreamClient:
    """JetStream operations for persistent messaging"""

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager

    async def create_stream(self, stream_config: StreamConfig):
        """Create JetStream stream"""
        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        try:
            await js.add_stream(stream_config)
            logger.info(f"Created stream: {stream_config.name}")
        except Exception as e:
            error_msg = str(e).lower()
            if "stream name already in use" in error_msg or "already exists" in error_msg:
                logger.debug(f"Stream {stream_config.name} already exists")
            else:
                raise NatsError(f"Failed to create stream: {e}")

    async def publish_async(self, subject: str, data: bytes, headers: Dict = None) -> int:
        """Publish message to JetStream"""
        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        try:
            ack = await js.publish(subject, data, headers=headers)
            return ack.seq
        except Exception as e:
            raise NatsPublishError(f"JetStream publish failed: {e}")

    async def create_consumer(self, stream: str, consumer_config: ConsumerConfig):
        """Create JetStream consumer"""
        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        try:
            ci = await js.add_consumer(stream, consumer_config)
            logger.info(f"Created consumer: {consumer_config.durable_name or consumer_config.name}")
            return ci
        except APIError as e:
            if "consumer name already in use" not in str(e).lower():
                raise NatsError(f"Failed to create consumer: {e}")

    async def pull_subscribe(self, stream: str, durable_name: str = None, subject: str = None) -> AsyncIterator['Msg']:
        """Create pull-based subscription"""
        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        if subject is None:
            # Default subject for pull
            subject = f"{stream}.$JS.API.CONSUMER.MSG.NEXT.{durable_name}"

        psub = await js.pull_subscribe(subject, stream=stream, durable=durable_name)

        try:
            while True:
                try:
                    msgs = await psub.fetch(batch=10, timeout=5.0)  # batch of 10
                    for msg in msgs:
                        yield msg
                except NatsTimeout:
                    continue
                except Exception as e:
                    logger.error(f"Error in pull subscription: {e}")
                    raise
        finally:
            await psub.unsubscribe()

@dataclass
class NatsWorkStreamConfig:
    """Configuration for NatsWork JetStream streams"""

    name: str
    subjects: List[str]
    retention: str = "workqueue"  # workqueue, limits, interest
    max_msgs: int = 1_000_000
    max_bytes: int = 1_073_741_824  # 1GB
    max_age: int = 86400  # 24 hours
    max_msg_size: int = 1_048_576  # 1MB
    storage: str = "file"  # file, memory
    replicas: int = 1
    discard: str = "old"  # old, new

class StreamManager:
    """Manages JetStream streams for job queues"""

    def __init__(self, js_client: JetStreamClient):
        self.js_client = js_client
        self._streams_created = set()

    async def ensure_job_stream(self, queue_name: str):
        """Ensure stream exists for job queue"""
        stream_name = f"JOBS_{queue_name.upper()}"

        if stream_name in self._streams_created:
            return

        config = NatsWorkStreamConfig(
            name=stream_name,
            subjects=[f"natswork.jobs.{queue_name}", f"natswork.jobs.{queue_name}.>"]
        )

        js_config = self._to_jetstream_config(config)
        await self.js_client.create_stream(js_config)
        self._streams_created.add(stream_name)

    def _to_jetstream_config(self, config: NatsWorkStreamConfig) -> StreamConfig:
        """Convert to nats.py StreamConfig"""
        retention_name = config.retention.upper().replace('WORKQUEUE', 'WORK_QUEUE')
        return StreamConfig(
            name=config.name,
            subjects=config.subjects,
            retention=RetentionPolicy[retention_name],
            max_msgs=config.max_msgs,
            max_bytes=config.max_bytes,
            max_age=config.max_age,
            max_msg_size=config.max_msg_size,
            storage=StorageType[config.storage.upper()],
            num_replicas=config.replicas,
            discard=DiscardPolicy[config.discard.upper()]
        )

class NatsConnectionPool:
    """Connection pool for NATS clients"""

    def __init__(self, max_connections: int = 10, servers: List[str] = None, options: Dict = None):
        self.max_connections = max_connections
        self.servers = servers or ["nats://localhost:4222"]
        self.options = options or {}
        self._pool: List[NatsConnectionManager] = []
        self._in_use: set = set()
        self._lock = asyncio.Lock()

    async def acquire(self) -> NatsConnectionManager:
        """Acquire connection from pool"""
        async with self._lock:
            available = [conn for conn in self._pool if conn not in self._in_use]

            if available:
                connection = available[0]
                self._in_use.add(connection)
                return connection

            if len(self._pool) < self.max_connections:
                connection = NatsConnectionManager(servers=self.servers, options=self.options)
                await connection.connect()
                self._pool.append(connection)
                self._in_use.add(connection)
                return connection

        # Wait for connection to become available
        while True:
            async with self._lock:
                available = [conn for conn in self._pool if conn not in self._in_use]
                if available:
                    connection = available[0]
                    self._in_use.add(connection)
                    return connection
            await asyncio.sleep(0.1)

    async def release(self, connection: NatsConnectionManager):
        """Release connection back to pool"""
        async with self._lock:
            self._in_use.discard(connection)

    async def close_all(self):
        """Close all connections in pool"""
        async with self._lock:
            for connection in list(self._pool):
                await connection.disconnect()
            self._pool.clear()
            self._in_use.clear()

class CircuitBreaker:
    """Circuit breaker pattern for NATS operations"""

    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    async def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        if self.state == "OPEN":
            if time.time() - (self.last_failure_time or 0) > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise NatsError("Circuit breaker is OPEN")

        try:
            result = await func(*args, **kwargs)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            raise e
