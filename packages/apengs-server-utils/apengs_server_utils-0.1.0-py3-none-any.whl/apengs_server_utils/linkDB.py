import re
import pymysql
import pandas
import sqlalchemy
from datetime import datetime, timedelta
import duckdb
import os


class MYSQL:
    """
    MySQL 数据库连接与操作封装类

    支持：
      - 查询（ExecQuery）
      - 批量写入（ExecNonQuery）
      - DataFrame 导入（dat2db）
      - ON DUPLICATE KEY UPDATE 写入（支持复合主键）
      - 数据更新合并（datUpdateDB）

    依赖 pymysql + sqlalchemy
    """

    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        engineStr = f"mysql+pymysql://{self.user}:{self.pwd}@{self.host}:3306/{self.db}"
        self.EE = sqlalchemy.create_engine(engineStr)

    def __GetConnect(self):
        if self.db:
            # noinspection PyBroadException
            try:
                self.conn = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.pwd,
                    database=self.db,
                    use_unicode=True,
                    charset="utf8",
                )
            except Exception as e:
                exit("Don't a MySQL or MSSQL database.")
        else:
            exit("No database.")
        cur = self.conn.cursor()
        if not cur:
            exit("Error connect")
        else:
            return cur

    @staticmethod
    def tidySQL(sql):
        # sql = re.sub(r'\n\s*--sql\s*\n', ' ', sql) # 替换掉注释
        sql = re.sub(r"\s*\n\s*", " ", sql)  # 替换掉换行前后的空白
        return sql

    def ExecQuery(self, sql):
        """执行查询语句

        Args:
            sql(str) : 一条查询命令

        """
        cur = self.__GetConnect()
        cur.execute(sql)
        res = cur.fetchall()
        res_columns = ([i[0] for i in cur.description],)
        res = res_columns + res  ##res的第0个元素是标题。
        self.conn.close()
        return res

    def ExecNonQuery(self, sqlList):
        """执行修改语句

        Args:
            sql (list): 一组修改命令

        Returns:
            str: 成功1, 失败0.
        """
        cur = self.__GetConnect()
        ok = 0
        # noinspection PyBroadException
        try:
            [cur.execute(i) for i in sqlList]
            self.conn.commit()
            ok = 1
        except Exception as e:
            self.conn.rollback()
        self.conn.close()
        return ok

    @staticmethod
    def update_insert_sql(table, column, value):
        """
        table : 'table name'
        column: ['c1','c2','c3']
        value : ["(1,'2','a')","(2,'3','b')"]
        NOTES : `ON DUPLICATE KEY UPDATE`, UNIQUE INDEX is necessary.
        """
        sql_col = [f"`{i}`" for i in column]
        sql_val = ",\n".join(value)
        sql = f"""
            INSERT INTO {table}({",".join([_ for _ in sql_col])}) 
            VALUE  {sql_val}
            ON DUPLICATE KEY UPDATE {",".join([_ + "=VALUES(" + _ + ")" for _ in sql_col])}
        """
        sql = re.sub(r"\s*\n\s*", "\n", sql)  ##tidy
        return sql

    def dat2db(self, dat, tb):
        """将dataFrame格式数据导入数据库表tb，默认数据库链接。

        Args:
            dat (objct): dataframe
            tb (str):  tb name
            con (object) : 数据库连接

        Returns:
            str: 执行的sql
        """
        dat = dat.fillna("")
        dat = dat.dropna(axis="columns", how="all")
        dat = dat.applymap(lambda x: str(x))
        # 再出数据以前更新DAT列以匹配数据库列
        dbcol = set(self.ExecQuery(f"SELECT * FROM {tb} LIMIT 1")[0])
        dat = dat[dbcol.intersection(dat.columns)]
        # END
        sqlValue = []
        for _, e in dat.iterrows():
            ival = "('" + e[0] + "','" + "','".join(e[1:]) + "')"
            sqlValue.append(ival)
        sql = self.update_insert_sql(tb, list(dat.columns), sqlValue)
        self.ExecNonQuery([sql])
        return sql

    def datUpdateDB(self, dat, table, oncol, keycol, cond="1=1"):
        """数据dat更新到table。

        Args:
            dat (df): pandas 数据表
            table (str): 需要更新到的表名
            keycol (list): 表的关键字列表[index key list]
            ee (object) : 数据库连接方式2
            cond (str): 更新过程指定数据行的条件

        Returns:
            df: 更新到数据库的数据表
        """
        select_col = str(keycol)[1:-1].replace("'", "`")
        sql = f"""
            SELECT {select_col}
            FROM {table}
            WHERE {cond}
        """
        datDB = pandas.read_sql(sql, self.EE)
        datDBdropCol = [
            i for i in datDB.columns if (i not in oncol) and (i in dat.columns)
        ]  # * 依上传表格为准。
        datDB.drop(datDBdropCol, inplace=True, axis=1)
        dat = pandas.merge(dat, datDB, how="left", on=oncol)
        self.dat2db(dat, table)
        return dat


