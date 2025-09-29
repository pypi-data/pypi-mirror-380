import threading
import time
import logging
from typing import Optional

from .client import Client
from .task_queue import TaskQueue
from .constants import DEFAULT_WORKER_NUM

logger = logging.getLogger(__name__)


class TaskProcessor:
    """任务处理器"""

    def __init__(
        self,
        queue: TaskQueue,
        client: Client,
        worker_num: int = DEFAULT_WORKER_NUM
    ):
        """
        初始化任务处理器

        Args:
            queue: 任务队列
            client: 客户端
            worker_num: 工作线程数
        """
        self.queue = queue
        self.client = client
        self.worker_num = worker_num
        self.stop_event = threading.Event()
        self.workers = []

        logger.info(f"TaskProcessor initialized with {worker_num} workers")

    def start(self):
        """启动处理器"""
        logger.info(f"Starting {self.worker_num} workers...")

        for i in range(self.worker_num):
            worker = threading.Thread(
                target=self._worker,
                args=(i,),
                daemon=True
            )
            worker.start()
            self.workers.append(worker)

        logger.info("All workers started")

    def _worker(self, worker_id: int):
        """工作线程"""
        logger.info(f"Worker-{worker_id} started")

        while not self.stop_event.is_set():
            task = self.queue.get_next_task()

            if task is None:
                time.sleep(1)
                continue

            logger.info(f"Worker-{worker_id} processing task: {task.id}")

            try:
                self.client.wait_for_task_completion(
                    task.id,
                    self.queue.on_task_completed
                )
            except Exception as e:
                logger.error(f"Worker-{worker_id} failed to process task {task.id}: {e}")

        logger.info(f"Worker-{worker_id} stopped")

    def stop(self, timeout: float = 30):
        """停止处理器"""
        logger.info("Stopping TaskProcessor...")
        self.stop_event.set()

        for worker in self.workers:
            worker.join(timeout=timeout/len(self.workers))

        logger.info("TaskProcessor stopped")