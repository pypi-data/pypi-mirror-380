#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   listen_operation.py
@Time    :   2025-09-27 17:02:18
@Author  :   chakcy
@Email   :   947105045@qq.com
@description   :   监听操作模块
"""


from ..mounter.listen_mounter import ListenMounter
import sqlite3
from typing import List, Tuple, Union


class ListenOperation:
    def __init__(self, db_dir):
        self.db_dir = db_dir
        self.listen_fields = ListenMounter.get_Listener_list()
        self.create_table()

    def _get_connection(self):
        """获取数据库连接"""
        return sqlite3.connect(
            self.db_dir,
            check_same_thread=False,
        )

    def create_table(self):
        if len(self.listen_fields) == 0:
            return
        conn = self._get_connection()

        # 分别执行每个SQL语句而不是使用executescript
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS listen_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key Text,
                value JSON
            )
        """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS change_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                table_name TEXT,
                row_id INTEGER,
                column_name TEXT,
                old_value TEXT,
                new_value TEXT,
                is_delete integer DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # 检查触发器是否已存在，如果不存在则创建
        try:
            conn.execute(
                """
                CREATE TRIGGER IF NOT EXISTS track_value_change
                AFTER UPDATE OF value ON listen_table
                FOR EACH ROW
                WHEN OLD.value <> NEW.value
                BEGIN
                    INSERT INTO change_log (table_name, row_id, column_name, old_value, new_value)
                    VALUES ('listen_table', NEW.id, 'key', OLD.key, NEW.key);
                END
            """
            )
        except sqlite3.Error:
            # 如果触发器创建失败，我们继续执行其他操作
            pass

        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA cache_size=-20000;")
        conn.execute("PRAGMA mmap_size=1073741824;")
        conn.execute("PRAGMA temp_store=MEMORY;")
        conn.execute("PRAGMA busy_timeout=5000;")
        conn.commit()

        for listen_field in self.listen_fields:
            sql = """
                INSERT INTO 
                    listen_table (key, value)
                VALUES 
                    (?, ?)
            """
            conn.execute(sql, (listen_field, "null"))
            conn.commit()

    def listen_data(self) -> Tuple[bool, Union[List[Tuple], str]]:
        sql = f"""
            SELECT * FROM change_log where is_delete = 0 ORDER BY id DESC LIMIT 100
        """
        conn = self._get_connection()
        result = conn.execute(sql).fetchall()
        if len(result) == 0:
            return False, "No data found"
        return True, result

    def delete_change_log(self, delete_id):
        sql = f"""
            DELETE FROM change_log WHERE id = {delete_id}
        """
        conn = self._get_connection()
        conn.execute(sql)

    def update_listen_data(self, key, value):
        sql = f"""
            UPDATE listen_table SET value = '{value}' WHERE key = '{key}'
        """
        conn = self._get_connection()
        conn.execute(sql)
        conn.commit()

    def get_value(self, key):
        sql = f"""
            SELECT value FROM listen_table WHERE key = '{key}'
        """
        conn = self._get_connection()
        result = conn.execute(sql).fetchone()
        if result is None:
            return None
        return result[0]

    def get_values(self):
        sql = f"""
            SELECT key, value FROM listen_table
        """
        conn = self._get_connection()
        result = conn.execute(sql).fetchall()
        return result
