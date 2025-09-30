import pymysql
from typing import List, Tuple, Any, Dict, Optional, Union
import logging
import sys

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('MySQLUtils')


class MySQLUtils:
    """MySQL 数据库操作工具类 - 支持上下文管理器"""

    def __init__(self, host: str, user: str, password: str, database: str,
                 port: int = 3306, charset: str = 'utf8mb4', autocommit: bool = True):
        """
        初始化数据库连接参数

        Args:
            host: 数据库主机地址
            user: 数据库用户名
            password: 数据库密码
            database: 数据库名称
            port: 数据库端口，默认3306
            charset: 字符集，默认utf8mb4
            autocommit: 是否自动提交事务，默认True
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None
        self._connected = False

    def __enter__(self):
        """
        进入上下文管理器时调用
        Returns:
            self: 返回自身实例
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器时调用

        Args:
            exc_type: 异常类型
            exc_val: 异常值
            exc_tb: 异常跟踪信息
        Returns:
            bool: 如果返回True，则异常被压制；返回False则异常会继续传播
        """
        try:
            self.disconnect()
        except Exception as e:
            logger.error(f"断开连接时发生错误: {e}")
        # 如果发生异常，返回False让异常继续传播
        return False

    def connect(self) -> bool:
        """
        连接数据库

        Returns:
            bool: 连接成功返回True，失败返回False
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                charset=self.charset,
                autocommit=self.autocommit,
                cursorclass=pymysql.cursors.DictCursor  # 返回字典形式的结果
            )
            self.cursor = self.connection.cursor()
            self._connected = True
            logger.info(f"成功连接到数据库 {self.database}")
            return True
        except Exception as e:
            logger.error(f"数据库连接失败: {e}")
            self._connected = False
            return False

    def disconnect(self):
        """断开数据库连接"""
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
            self._connected = False
            logger.info("数据库连接已关闭")
        except Exception as e:
            logger.error(f"断开数据库连接时发生错误: {e}")
            raise

    def is_connected(self) -> bool:
        """
        检查是否已连接数据库

        Returns:
            bool: 已连接返回True，否则返回False
        """
        if not self._connected or not self.connection:
            return False
        try:
            # 尝试执行一个简单的查询来验证连接是否有效
            self.cursor.execute("SELECT 1")
            return True
        except Exception:
            self._connected = False
            return False

    def ensure_connection(self):
        """确保数据库连接有效，如果无效则重新连接"""
        if not self.is_connected():
            logger.info("数据库连接已断开，尝试重新连接...")
            self.connect()

    def execute_query(self, sql: str, params: Union[Tuple, List, Dict] = None) -> List[Dict]:
        """
        执行查询语句

        Args:
            sql: SQL查询语句
            params: 查询参数

        Returns:
            List[Dict]: 查询结果列表
        """
        try:
            self.ensure_connection()

            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            logger.debug(f"执行查询: {sql}, 参数: {params}, 返回行数: {len(result)}")
            return result
        except Exception as e:
            logger.error(f"查询执行失败: {e}, SQL: {sql}")
            return []

    def execute_query_one(self, sql: str, params: Union[Tuple, List, Dict] = None) -> Optional[Dict]:
        """
        执行查询语句，返回单条记录

        Args:
            sql: SQL查询语句
            params: 查询参数

        Returns:
            Optional[Dict]: 单条查询结果，无结果时返回None
        """
        try:
            self.ensure_connection()

            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            logger.debug(f"执行单条查询: {sql}, 参数: {params}")
            return result
        except Exception as e:
            logger.error(f"单条查询执行失败: {e}, SQL: {sql}")
            return None

    def execute_update(self, sql: str, params: Union[Tuple, List, Dict] = None) -> int:
        """
        执行增删改操作

        Args:
            sql: SQL语句
            params: 参数

        Returns:
            int: 受影响的行数
        """
        try:
            self.ensure_connection()

            affected_rows = self.cursor.execute(sql, params)
            if not self.autocommit:
                self.connection.commit()
            logger.debug(f"执行更新: {sql}, 参数: {params}, 影响行数: {affected_rows}")
            return affected_rows
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"更新执行失败: {e}, SQL: {sql}")
            return 0

    def execute_many(self, sql: str, params: List[Union[Tuple, List, Dict]]) -> int:
        """
        批量执行操作

        Args:
            sql: SQL语句
            params: 参数列表

        Returns:
            int: 受影响的行数
        """
        try:
            self.ensure_connection()

            affected_rows = self.cursor.executemany(sql, params)
            if not self.autocommit:
                self.connection.commit()
            logger.debug(f"批量执行: {sql}, 参数数量: {len(params)}, 影响行数: {affected_rows}")
            return affected_rows
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"批量执行失败: {e}, SQL: {sql}")
            return 0

    def begin_transaction(self):
        """开始事务（仅在 autocommit=False 时有效）"""
        if self.connection and not self.autocommit:
            # 在PyMySQL中，autocommit=False时默认在事务中
            # 这里主要是一个语义上的方法
            logger.debug("开始事务")

    def commit(self):
        """提交事务"""
        if self.connection and not self.autocommit:
            self.connection.commit()
            logger.debug("事务已提交")

    def rollback(self):
        """回滚事务"""
        if self.connection and not self.autocommit:
            self.connection.rollback()
            logger.debug("事务已回滚")

    def insert(self, table: str, data: Dict) -> int:
        """
        插入单条数据

        Args:
            table: 表名
            data: 数据字典

        Returns:
            int: 插入的行ID
        """
        try:
            self.ensure_connection()

            keys = ', '.join(data.keys())
            values_placeholder = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {table} ({keys}) VALUES ({values_placeholder})"

            self.cursor.execute(sql, tuple(data.values()))
            if not self.autocommit:
                self.connection.commit()
            last_id = self.cursor.lastrowid
            logger.debug(f"插入数据到 {table}, 数据: {data}, 最后ID: {last_id}")
            return last_id
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"插入数据失败: {e}, 表: {table}, 数据: {data}")
            return 0

    def insert_many(self, table: str, data_list: List[Dict]) -> int:
        """
        批量插入数据

        Args:
            table: 表名
            data_list: 数据字典列表

        Returns:
            int: 受影响的行数
        """
        if not data_list:
            return 0

        try:
            self.ensure_connection()

            keys = ', '.join(data_list[0].keys())
            values_placeholder = ', '.join(['%s'] * len(data_list[0]))
            sql = f"INSERT INTO {table} ({keys}) VALUES ({values_placeholder})"

            values = [tuple(item.values()) for item in data_list]
            affected_rows = self.cursor.executemany(sql, values)
            if not self.autocommit:
                self.connection.commit()
            logger.debug(f"批量插入数据到 {table}, 数据数量: {len(data_list)}, 影响行数: {affected_rows}")
            return affected_rows
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"批量插入数据失败: {e}, 表: {table}")
            return 0

    def update(self, table: str, data: Dict, condition: str, condition_params: Union[Tuple, List, Dict] = None) -> int:
        """
        更新数据

        Args:
            table: 表名
            data: 要更新的数据字典
            condition: WHERE条件
            condition_params: 条件参数

        Returns:
            int: 受影响的行数
        """
        try:
            self.ensure_connection()

            set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
            sql = f"UPDATE {table} SET {set_clause} WHERE {condition}"

            params = tuple(data.values())
            if condition_params:
                if isinstance(condition_params, (list, tuple)):
                    params += tuple(condition_params)
                else:
                    params += (condition_params,)

            affected_rows = self.cursor.execute(sql, params)
            if not self.autocommit:
                self.connection.commit()
            logger.debug(f"更新表 {table}, 数据: {data}, 条件: {condition}, 影响行数: {affected_rows}")
            return affected_rows
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"更新数据失败: {e}, 表: {table}, 数据: {data}")
            return 0

    def delete(self, table: str, condition: str, params: Union[Tuple, List, Dict] = None) -> int:
        """
        删除数据

        Args:
            table: 表名
            condition: WHERE条件
            params: 条件参数

        Returns:
            int: 受影响的行数
        """
        try:
            self.ensure_connection()

            sql = f"DELETE FROM {table} WHERE {condition}"
            affected_rows = self.cursor.execute(sql, params)
            if not self.autocommit:
                self.connection.commit()
            logger.debug(f"删除表 {table} 数据, 条件: {condition}, 影响行数: {affected_rows}")
            return affected_rows
        except Exception as e:
            if self.connection and not self.autocommit:
                self.connection.rollback()
            logger.error(f"删除数据失败: {e}, 表: {table}, 条件: {condition}")
            return 0

    def select(self, table: str, columns: str = "*", condition: str = None,
               params: Union[Tuple, List, Dict] = None, order_by: str = None,
               limit: int = None, offset: int = None) -> List[Dict]:
        """
        查询数据

        Args:
            table: 表名
            columns: 查询列，默认*
            condition: WHERE条件
            params: 条件参数
            order_by: 排序
            limit: 限制条数
            offset: 偏移量

        Returns:
            List[Dict]: 查询结果
        """
        try:
            self.ensure_connection()

            sql = f"SELECT {columns} FROM {table}"

            if condition:
                sql += f" WHERE {condition}"

            if order_by:
                sql += f" ORDER BY {order_by}"

            if limit is not None:
                sql += f" LIMIT {limit}"
                if offset is not None:
                    sql += f" OFFSET {offset}"

            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            logger.debug(f"查询表 {table}, 条件: {condition}, 返回行数: {len(result)}")
            return result
        except Exception as e:
            logger.error(f"查询数据失败: {e}, 表: {table}")
            return []

    def select_one(self, table: str, columns: str = "*", condition: str = None,
                   params: Union[Tuple, List, Dict] = None) -> Optional[Dict]:
        """
        查询单条数据

        Args:
            table: 表名
            columns: 查询列，默认*
            condition: WHERE条件
            params: 条件参数

        Returns:
            Optional[Dict]: 单条查询结果
        """
        try:
            self.ensure_connection()

            sql = f"SELECT {columns} FROM {table}"

            if condition:
                sql += f" WHERE {condition}"

            sql += " LIMIT 1"

            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            logger.debug(f"查询单条表 {table}, 条件: {condition}")
            return result
        except Exception as e:
            logger.error(f"查询单条数据失败: {e}, 表: {table}")
            return None

    def table_exists(self, table_name: str) -> bool:
        """
        检查表是否存在

        Args:
            table_name: 表名

        Returns:
            bool: 表是否存在
        """
        try:
            sql = """
            SELECT COUNT(*) as count 
            FROM information_schema.tables 
            WHERE table_schema = %s AND table_name = %s
            """
            result = self.execute_query_one(sql, (self.database, table_name))
            return result['count'] > 0 if result else False
        except Exception as e:
            logger.error(f"检查表存在失败: {e}")
            return False

    def get_table_columns(self, table_name: str) -> List[str]:
        """
        获取表的所有列名

        Args:
            table_name: 表名

        Returns:
            List[str]: 列名列表
        """
        try:
            sql = f"DESCRIBE {table_name}"
            result = self.execute_query(sql)
            return [column['Field'] for column in result] if result else []
        except Exception as e:
            logger.error(f"获取表列名失败: {e}")
            return []

    def get_table_info(self, table_name: str) -> List[Dict]:
        """
        获取表的详细信息

        Args:
            table_name: 表名

        Returns:
            List[Dict]: 表的列信息
        """
        try:
            sql = f"SHOW COLUMNS FROM {table_name}"
            return self.execute_query(sql)
        except Exception as e:
            logger.error(f"获取表信息失败: {e}")
            return []