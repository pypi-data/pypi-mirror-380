#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   task_cycle.py
@Time    :   2025-09-27 16:59:31
@Author  :   chakcy
@Email   :   947105045@qq.com
@description   :   任务周期模块
"""


from ..model import MessageItem
from typing import Callable, Optional
from ..constant import MessageStatus
import json

import functools
import time


def retry_sync(max_retries=3, delay=1):
    """
    同步重试装饰器

    Args:
        max_retries: 最大重试次数
        delay: 重试间隔（秒）
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            last_exception = None
            # 使用message_item中的retry_count作为最大重试次数
            retries = getattr(self.message_item, "retry_count", max_retries)

            # 至少尝试一次（retries+1），最多尝试max_retries+1次
            actual_retries = min(retries, max_retries) if max_retries > 0 else retries

            for attempt in range(actual_retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < actual_retries:
                        time.sleep(delay)
                    else:
                        break

            # 如果没有捕获到异常，则创建一个新的异常
            if last_exception is not None:
                raise last_exception
            else:
                raise Exception("Unknown error occurred during sync task execution")

        return wrapper

    return decorator


class TaskCycle:
    def __init__(self, message_item: MessageItem, callback: Optional[Callable]):
        self.message_item = message_item
        self.callback = callback
        self.task_result = None
        self.task_status = None
        self.task_error = None

    @retry_sync(max_retries=3, delay=1)
    def run(self):
        try:
            task_result = self.callback(self.message_item)  # type: ignore
        except Exception as e:
            self.task_result = None
            self.task_status = MessageStatus.FAILED
            self.task_error = str(e)
        else:
            self.task_result = task_result  # type: ignore
            self.task_status = MessageStatus.COMPLETED
            self.task_error = None

    def get_task_result(self):
        if isinstance(self.task_result, (dict, list)):
            try:
                return json.dumps(self.task_result)
            except:
                return json.dumps({"result": str(self.task_result)})

        elif isinstance(self.task_result, str):
            try:
                json.loads(self.task_result)
                return self.task_result
            except:
                return json.dumps({"result": self.task_result})
        elif isinstance(self.task_result, (int, float, bool)):
            return json.dumps({"result": self.task_result})
        elif self.task_result is None:
            return "null"
        else:
            return json.dumps({"result": str(self.task_result)})

    def get_task_status(self):
        return self.task_status

    def get_task_error(self):
        return self.task_error

    def get_task_message_item(self):
        return self.message_item

    def get_task_callback(self):
        return self.callback
