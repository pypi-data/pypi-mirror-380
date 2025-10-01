"""HTTP server for health check endpoints"""
import asyncio
import json
import logging
from datetime import datetime

logger = logging.getLogger("natswork.health.http")


class SimpleHTTPHealthServer:
    """Lightweight HTTP server for health checks without external dependencies"""

    def __init__(self, health_monitor, host: str = "0.0.0.0", port: int = 8080):
        self.health_monitor = health_monitor
        self.host = host
        self.port = port
        self.server = None
        self._running = False

    async def start(self):
        """Start HTTP health server"""
        self.server = await asyncio.start_server(
            self._handle_client, self.host, self.port
        )
        self._running = True

        logger.info(f"Health HTTP server started on {self.host}:{self.port}")

        async with self.server:
            await self.server.serve_forever()

    async def stop(self):
        """Stop HTTP health server"""
        self._running = False
        if self.server:
            self.server.close()
            await self.server.wait_closed()

        logger.info("Health HTTP server stopped")

    async def _handle_client(self, reader, writer):
        """Handle incoming HTTP request"""
        try:
            # Read request line
            request_line = await reader.readline()
            request_str = request_line.decode('utf-8').strip()

            if not request_str:
                writer.close()
                await writer.wait_closed()
                return

            # Parse request
            parts = request_str.split()
            if len(parts) < 2:
                await self._send_response(writer, 400, "Bad Request", {})
                return

            method = parts[0]
            path = parts[1]

            # Read headers (we don't really need them for health checks)
            while True:
                line = await reader.readline()
                if line == b'\r\n' or line == b'\n' or not line:
                    break

            # Route request
            if method == "GET":
                if path == "/health":
                    await self._health_handler(writer)
                elif path == "/health/live":
                    await self._liveness_handler(writer)
                elif path == "/health/ready":
                    await self._readiness_handler(writer)
                elif path == "/metrics":
                    await self._metrics_handler(writer)
                else:
                    await self._send_response(writer, 404, "Not Found", {"error": "Endpoint not found"})
            else:
                await self._send_response(writer, 405, "Method Not Allowed", {"error": "Only GET is supported"})

        except Exception as e:
            logger.error(f"Error handling request: {e}", exc_info=True)
            try:
                await self._send_response(writer, 500, "Internal Server Error", {"error": str(e)})
            except:
                pass
        finally:
            try:
                writer.close()
                await writer.wait_closed()
            except:
                pass

    async def _health_handler(self, writer):
        """Comprehensive health status"""
        from .health import HealthStatus

        results = await self.health_monitor.check_all()
        overall_status = self.health_monitor.get_overall_status()

        response_data = {
            "status": overall_status.value,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "checks": {}
        }

        for name, result in results.items():
            response_data["checks"][name] = {
                "status": result.status.value,
                "message": result.message,
                "duration_ms": result.duration_ms,
                "details": result.details
            }

        status_code = 200 if overall_status in [HealthStatus.HEALTHY, HealthStatus.WARNING] else 503

        await self._send_response(
            writer, status_code, "OK" if status_code == 200 else "Service Unavailable", response_data
        )

    async def _liveness_handler(self, writer):
        """Kubernetes liveness probe"""
        await self._send_response(writer, 200, "OK", {"status": "alive"})

    async def _readiness_handler(self, writer):
        """Kubernetes readiness probe"""
        from .health import HealthStatus

        await self.health_monitor.check_all()
        overall_status = self.health_monitor.get_overall_status()

        if overall_status == HealthStatus.HEALTHY:
            await self._send_response(writer, 200, "OK", {"status": "ready"})
        else:
            await self._send_response(writer, 503, "Service Unavailable", {"status": "not_ready"})

    async def _metrics_handler(self, writer):
        """Simple metrics endpoint"""
        try:
            # Get metrics from the health monitor's last results
            results = self.health_monitor.last_results

            metrics_lines = [
                "# NatsWork Health Metrics",
                f"# Timestamp: {datetime.utcnow().isoformat()}Z",
                ""
            ]

            for name, result in results.items():
                # Convert health status to numeric (1=healthy, 0=unhealthy)
                from .health import HealthStatus
                status_value = 1 if result.status == HealthStatus.HEALTHY else 0

                metrics_lines.append(f'natswork_health_check{{check="{name}"}} {status_value}')
                metrics_lines.append(f'natswork_health_check_duration_ms{{check="{name}"}} {result.duration_ms}')

            metrics_text = "\n".join(metrics_lines)

            # Send plain text response
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/plain; version=0.0.4\r\n"
            response += f"Content-Length: {len(metrics_text)}\r\n"
            response += "Connection: close\r\n"
            response += "\r\n"
            response += metrics_text

            writer.write(response.encode('utf-8'))
            await writer.drain()

        except Exception as e:
            logger.error(f"Error generating metrics: {e}")
            await self._send_response(writer, 500, "Internal Server Error", {"error": str(e)})

    async def _send_response(self, writer, status_code: int, status_text: str, data: dict):
        """Send HTTP JSON response"""
        json_data = json.dumps(data, indent=2)

        response = f"HTTP/1.1 {status_code} {status_text}\r\n"
        response += "Content-Type: application/json\r\n"
        response += f"Content-Length: {len(json_data)}\r\n"
        response += "Connection: close\r\n"
        response += "\r\n"
        response += json_data

        writer.write(response.encode('utf-8'))
        await writer.drain()
