#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2025-09-27 17:02:39
@Author  :   chakcy
@Email   :   947105045@qq.com
@description   :   队列调度器
"""


from .standard import StandardQueueScheduler
from ._async import AsyncQueueScheduler
from .base import BaseScheduler
from ..model import MessageItem
from typing import Callable
import multiprocessing


SCHEDULER_TYPES = {"standard": StandardQueueScheduler, "async": AsyncQueueScheduler}


class QueueScheduler(BaseScheduler):
    def __init__(
        self,
        receive_thread_num=1,
        task_thread_num=multiprocessing.cpu_count() * 2,
        shard_num=4,
        scheduler_type="standard",
    ):
        scheduler_class = SCHEDULER_TYPES.get(scheduler_type, None)
        if not scheduler_class:
            raise ValueError(f"Invalid scheduler type: {scheduler_type}")
        self.scheduler = scheduler_class(receive_thread_num, task_thread_num, shard_num)

        if self.scheduler:
            self.queue_operation = self.scheduler.queue_operation

    def send_message(self, message: MessageItem, callback: Callable):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        self.scheduler.send_message(message, callback)

    def start(self):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        self.scheduler.start()

    def stop(self):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        self.scheduler.stop()

    def update_listen_data(self, key, value):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        self.scheduler.update_listen_data(key, value)

    def get_listen_datas(self):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        return self.scheduler.get_listen_datas()

    def get_listen_data(self, key):
        if not self.scheduler:
            raise Exception("Scheduler not initialized")
        return self.scheduler.get_listen_data(key)


__all__ = ["QueueScheduler"]