# 完整的DuckDB Wrapper类
class DuckDBWrapper:
    def __init__(self, db_path=":memory:", auto_sync=False):
        """
        初始化DuckDB连接

        Args:
            db_path: DuckDB文件路径，':memory:'表示内存模式
            auto_sync: 是否自动同步到文件（当使用文件模式时）
        """
        self.db_path = db_path
        self.auto_sync = auto_sync
        self.conn = duckdb.connect(database=db_path)
        self.cache_time = {}  # 缓存时间记录
        self.cache_data = {}  # 缓存的数据框
        self.loaded_tables = set()  # 已经加载的表

    @staticmethod
    def _infer_schema(df):
        """
        根据 DataFrame 自动推断 DuckDB 表结构

        Args:
            df (pd.DataFrame): 输入数据

        Returns:
            dict: {列名: DuckDB 类型}
        """
        schema = {}
        for col in df.columns:
            # 基础类型推断
            if pandas.api.types.is_integer_dtype(df[col]):
                schema[col] = "BIGINT"
            elif pandas.api.types.is_float_dtype(df[col]):
                schema[col] = "DOUBLE"
            elif pandas.api.types.is_bool_dtype(df[col]):
                schema[col] = "BOOLEAN"
            elif pandas.api.types.is_datetime64_any_dtype(df[col]):
                schema[col] = "TIMESTAMP"
            else:
                # 默认使用 VARCHAR，可扩展 TEXT 或 BLOB
                schema[col] = "VARCHAR"
        return schema

    @staticmethod
    def _format_pk_value(val):
        """格式化主键值，支持 NULL 和字符串转义"""
        if val is None or pandas.isna(val):
            return "NULL"
        else:
            # 转义单引号，确保 SQL 安全
            s = str(val).replace("'", "''")
            return f"'{s}'"

    def load_from_mysql(
        self,
        mysql_instance,
        sql,
        table_name,
        force_refresh=False,
        cache_minutes=10,
        primary_key=None,
    ):
        """
        从 MySQL 增量加载数据到 DuckDB（支持复合主键）

        🔄 增量逻辑：
        - 若表不存在 → 创建表 + 全量导入
        - 若有主键且表存在 → 仅导入 MySQL 中新增主键记录
        - 若无主键或强制刷新 → 清空表后全量导入

        🧠 缓存机制：
        - 自动缓存 DataFrame 和加载时间
        - 在 cache_minutes 内重复调用直接返回缓存

        Args:
            mysql_instance (MYSQL): 已初始化的 MySQL 实例
            sql (str): SELECT 查询语句（如 "SELECT id,name FROM users"）
            table_name (str): DuckDB 中目标表名
            force_refresh (bool): 忽略缓存，强制重新加载
            cache_minutes (int): 缓存有效期（分钟），默认 10
            primary_key (str or list): 主键字段，用于增量同步。例: "id" 或 ["user_id", "date"]

        Returns:
            pd.DataFrame: 加载的数据（可能为空）

        Example:
            >>> duck.load_from_mysql(mysql, "SELECT * FROM sales", "sales", primary_key="id")
        """
        # 检查是否需要刷新缓存
        now = datetime.now()
        if not force_refresh and table_name in self.cache_time:
            last_load = self.cache_time[table_name]
            if now - last_load < timedelta(minutes=cache_minutes):
                print(f"使用缓存中的 {table_name}")
                return self.cache_data[table_name]

        # 处理复合主键（统一转为列表格式）
        if isinstance(primary_key, str):
            primary_key = [primary_key]
        has_compound_key = isinstance(primary_key, list) and len(primary_key) > 1

        # 增量同步逻辑（支持复合主键）
        incremental_sql = sql
        if primary_key and self.table_exists(table_name):
            # 获取DuckDB中已有的主键组合
            pk_columns = ", ".join(primary_key)
            duckdb_pk = self.execute_query(f"SELECT {pk_columns} FROM {table_name}")

            if not duckdb_pk.empty:
                # 生成主键组合条件（如 (id, version) NOT IN ((1,2), (3,4))）
                pk_tuples = [tuple(row) for _, row in duckdb_pk.iterrows()]
                pk_str = ", ".join(
                    [
                        "("
                        + ", ".join(DuckDBWrapper._format_pk_value(v) for v in t)
                        + ")"
                        for t in pk_tuples
                    ]
                )
                incremental_where = f" WHERE ({pk_columns}) NOT IN ({pk_str})"

                # 追加到原SQL（处理原SQL可能已有WHERE的情况）
                if "WHERE" in sql:
                    incremental_sql += f" AND ({pk_columns}) NOT IN ({pk_str})"
                else:
                    incremental_sql += incremental_where
                print(f"增量同步（复合主键）：加载新数据")

        # 从MySQL加载数据
        df = pandas.read_sql(incremental_sql, mysql_instance.EE)
        if df.empty:
            print(f"MySQL中无新数据（{table_name}）")
            return df

        # 自动创建表（复合主键场景需显式指定主键）
        if not self.table_exists(table_name):
            schema = self._infer_schema(df)
            self.create_table(table_name, schema)
            # 额外创建复合主键约束
            if primary_key:
                pk_str = ", ".join(primary_key)
                try:
                    self.execute_non_query(
                        f"ALTER TABLE {table_name} ADD PRIMARY KEY ({pk_str})"
                    )
                    print(f"✅ 已为表 {table_name} 添加主键约束: ({pk_str})")
                except Exception as e:
                    print(f"⚠️ 无法添加主键约束（请确保主键列非空且唯一）: {e}")
                    # 不中断流程，继续插入（但增量同步可能不准）
            print(f"已创建实体表 {table_name}（含复合主键）")

        # 写入DuckDB（全量/增量）
        if force_refresh or not primary_key:
            self.execute_non_query(f"DELETE FROM {table_name}")
            self.dat2db(df, table_name)
            print(f"全量同步完成，{table_name} 共 {len(df)} 行")
        else:
            self.dat2db(df, table_name)
            print(f"增量同步完成，新增 {len(df)} 行")

        # 更新缓存
        self.cache_time[table_name] = now
        self.cache_data[table_name] = df
        return df

    def save_to_file(self, file_path):
        """
        将当前DuckDB内容保存到文件（仅内存模式有效）
        """
        if self.db_path != ":memory:":
            print("ℹ️ 当前已是文件模式，无需保存")
            return True

        try:
            conn_temp = duckdb.connect(file_path)
            # 使用标准信息模式获取用户表
            tables = self.conn.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'main' AND table_type = 'BASE TABLE'
            """).fetchall()

            for (table_name,) in tables:
                df = self.execute_query(f"SELECT * FROM {table_name}")
                # 注册并创建表
                conn_temp.register(table_name, df)
                # 自动推断并创建表结构
                sample_row = df.iloc[0] if len(df) > 0 else None
                if sample_row is not None:
                    cols = []
                    for col in df.columns:
                        val = sample_row[col]
                        if isinstance(val, int):
                            cols.append(f"{col} BIGINT")
                        elif isinstance(val, float):
                            cols.append(f"{col} DOUBLE")
                        elif isinstance(val, bool):
                            cols.append(f"{col} BOOLEAN")
                        elif isinstance(val, (datetime, pandas.Timestamp)):
                            cols.append(f"{col} TIMESTAMP")
                        else:
                            cols.append(f"{col} VARCHAR")
                    create_sql = f"CREATE TABLE {table_name} ({', '.join(cols)})"
                    conn_temp.execute(create_sql)
                else:
                    # 空表，用 PRAGMA 推断结构
                    schema = self.get_table_info(table_name)
                    if schema is not None and not schema.empty:
                        cols = [
                            f"{row['name']} {row['type']}"
                            for _, row in schema.iterrows()
                        ]
                        create_sql = f"CREATE TABLE {table_name} ({', '.join(cols)})"
                        conn_temp.execute(create_sql)

                # 插入数据
                if not df.empty:
                    conn_temp.execute(
                        f"INSERT INTO {table_name} SELECT * FROM {table_name}"
                    )

            conn_temp.close()
            print(f"✅ 数据已保存到 {file_path}")
            return True
        except Exception as e:
            print(f"❌ 保存失败: {e}")
            return False

    def load_from_file(self, file_path):
        """
        从文件加载DuckDB内容
        """
        try:
            self.conn = duckdb.connect(database=file_path)
            self.db_path = file_path
            print(f"从文件加载数据: {file_path}")
            return True
        except Exception as e:
            print(f"加载失败: {e}")
            return False

    def execute_query(self, sql):
        """执行查询语句并返回结果"""
        return self.conn.execute(sql).fetchdf()

    def execute_non_query(self, sql):
        """执行非查询语句（INSERT, UPDATE, DELETE等）"""
        try:
            self.conn.execute(sql)
            return True
        except Exception as e:
            print(f"执行失败: {e}")
            return False

    def create_table(self, table_name, schema_dict, if_not_exists=True):
        """
        创建表
        schema_dict: {'column_name': 'type', ...}
        """
        columns = [f"{name} {dtype}" for name, dtype in schema_dict.items()]
        if_exists = "IF NOT EXISTS" if if_not_exists else ""
        sql = f"CREATE TABLE {if_exists} {table_name} ({', '.join(columns)})"
        return self.execute_non_query(sql)

    def dat2db(self, dat, tb):
        """
        将 pandas.DataFrame 数据高效批量插入 DuckDB 表（推荐方式）

        Args:
            dat (pd.DataFrame): 要插入的数据
            tb (str): 目标表名（必须已存在）

        Returns:
            str: 插入结果描述

        注意:
            - 表必须预先创建
            - 列名需匹配（自动过滤不存在的列）
            - 使用 DuckDB 内部注册机制，性能远优于拼接 VALUES
        """
        if dat.empty:
            return "No data to insert"
        # 数据预处理
        dat = dat.fillna("")
        dat = dat.dropna(axis="columns", how="all")
        dat = dat.applymap(lambda x: str(x))

        # 获取现有表的列名（如果表存在）
        if self.table_exists(tb):
            try:
                table_info = self.execute_query(f"PRAGMA table_info('{tb}')")
                existing_cols = set(table_info["name"].tolist())
                dat = dat[[col for col in dat.columns if col in existing_cols]]
            except Exception:
                pass  # 如果获取表结构失败，使用所有列

        if dat.empty:
            return "No matching columns to insert"

        # 注册 DataFrame 为临时视图（DuckDB 最佳实践）
        temp_view = f"temp_view_{id(dat)}"
        self.conn.register(temp_view, dat)

        # 构建 INSERT SELECT 语句
        columns = ", ".join(f'"{col}"' for col in dat.columns)
        sql = f'INSERT INTO "{tb}" SELECT {columns} FROM {temp_view}'

        try:
            self.conn.execute(sql)
            self.conn.unregister(temp_view)  # 清理临时视图
            return f"Inserted {len(dat)} rows into {tb}"
        except Exception as e:
            self.conn.unregister(temp_view)
            raise RuntimeError(f"Failed to insert data: {e}")

    def update_insert_sql(self, table, column, value):
        """
        类似MySQL的update_insert_sql方法
        """
        sql_col = [f'"{i}"' for i in column]
        sql_val = ",\n".join(value)
        sql = f"""
            INSERT INTO {table}({",".join([_ for _ in sql_col])}) 
            VALUES {sql_val}
            ON CONFLICT ({",".join([_ for _ in sql_col])}) 
            DO UPDATE SET {",".join([_ + "=EXCLUDED." + _ for _ in sql_col])}
        """
        return sql

    def insert_data(self, table_name, data):
        """
        简单插入数据（使用dat2db方法）
        """
        if isinstance(data, pandas.DataFrame):
            return self.dat2db(data, table_name)
        else:
            print("仅支持DataFrame类型数据")
            return None

    def update_data(self, table_name, set_clause, where_clause=""):
        """
        更新数据
        set_clause: "column1=value1, column2=value2"
        where_clause: "WHERE condition"
        """
        sql = f"UPDATE {table_name} SET {set_clause}"
        if where_clause:
            sql += f" {where_clause}"
        return self.execute_non_query(sql)

    def delete_data(self, table_name, where_clause=""):
        """
        删除数据
        where_clause: "WHERE condition"
        """
        sql = f"DELETE FROM {table_name}"
        if where_clause:
            sql += f" {where_clause}"
        return self.execute_non_query(sql)

    def table_exists(self, table_name):
        """检查表是否存在"""
        try:
            self.conn.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
            return True
        except Exception:
            return False

    def get_table_info(self, table_name):
        """获取表结构信息"""
        try:
            result = self.execute_query(f"PRAGMA table_info('{table_name}')")
            return result
        except Exception as e:
            print(f"获取表信息失败: {e}")
            return None

    def get_table_count(self, table_name):
        """获取表记录数"""
        try:
            result = self.execute_query(f"SELECT COUNT(*) as count FROM {table_name}")
            return int(result.iloc[0]["count"])
        except Exception as e:
            print(f"获取记录数失败: {e}")
            return 0

    def drop_table(self, table_name):
        """删除表"""
        sql = f"DROP TABLE IF EXISTS {table_name}"
        return self.execute_non_query(sql)

    def sync_to_mysql(
        self,
        mysql_instance,
        table_name,
        mysql_table_name=None,
        primary_key=None,  # 支持复合主键，如["id", "version"]
    ):
        """
        将 DuckDB 表数据增量同步到 MySQL（支持复合主键）

        🔄 增量逻辑：
        - 查询 MySQL 中已存在的主键组合
        - 从 DuckDB 中筛选出不存在于 MySQL 的记录
        - 调用 mysql_instance.dat2db 执行插入（支持 ON DUPLICATE KEY UPDATE）

        ⚠️ 要求：
        - MySQL 目标表必须有对应主键或唯一索引
        - 主键列在 DuckDB 和 MySQL 中名称和类型一致

        Args:
            mysql_instance (MYSQL): MySQL 连接实例
            table_name (str): DuckDB 源表名
            mysql_table_name (str): MySQL 目标表名（默认同名）
            primary_key (str or list): 主键字段

        Returns:
            bool: 是否同步成功

        Example:
            >>> duck.sync_to_mysql(mysql, "sales", primary_key=["user_id", "date"])
        """
        mysql_table_name = mysql_table_name or table_name
        if isinstance(primary_key, str):
            primary_key = [primary_key]
        has_compound_key = isinstance(primary_key, list) and len(primary_key) > 1

        try:
            # 增量同步逻辑（基于复合主键）
            if primary_key and self.table_exists(table_name):
                # 获取MySQL中已有的主键组合
                pk_columns = ", ".join(primary_key)
                # 注意：MySQL的ExecQuery返回格式是（列名, (行1), (行2), ...）
                mysql_pk_result = mysql_instance.ExecQuery(
                    f"SELECT {pk_columns} FROM {mysql_table_name}"
                )
                # 解析结果为元组列表（跳过第一行列名）
                mysql_pk_tuples = (
                    [tuple(row) for row in mysql_pk_result[1:]]
                    if len(mysql_pk_result) > 1
                    else []
                )

                # 从DuckDB查询不在MySQL中的数据
                if mysql_pk_tuples:
                    pk_str = ", ".join(
                        [f"({', '.join(map(repr, t))})" for t in mysql_pk_tuples]
                    )
                    df = self.execute_query(f"""
                        SELECT * FROM {table_name} 
                        WHERE ({pk_columns}) NOT IN ({pk_str})
                    """)
                    print(f"增量同步到MySQL（复合主键）：{len(df)} 条新数据")
                else:
                    # MySQL中无数据，全量同步
                    df = self.execute_query(f"SELECT * FROM {table_name}")
            else:
                # 无主键，全量同步
                df = self.execute_query(f"SELECT * FROM {table_name}")

            if df.empty:
                print(f"DuckDB表 {table_name} 无新数据可同步到MySQL")
                return True

            # 调用MySQL的dat2db写入（复用现有逻辑，支持复合主键冲突处理）
            mysql_instance.dat2db(df, mysql_table_name)
            print(f"数据已同步到MySQL表 {mysql_table_name}")
            return True
        except Exception as e:
            print(f"同步到MySQL失败: {e}")
            return False

    def list_tables(self):
        """列出所有表（修正DuckDB语法）"""
        try:
            # 使用DuckDB的information_schema获取表列表
            tables = self.conn.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_type = 'BASE TABLE' 
                AND table_schema = 'main'  # 排除系统表
            """).fetchall()
            return [table[0] for table in tables]
        except Exception as e:
            print(f"获取表列表失败: {e}")
            return []

    def get_table_summary(self, table_name):
        """获取表的摘要信息"""
        try:
            # 获取记录数
            count_result = self.execute_query(
                f"SELECT COUNT(*) as count FROM {table_name}"
            )
            count = int(count_result.iloc[0]["count"])

            # 获取表结构
            schema_result = self.execute_query(f"PRAGMA table_info('{table_name}')")

            # 获取前5条数据
            data_result = self.execute_query(f"SELECT * FROM {table_name} LIMIT 5")

            return {
                "table_name": table_name,
                "record_count": count,
                "schema": schema_result,
                "sample_data": data_result,
            }
        except Exception as e:
            print(f"获取表摘要失败: {e}")
            return None

    def print_all_contents(self):
        """打印文件中所有内容的概览"""
        tables = self.list_tables()
        if not tables:
            print("文件中没有找到任何表")
            return

        print(f"=== DuckDB文件内容概览: {self.db_path} ===")
        for table_name in tables:
            summary = self.get_table_summary(table_name)
            if summary:
                print(f"\n表名: {summary['table_name']}")
                print(f"记录数: {summary['record_count']}")
                print("表结构:")
                for _, row in summary["schema"].iterrows():
                    print(f"  {row['name']} ({row['type']})")
                print("前5条数据:")
                print(summary["sample_data"].to_string(index=False))

    def clear_cache(self, table_name=None):
        """清除特定表或所有缓存"""
        if table_name:
            self.cache_time.pop(table_name, None)
            self.cache_data.pop(table_name, None)
        else:
            self.cache_time.clear()
            self.cache_data.clear()

    def get_loaded_tables(self):
        """获取已加载的表列表"""
        return list(self.loaded_tables)

    def close(self):
        """关闭连接"""
        self.conn.close()


# todo 使用示例
if __name__ == "__main__":
    SQLCON1 = {
        "host": "10.108.155.45",
        "user": "cmgg",
        "pwd": "123",
        "db": "report",
    }  # 示例配置

    def db():
        """获取MySQL连接"""
        CON = MYSQL(**SQLCON1)
        return CON, CON.EE

    def get_duckdb_conn(db_path=":memory:"):
        """获取DuckDB连接"""
        return DuckDBWrapper(db_path)
