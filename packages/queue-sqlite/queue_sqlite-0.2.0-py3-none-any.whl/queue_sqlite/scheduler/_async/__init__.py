#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2025-09-27 17:04:34
@Author  :   chakcy
@Email   :   947105045@qq.com
@description   :   异步调度器
"""


from .async_receive_scheduler import AsyncReceiveScheduler
from .async_task_scheduler import AsyncTaskScheduler
from .async_listen_data_scheduler import AsyncListenDataScheduler
from ...model import MessageItem
from ...queue_operation.listen_operation import ListenOperation
from typing import Callable
from queue_sqlite_core import ShardedQueueOperation
import os
from ..base import BaseScheduler
from ..cleanup_scheduler import CleanupScheduler


class AsyncQueueScheduler(BaseScheduler):

    def __init__(
        self, receive_thread_num=1, task_thread_num=1, shard_num=4, queue_name="default"
    ):
        self.queue_operation = ShardedQueueOperation(shard_num, queue_name=queue_name)
        self.receive_scheduler = AsyncReceiveScheduler(
            self.queue_operation, receive_thread_num
        )
        self.listen_operation = ListenOperation(
            os.path.join(self.queue_operation.db_dir, "listen.db")
        )
        self.listen_operation.create_table()
        self.listen_scheduler = AsyncListenDataScheduler(self.listen_operation)
        self.task_scheduler = AsyncTaskScheduler(self.queue_operation, task_thread_num)
        self.cleanup_scheduler = CleanupScheduler(self.queue_operation)

    def send_message(self, message: MessageItem, callback: Callable):
        self.receive_scheduler.send_message(message, callback)

    def update_listen_data(self, key, value):
        self.listen_operation.update_listen_data(key, value)

    def get_listen_datas(self):
        return self.listen_operation.get_values()

    def get_listen_data(self, key):
        return self.listen_operation.get_value(key)

    def start(self):
        self.receive_scheduler.start_receive_thread()
        self.task_scheduler.start_task_thread()

    def stop(self):
        self.receive_scheduler.stop_receive_thread()
        self.task_scheduler.stop_task_thread()


__all__ = ["AsyncQueueScheduler"]
