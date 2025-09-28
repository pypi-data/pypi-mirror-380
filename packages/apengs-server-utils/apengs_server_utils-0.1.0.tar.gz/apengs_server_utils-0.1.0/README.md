# apengs-dash-components

一个包含实用工具函数的辅助库，提供时间格式化、连接数据库、访问Window命令行执行等功能，主要用于个人使用。

## 安装
```bash
pip install apengs-server-utils

# apengs-server-utils

一个高效的数据库操作工具库，封装了 MySQL 和 DuckDB 的常用操作，支持跨数据库数据同步、批量数据处理及智能缓存机制，大幅简化后端开发中的数据库交互流程。


## 功能特点

- **MySQL 核心能力**：封装查询、批量写入、DataFrame 导入、冲突更新（`ON DUPLICATE KEY UPDATE`）等高频操作
- **DuckDB 完整支持**：兼容内存/文件两种运行模式，提供表创建、数据增删改查、结构查询等全生命周期 API
- **跨库增量同步**：实现 MySQL 与 DuckDB 双向数据同步，支持单主键与复合主键场景
- **智能缓存机制**：自动缓存查询结果，可配置缓存有效期，减少重复数据库请求
- **类型自动推断**：根据 pandas.DataFrame 数据类型，自动生成匹配的数据库表结构
- **冲突安全处理**：支持 MySQL 冲突更新、DuckDB 冲突覆盖，避免数据写入异常


## 安装方法

通过 PyPI 直接安装（Python 3.7+ 兼容）：

```bash
pip install apengs-server-utils
```


## 快速使用示例

### 1. MySQL 基础操作

```python
from apengs_server_utils import db
import pandas as pd

# 1. 获取 MySQL 连接（默认使用配置中的 SQLCON1 连接信息）
mysql_conn, mysql_engine = db()

# 2. 执行查询（返回格式：(列名元组, 数据行1, 数据行2, ...)）
query_result = mysql_conn.ExecQuery("SELECT id, name, age FROM users LIMIT 5")
columns = query_result[0]  # 获取列名：('id', 'name', 'age')
data_rows = query_result[1:]  # 获取数据行：((1, 'Alice', 25), (2, 'Bob', 30), ...)

# 3. 批量执行非查询 SQL（INSERT/UPDATE/DELETE）
sql_list = [
    "INSERT INTO logs (operate_user, content) VALUES ('admin', '系统启动')",
    "UPDATE users SET age = 26 WHERE id = 1"
]
execute_status = mysql_conn.ExecNonQuery(sql_list)  # 成功返回1，失败返回0

# 4. 导入 DataFrame 到 MySQL 表（自动处理字段匹配与冲突）
df = pd.DataFrame({
    "id": [3, 4],
    "name": ["Charlie", "Diana"],
    "age": [28, 24]
})
mysql_conn.dat2db(df, "users")  # 自动生成冲突更新 SQL
```


### 2. DuckDB 基础操作

```python
from apengs_server_utils import get_duckdb_conn
import pandas as pd

# 1. 创建 DuckDB 连接（内存模式：":memory:"，文件模式：指定路径如 "data.duckdb"）
duck_conn = get_duckdb_conn(db_path="sales_data.duckdb")

# 2. 创建表（手动指定 schema）
schema = {
    "order_id": "BIGINT",
    "order_date": "TIMESTAMP",
    "amount": "DOUBLE",
    "status": "VARCHAR"
}
duck_conn.create_table("sales", schema)

# 3. 插入 DataFrame 数据
df = pd.DataFrame({
    "order_id": [1001, 1002],
    "order_date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
    "amount": [599.9, 899.5],
    "status": ["paid", "unpaid"]
})
insert_result = duck_conn.dat2db(df, "sales")  # 返回插入结果描述

# 4. 执行查询
query_df = duck_conn.execute_query(
    "SELECT order_id, amount FROM sales WHERE status = 'paid'"
)

# 5. 更新与删除数据
duck_conn.update_data(
    table_name="sales",
    set_clause="status = 'paid'",
    where_clause="WHERE order_id = 1002"
)
duck_conn.delete_data(
    table_name="sales",
    where_clause="WHERE amount < 100"
)

