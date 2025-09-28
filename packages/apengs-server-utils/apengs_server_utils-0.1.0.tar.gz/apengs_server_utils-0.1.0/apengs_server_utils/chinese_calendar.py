# -*- coding: utf-8 -*-
import json
import datetime
from typing import List, Dict, Optional, Union
from pathlib import Path

import pandas as pd


class ChineseCalendar:
    """
    中国日历工具：基于“日期-是否工作日”数据，提供休息日列表与工作日计数功能。

    支持从本地 JSON 文件或数据库 SQL 查询加载数据。
    数据格式要求：每条记录包含日期字段和工作日标志字段（0=非工作日，1=工作日）。

    默认字段映射：
        - "date" -> "日期"
        - "work_flag" -> "是否工作日（0：否，1：是）"

    Examples:
        >>> cal = ChineseCalendar(source="holidays.json")
        >>> holidays = cal.get_holiday_list()
        >>> workdays = cal.count_workdays("2024-01-01", "2024-01-31")

        >>> from sqlalchemy import create_engine
        >>> engine = create_engine("sqlite:///calendar.db")
        >>> cal = ChineseCalendar(
        ...     sql="SELECT date_col, is_work FROM calendar",
        ...     conn=engine,
        ...     field_map={"date": "date_col", "work_flag": "is_work"}
        ... )
    """

    # 默认字段映射（兼容旧数据）
    DEFAULT_MAP = {
        "date": "日期",
        "work_flag": "是否工作日",
    }

    def __init__(
        self,
        source: Union[str, Path, None] = None,  # JSON 文件路径
        sql: Optional[str] = None,  # 直接 SQL 查询
        conn=None,  # SQLAlchemy connectable
        field_map: Optional[Dict[str, str]] = None,  # 自定义字段映射
    ):
        """
        初始化中国日历工具。

        Args:
            source (str or Path, optional): 本地 JSON 文件路径，包含日期与工作日标志数据。
            sql (str, optional): SQL 查询语句，用于从数据库获取数据。
            conn: SQLAlchemy 可连接对象（如 Engine 或 Connection），当使用 sql 时必须提供。
            field_map (dict, optional): 自定义字段映射，键为内部字段名（"date", "work_flag"），
                                        值为数据源中的实际列名。

        Raises:
            ValueError: 当未提供 source 或 sql，或使用 sql 但未提供 conn 时抛出。

        Note:
            - 必须指定 source 或 sql 中的一个。
            - JSON 文件应为列表格式，每项为字典，例如：
              [{"日期": "2024-01-01", "是否工作日（0：否，1：是）": 0}, ...]
        """
        self.field_map = self.DEFAULT_MAP | (field_map or {})
        self._holiday_set: set[str] = set()

        if sql:
            if conn is None:
                raise ValueError("使用 SQL 时必须传入 conn（SQLAlchemy connectable）")
            df = pd.read_sql(sql, conn)
            self._load_from_df(df)
        elif source:
            self._load_from_file(source)
        else:
            raise ValueError("必须指定 source 文件路径 或 sql 查询语句")

    # ---------- 内部载入 ----------
    def _load_from_file(self, path: Union[str, Path]):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        self._load_from_records(data)

    def _load_from_df(self, df: pd.DataFrame):
        self._load_from_records(df.to_dict(orient="records"))

    def _load_from_records(self, records: List[dict]):
        date_key = self.field_map["date"]
        flag_key = self.field_map["work_flag"]
        for row in records:
            if str(row[flag_key]) == "0":  # 0 代表非工作日
                self._holiday_set.add(str(row[date_key]))
        # 去重 & 排序，方便调试
        self._holiday_set = set(sorted(self._holiday_set))

    # ---------- 对外 API ----------
    def get_holiday_list(self) -> List[str]:
        """
        获取所有非工作日（休息日）列表，包括周末、法定节假日及调休日。

        Returns:
            List[str]: 日期字符串列表，格式为 "YYYY-MM-DD"，按字典序排序。
        """
        return list(self._holiday_set)

    def count_workdays(self, begin_date: str, end_date: str) -> int:
        """
        统计闭区间 [begin_date, end_date] 内的工作日天数。

        Args:
            begin_date (str): 起始日期，格式 "YYYY-MM-DD"。
            end_date (str): 结束日期，格式 "YYYY-MM-DD"。

        Returns:
            int: 区间内的工作日数量（总天数减去非工作日数量）。

        Note:
            - 若 begin_date > end_date，会自动交换两者。
            - 仅依赖已加载的非工作日数据，不自动判断周末（需数据中已包含）。
        """
        begin = datetime.datetime.strptime(begin_date, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        if begin > end:
            begin, end = end, begin

        total_days = (end - begin).days + 1
        holiday_in_range = 0
        for i in range(total_days):
            day = begin + datetime.timedelta(days=i)
            if day.isoformat() in self._holiday_set:
                holiday_in_range += 1
        return total_days - holiday_in_range


# ---------- 快捷函数（保持旧接口风格） ----------
def read_chinese_calendar(file: Union[str, Path, None] = None) -> List[str]:
    """兼容老函数：仅返回休息日列表"""
    return ChineseCalendar(
        source=file or "project/_files/chinese-calendarWorkDay.json"
    ).get_holiday_list()


def get_workdays(
    begin_date: str, end_date: str, file: Union[str, Path, None] = None
) -> int:
    """兼容老函数：返回工作日天数"""
    cal = ChineseCalendar(source=file or "project/_files/chinese-calendarWorkDay.json")
    return cal.count_workdays(begin_date, end_date)
