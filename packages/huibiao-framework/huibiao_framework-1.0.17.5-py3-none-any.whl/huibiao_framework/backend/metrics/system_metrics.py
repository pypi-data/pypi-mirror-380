import asyncio
import os

import psutil
from prometheus_client import Gauge


class SystemMetricsMonitor:
    def __init__(self):
        self.CPU_GAUGE = Gauge(
            "cpu_usage_percent",
            "CPU usage in percent",
            ["pid"],
            multiprocess_mode="all",
        )

        self.MEMORY_GAUGE = Gauge(
            "memory_usage_mb", "Memory usage in MB", ["pid"], multiprocess_mode="all"
        )

        self.pid = os.getpid()
        self.process = psutil.Process(self.pid)

    async def run_monitor(self, interval_sec: int = 10):
        async def work():
            while True:
                cpu_usage = self.process.cpu_percent()
                self.CPU_GAUGE.labels(pid=self.pid).set(cpu_usage)

                memory_info = self.process.memory_info()
                memory_usage = memory_info.rss / (1024 * 1024)
                self.MEMORY_GAUGE.labels(pid=self.process).set(memory_usage)

                await asyncio.sleep(interval_sec)

        asyncio.create_task(work())