# 6. 查看表结构与数据量
table_schema = duck_conn.get_table_info("sales")  # 返回表结构 DataFrame
record_count = duck_conn.get_table_count("sales")  # 返回表记录数

# 7. 关闭连接
duck_conn.close()
```


### 3. MySQL 与 DuckDB 双向同步

```python
from apengs_server_utils import db, get_duckdb_conn

# 1. 初始化连接
mysql_conn, _ = db()
duck_conn = get_duckdb_conn()

# 2. 从 MySQL 增量同步数据到 DuckDB（支持复合主键）
# 场景：同步 sales 表，以 (order_id, order_date) 为复合主键，缓存有效期 15 分钟
duck_conn.load_from_mysql(
    mysql_instance=mysql_conn,
    sql="SELECT order_id, order_date, amount, status FROM sales",
    table_name="sales_duck",
    primary_key=["order_id", "order_date"],  # 复合主键
    cache_minutes=15,
    force_refresh=False  # 不强制刷新（优先使用缓存）
)

# 3. 在 DuckDB 中处理数据（示例：计算每日销售额）
daily_sales_df = duck_conn.execute_query("""
    SELECT DATE(order_date) AS sale_date, SUM(amount) AS total_sales
    FROM sales_duck
    GROUP BY sale_date
""")

# 4. 将处理结果同步回 MySQL（增量写入，避免重复）
# 先创建 MySQL 目标表（若不存在）
mysql_conn.ExecNonQuery([
    """
    CREATE TABLE IF NOT EXISTS daily_sales (
        sale_date DATE PRIMARY KEY,
        total_sales DOUBLE
    )
    """
])
# 增量同步 DuckDB 数据到 MySQL
duck_conn.sync_to_mysql(
    mysql_instance=mysql_conn,
    table_name="daily_sales",  # DuckDB 源表
    mysql_table_name="daily_sales",  # MySQL 目标表
    primary_key="sale_date"  # MySQL 表主键
)

