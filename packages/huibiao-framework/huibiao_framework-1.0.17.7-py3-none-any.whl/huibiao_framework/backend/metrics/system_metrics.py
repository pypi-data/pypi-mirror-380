import asyncio
import os
from abc import ABC, abstractmethod
from typing import List, Type

import psutil
from prometheus_client import Gauge

from loguru import logger


class MetricCollector(ABC):
    """指标收集器抽象基类"""

    def __init__(self, process: psutil.Process, pid: int):
        self.process = process
        self.pid = pid

    @abstractmethod
    async def collect(self):
        """收集指标数据"""
        pass


class CPUMetricCollector(MetricCollector):
    """CPU使用率指标收集器"""

    def __init__(self, process: psutil.Process, pid: int):
        super().__init__(process, pid)
        self.gauge = Gauge(
            "cpu_usage_percent",
            "CPU usage in percent",
            ["pid"],
            multiprocess_mode="all",
        )

    async def collect(self):
        cpu_usage = self.process.cpu_percent()
        self.gauge.labels(pid=self.pid).set(cpu_usage)


class MemoryMetricCollector(MetricCollector):
    """内存使用量指标收集器"""

    def __init__(self, process: psutil.Process, pid: int):
        super().__init__(process, pid)
        self.gauge = Gauge(
            "memory_usage_mb", "Memory usage in MB", ["pid"], multiprocess_mode="all"
        )

    async def collect(self):
        memory_info = self.process.memory_info()
        memory_usage = memory_info.rss / (1024 * 1024)
        self.gauge.labels(pid=self.pid).set(memory_usage)


class ThreadCountMetricCollector(MetricCollector):
    """线程数指标收集器"""

    def __init__(self, process: psutil.Process, pid: int):
        super().__init__(process, pid)
        self.gauge = Gauge(
            "thread_count", "Number of threads", ["pid"], multiprocess_mode="all"
        )

    async def collect(self):
        thread_count = self.process.num_threads()
        self.gauge.labels(pid=self.pid).set(thread_count)


class SystemMetricsMonitor:
    """系统指标监控器 - 采用组装模式"""

    def __init__(self):
        self.pid = os.getpid()
        self.process = psutil.Process(self.pid)
        self.collectors: List[MetricCollector] = []

    def assemble(self, *collector_classes: Type[MetricCollector]) -> 'SystemMetricsMonitor':
        """组装指标收集器 - 采用可变长度参数"""
        if len(self.collectors) > 0:
            logger.warning("已存在指标收集器，请勿重复组装")
            return self

        for collector_class in collector_classes:
            collector_instance = collector_class(self.process, self.pid)
            self.collectors.append(collector_instance)

        logger.info(f"已组装 {len(self.collectors)} 个指标收集器")

        return self

    def assemble_default(self) -> 'SystemMetricsMonitor':
        """
        组装默认指标收集器
        """
        return self.assemble(CPUMetricCollector, MemoryMetricCollector, ThreadCountMetricCollector)

    async def run_monitor(self, interval_sec: int = 10):
        """运行监控任务"""

        async def work():
            while True:
                # 执行所有收集器的收集任务
                for collector in self.collectors:
                    await collector.collect()

                await asyncio.sleep(interval_sec)

        if self.collectors:
            asyncio.create_task(work())
