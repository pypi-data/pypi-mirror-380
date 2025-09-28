#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   to_json_utils.py
@Time    :   2025-09-27 16:36:18
@Author  :   chakcy
@Email   :   947105045@qq.com
@description   :   xxxxxxxxx
"""

import sqlite3
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime


class SQLiteToJSONConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite 表转 JSON 工具")
        self.root.geometry("800x600")

        # 变量
        self.db_path = tk.StringVar()
        self.tables = []
        self.selected_table = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # type: ignore

        # 数据库选择部分
        db_frame = ttk.LabelFrame(main_frame, text="数据库选择", padding="5")
        db_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)  # type: ignore

        ttk.Entry(db_frame, textvariable=self.db_path, width=70).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(db_frame, text="浏览", command=self.browse_db).grid(
            row=0, column=1, padx=5
        )
        ttk.Button(db_frame, text="连接", command=self.connect_db).grid(
            row=0, column=2, padx=5
        )

        # 表选择部分
        table_frame = ttk.LabelFrame(main_frame, text="表选择", padding="5")
        table_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)  # type: ignore

        ttk.Label(table_frame, text="选择表:").grid(row=0, column=0, sticky=tk.W)
        self.table_combo = ttk.Combobox(
            table_frame, textvariable=self.selected_table, state="readonly"
        )
        self.table_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)  # type: ignore
        ttk.Button(table_frame, text="加载数据", command=self.load_table_data).grid(
            row=0, column=2, padx=5
        )

        # 数据显示部分
        data_frame = ttk.LabelFrame(main_frame, text="表数据", padding="5")
        data_frame.grid(
            row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5  # type: ignore
        )

        # 创建Treeview显示数据
        columns = ("#0",)
        self.tree = ttk.Treeview(data_frame, columns=columns, show="headings")
        vsb = ttk.Scrollbar(data_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(data_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # type: ignore
        vsb.grid(row=0, column=1, sticky=(tk.N, tk.S))  # type: ignore
        hsb.grid(row=1, column=0, sticky=(tk.W, tk.E))  # type: ignore

        # 按钮部分
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="导出为JSON", command=self.export_to_json).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(button_frame, text="清空", command=self.clear_all).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(button_frame, text="退出", command=self.root.quit).pack(
            side=tk.LEFT, padx=5
        )

        # 配置权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        data_frame.columnconfigure(0, weight=1)
        data_frame.rowconfigure(0, weight=1)

    def browse_db(self):
        file_path = filedialog.askopenfilename(
            title="选择SQLite数据库文件",
            filetypes=[
                ("SQLite数据库", "*.db *.sqlite *.sqlite3"),
                ("所有文件", "*.*"),
            ],
        )
        if file_path:
            self.db_path.set(file_path)

    def connect_db(self):
        if not self.db_path.get():
            messagebox.showerror("错误", "请先选择数据库文件")
            return

        try:
            conn = sqlite3.connect(self.db_path.get())
            cursor = conn.cursor()

            # 获取所有表名
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.tables = [table[0] for table in cursor.fetchall()]

            self.table_combo["values"] = self.tables
            if self.tables:
                self.selected_table.set(self.tables[0])

            conn.close()
            messagebox.showinfo(
                "成功", f"成功连接到数据库，找到 {len(self.tables)} 个表"
            )

        except sqlite3.Error as e:
            messagebox.showerror("数据库错误", f"连接数据库时出错: {str(e)}")

    def load_table_data(self):
        if not self.selected_table.get():
            messagebox.showerror("错误", "请先选择表")
            return

        try:
            conn = sqlite3.connect(self.db_path.get())
            conn.row_factory = sqlite3.Row  # 这样可以使用列名访问数据
            cursor = conn.cursor()

            # 获取表数据
            cursor.execute(f"SELECT * FROM {self.selected_table.get()}")
            rows = cursor.fetchall()

            # 清空Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # 设置列
            columns = [description[0] for description in cursor.description]
            self.tree["columns"] = columns
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100, minwidth=50)

            # 添加数据
            for row in rows:
                self.tree.insert("", "end", values=tuple(row))

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror("数据库错误", f"加载数据时出错: {str(e)}")

    def export_to_json(self):
        if not self.selected_table.get():
            messagebox.showerror("错误", "请先选择表")
            return

        # 选择保存位置
        file_path = filedialog.asksaveasfilename(
            title="保存JSON文件",
            defaultextension=".json",
            filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")],
        )

        if not file_path:
            return

        try:
            conn = sqlite3.connect(self.db_path.get())
            conn.row_factory = sqlite3.Row  # 使用列名访问数据
            cursor = conn.cursor()

            # 获取表数据
            cursor.execute(f"SELECT * FROM {self.selected_table.get()}")
            rows = cursor.fetchall()

            # 转换为字典列表
            result = [dict(row) for row in rows]

            # 写入JSON文件
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4, ensure_ascii=False)

            conn.close()
            messagebox.showinfo("成功", f"数据已成功导出到 {file_path}")

        except sqlite3.Error as e:
            messagebox.showerror("数据库错误", f"导出数据时出错: {str(e)}")
        except Exception as e:
            messagebox.showerror("错误", f"保存文件时出错: {str(e)}")

    def clear_all(self):
        self.db_path.set("")
        self.tables = []
        self.table_combo["values"] = []
        self.selected_table.set("")
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ("#0",)


if __name__ == "__main__":
    root = tk.Tk()
    app = SQLiteToJSONConverter(root)
    root.mainloop()