# 5. 关闭连接
duck_conn.close()
mysql_conn.close()
```


## 核心 API 文档

### 1. MySQL 类（`MYSQL`）

| 方法名 | 功能描述 | 参数说明 | 返回值 |
|--------|----------|----------|--------|
| `__init__(host, user, pwd, db)` | 初始化 MySQL 连接参数 | `host`: 数据库地址<br>`user`: 用户名<br>`pwd`: 密码<br>`db`: 数据库名 | - |
| `ExecQuery(sql)` | 执行查询 SQL | `sql`: 查询语句（字符串） | 元组：`(列名元组, 数据行1, 数据行2, ...)` |
| `ExecNonQuery(sqlList)` | 批量执行非查询 SQL | `sqlList`: SQL 语句列表 | 整数：`1`（成功）/ `0`（失败） |
| `dat2db(dat, tb)` | 导入 DataFrame 到表 | `dat`: 待导入 DataFrame<br>`tb`: 目标表名 | 执行的 SQL 语句（字符串） |
| `datUpdateDB(dat, table, oncol, keycol, cond="1=1")` | 数据更新合并 | `dat`: 待合并 DataFrame<br>`table`: 目标表名<br>`oncol`: 关联字段列表<br>`keycol`: 主键字段列表<br>`cond`: 筛选条件 | 合并后的 DataFrame |
| `update_insert_sql(table, column, value)` | 生成冲突更新 SQL | `table`: 表名<br>`column`: 字段列表<br>`value`: values 字符串列表 | 完整 SQL 语句（字符串） |


### 2. DuckDB 封装类（`DuckDBWrapper`）

| 方法名 | 功能描述 | 参数说明 | 返回值 |
|--------|----------|----------|--------|
| `__init__(db_path=":memory:", auto_sync=False)` | 初始化 DuckDB 连接 | `db_path`: 数据库路径（`:memory:` 为内存模式）<br>`auto_sync`: 是否自动同步到文件 | - |
| `load_from_mysql(...)` | 从 MySQL 增量加载数据 | 见「快速使用示例 3」 | 加载的 DataFrame |
| `save_to_file(file_path)` | 保存内存数据库到文件 | `file_path`: 目标文件路径 | 布尔值：`True`（成功）/ `False`（失败） |
| `load_from_file(file_path)` | 从文件加载数据库 | `file_path`: 源文件路径 | 布尔值：`True`（成功）/ `False`（失败） |
| `execute_query(sql)` | 执行查询 SQL | `sql`: 查询语句 | 结果 DataFrame |
| `execute_non_query(sql)` | 执行非查询 SQL | `sql`: 非查询语句（INSERT/UPDATE/DELETE 等） | 布尔值：`True`（成功）/ `False`（失败） |
| `create_table(table_name, schema_dict, if_not_exists=True)` | 创建表 | `table_name`: 表名<br>`schema_dict`: 字段-类型字典<br>`if_not_exists`: 是否忽略已存在表 | 布尔值：`True`（成功）/ `False`（失败） |
| `dat2db(dat, tb)` | 导入 DataFrame 到表 | `dat`: 待导入 DataFrame<br>`tb`: 目标表名 | 插入结果描述（字符串） |
| `sync_to_mysql(...)` | 同步数据到 MySQL | 见「快速使用示例 3」 | 布尔值：`True`（成功）/ `False`（失败） |
| `table_exists(table_name)` | 检查表是否存在 | `table_name`: 表名 | 布尔值：`True`（存在）/ `False`（不存在） |
| `get_table_info(table_name)` | 获取表结构 | `table_name`: 表名 | 表结构 DataFrame（含字段名、类型等） |
| `get_table_count(table_name)` | 获取表记录数 | `table_name`: 表名 | 整数：表记录数 |
| `drop_table(table_name)` | 删除表 | `table_name`: 表名 | 布尔值：`True`（成功）/ `False`（失败） |
| `close()` | 关闭数据库连接 | - | - |

## 注意事项

1. **主键与唯一索引**：使用增量同步（`load_from_mysql`/`sync_to_mysql`）时，目标表必须存在主键或唯一索引，否则无法触发冲突更新逻辑。
2. **数据类型兼容性**：确保 MySQL 与 DuckDB 之间的字段类型匹配（如 MySQL 的 `INT` 对应 DuckDB 的 `BIGINT`，`DATETIME` 对应 `TIMESTAMP`）。
3. **内存模式风险**：DuckDB 内存模式（`db_path=":memory:"`）下，数据在程序退出后会丢失，需通过 `save_to_file` 手动持久化。
4. **大批量数据处理**：导入/同步超大规模 DataFrame 时，建议分批次处理，避免内存溢出。
5. **配置修改**：默认 MySQL 连接配置（`SQLCON1`）需根据实际环境修改，建议在生产环境中通过环境变量注入敏感信息（如密码）。

## ChineseCalendar —— 中国日历“工作日 / 休息日”查询器
## 一、一句话职责

给定一份“日期→是否工作日”清单（JSON 文件或 SQL 结果），提供以下能力：

1. 拿到全年所有休息日列表（含周末、节假日、调休）
2. 计算任意两段日期之间的工作日天数（左闭右闭）

## 二、支持的输入方式

- **方式 A**：本地 JSON 文件（推荐离线场景）
- **方式 B**：SQL 查询（推荐在线场景，表结构见下）

## 三、JSON / SQL 必需字段

| 字段含义       | 本类默认列名（可自定义）         | 类型      | 取值说明                     |
|----------------|-------------------------------|-----------|------------------------------|
| 日期           | `日期`                         | `str`     | `"2025-10-01"`               |
| 是否工作日     | `是否工作日`    | `str/int` | `"0"`=休息日，`"1"`=工作日   |

> 其他列可任意存在，会被忽略。

## 四、快速上手（90% 场景够用）

```python
import datetime
from apengs_server_utils import ChineseCalendar

# 1. 载入日历（JSON 为例）
cal = ChineseCalendar(source="project/_files/chinese-calendarWorkDay.json")

# 2. 取休息日
holidays = cal.get_holiday_list()          # -> ["2025-01-01", "2025-01-02", ...]

# 3. 算工作日
days = cal.count_workdays("2025-10-01", "2025-10-31")  # -> 18
```

## 版本历史

| 版本号 | 发布日期 | 更新内容 |
|--------|----------|----------|
| v0.1.0 | 2025-09-26 | 初始版本：<br>- 实现 MySQL 基础操作封装<br>- 实现 DuckDB 基础操作封装<br>- 支持单主键跨库同步 |
