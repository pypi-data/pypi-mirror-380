# -*- coding:utf-8 -*-
"""
MySQL数据上传器 - 重构版本
提供高可用、易维护的MySQL数据上传功能
"""

import datetime
import time
import json
import re
from typing import Union, List, Dict, Optional, Any, Tuple
from functools import wraps
from decimal import Decimal, InvalidOperation
import math

import pymysql
import pandas as pd
from dbutils.pooled_db import PooledDB
from mdbq.log import mylogger
# from mdbq.myconf import myconf

# 配置日志
logger = mylogger.MyLogger(
    logging_mode='file',
    log_level='info',
    log_format='json',
    max_log_size=50,
    backup_count=5,
    enable_async=False,
    sample_rate=1,
    sensitive_fields=[],
    enable_metrics=False,
)


class DatabaseConnectionManager:
    """数据库连接管理器"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.pool = None
        self._create_pool()
    
    def _create_pool(self):
        """创建连接池"""
        pool_params = {
            'creator': pymysql,
            'host': self.config['host'],
            'port': self.config['port'],
            'user': self.config['username'],
            'password': self.config['password'],
            'charset': self.config['charset'],
            'cursorclass': pymysql.cursors.DictCursor,
            'maxconnections': self.config['pool_size'],
            'mincached': self.config.get('mincached', 0),
            'maxcached': self.config.get('maxcached', 0),
            'ping': 7,
            'connect_timeout': self.config.get('connect_timeout', 10),
            'read_timeout': self.config.get('read_timeout', 30),
            'write_timeout': self.config.get('write_timeout', 30),
            'autocommit': False
        }
        
        if self.config.get('ssl'):
            pool_params['ssl'] = self.config['ssl']
        
        try:
            self.pool = PooledDB(**pool_params)
            logger.debug('数据库连接池创建成功', {'host': self.config['host']})
        except Exception as e:
            logger.error('连接池创建失败', {'error': str(e)})
            raise ConnectionError(f'连接池创建失败: {str(e)}')
    
    def get_connection(self):
        """获取数据库连接"""
        if not self.pool:
            self._create_pool()
        return self.pool.connection()
    
    def close(self):
        """关闭连接池"""
        if self.pool:
            self.pool = None
            logger.debug('数据库连接池已关闭')


class DataTypeInferrer:
    """数据类型推断器"""
    
    @staticmethod
    def infer_mysql_type(value: Any) -> str:
        """推断MySQL数据类型"""
        if value is None or str(value).lower() in ['', 'none', 'nan']:
            return 'VARCHAR(255)'
        
        if isinstance(value, bool):
            return 'TINYINT(1)'
        elif isinstance(value, int):
            if -2147483648 <= value <= 2147483647:
                return 'INT'
            else:
                return 'BIGINT'
        elif isinstance(value, float):
            return 'DECIMAL(20,6)'
        elif isinstance(value, (datetime.datetime, pd.Timestamp)):
            return 'DATETIME'
        elif isinstance(value, datetime.date):
            return 'DATE'
        elif isinstance(value, (list, dict)):
            return 'JSON'
        elif isinstance(value, str):
            # 尝试判断是否是日期时间
            if DataValidator.is_datetime_string(value):
                return 'DATETIME'
            
            # 根据字符串长度选择类型
            length = len(value)
            if length <= 255:
                return 'VARCHAR(255)'
            elif length <= 65535:
                return 'TEXT'
            else:
                return 'LONGTEXT'
        
        return 'VARCHAR(255)'
    
    @staticmethod
    def infer_types_from_data(data: List[Dict]) -> Dict[str, str]:
        """从数据中推断所有列的类型"""
        if not data:
            return {}
        
        type_map = {}
        for row in data[:10]:  # 只检查前10行
            for col, value in row.items():
                # 跳过系统列
                if col.lower() in ['id', 'create_at', 'update_at']:
                    continue
                if col not in type_map and value is not None:
                    type_map[col] = DataTypeInferrer.infer_mysql_type(value)
        
        # 自动添加系统列类型定义
        type_map['id'] = 'BIGINT'
        type_map['create_at'] = 'TIMESTAMP'
        type_map['update_at'] = 'TIMESTAMP'
        
        return type_map


class DataValidator:
    """数据验证器"""
    
    @staticmethod
    def is_datetime_string(value: str) -> bool:
        """检查字符串是否为日期时间格式"""
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%Y/%m/%d %H:%M:%S',
            '%Y/%m/%d',
            '%Y%m%d',
            '%Y-%m-%dT%H:%M:%S',
        ]
        
        for fmt in formats:
            try:
                datetime.datetime.strptime(value, fmt)
                return True
            except ValueError:
                continue
        return False
    
    @staticmethod
    def validate_and_convert_value(value: Any, mysql_type: str, allow_null: bool = False) -> Any:
        """验证并转换数据值"""
        mysql_type_lower = mysql_type.lower()
        
        # 处理空值
        if value is None or (isinstance(value, str) and value.strip() == ''):
            if allow_null:
                return None
            # 对于日期时间类型，直接返回默认的日期时间值
            if 'datetime' in mysql_type_lower or 'timestamp' in mysql_type_lower:
                return '2000-01-01 00:00:00'
            elif 'date' in mysql_type_lower:
                return '2000-01-01'
            return DataValidator._get_default_value(mysql_type)
        
        # 处理pandas的NaN值
        if not isinstance(value, (list, dict)):
            try:
                if pd.isna(value) or (isinstance(value, float) and math.isinf(value)):
                    if allow_null:
                        return None
                    # 对于日期时间类型，直接返回默认的日期时间值
                    if 'datetime' in mysql_type_lower or 'timestamp' in mysql_type_lower:
                        return '2000-01-01 00:00:00'
                    elif 'date' in mysql_type_lower:
                        return '2000-01-01'
                    return DataValidator._get_default_value(mysql_type)
            except (ValueError, TypeError):
                pass
        
        # JSON类型
        if 'json' in mysql_type_lower:
            if isinstance(value, (dict, list)):
                return json.dumps(value, ensure_ascii=False)
            elif isinstance(value, str):
                try:
                    json.loads(value)
                    return value
                except (TypeError, ValueError):
                    raise ValueError(f"无效的JSON字符串: {value}")
            else:
                return str(value)
        
        # 日期时间类型
        if 'datetime' in mysql_type_lower or 'timestamp' in mysql_type_lower:
            return DataValidator._convert_to_datetime(value)
        elif 'date' in mysql_type_lower:
            return DataValidator._convert_to_date(value)
        
        # 数值类型
        elif 'int' in mysql_type_lower:
            return DataValidator._convert_to_int(value)
        elif any(t in mysql_type_lower for t in ['decimal', 'float', 'double']):
            return DataValidator._convert_to_decimal(value)
        
        # 字符串类型
        elif 'varchar' in mysql_type_lower:
            str_value = str(value)
            # 检查长度限制
            match = re.search(r'\((\d+)\)', mysql_type)
            if match:
                max_len = int(match.group(1))
                if len(str_value.encode('utf-8')) > max_len:
                    return str_value.encode('utf-8')[:max_len].decode('utf-8', 'ignore')
            return str_value
        
        # 默认转为字符串
        return str(value)
    
    @staticmethod
    def _get_default_value(mysql_type: str) -> Any:
        """获取MySQL类型的默认值"""
        mysql_type_lower = mysql_type.lower()
        
        if any(t in mysql_type_lower for t in ['int', 'bigint', 'tinyint', 'smallint']):
            return 0
        elif any(t in mysql_type_lower for t in ['decimal', 'float', 'double']):
            return 0.0
        elif any(t in mysql_type_lower for t in ['varchar', 'text', 'char']):
            return 'none'
        elif 'date' in mysql_type_lower:
            if 'datetime' in mysql_type_lower:
                return '2000-01-01 00:00:00'
            else:
                return '2000-01-01'
        elif 'json' in mysql_type_lower:
            return '{}'
        else:
            return 'none'
    
    @staticmethod
    def _convert_to_datetime(value: Any) -> str:
        """转换为datetime格式"""
        if hasattr(value, 'strftime'):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        
        value_str = str(value).strip()
        
        # 处理特殊的无效值
        if value_str.lower() in ['none', 'null', 'nan', '', 'nat']:
            return '2000-01-01 00:00:00'
        
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%Y/%m/%d %H:%M:%S',
            '%Y/%m/%d',
            '%Y%m%d',
            '%Y-%m-%dT%H:%M:%S',
        ]
        
        for fmt in formats:
            try:
                dt = datetime.datetime.strptime(value_str, fmt)
                return dt.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                continue
        
        # 如果所有格式都无法解析，返回默认值而不是抛出异常
        return '2000-01-01 00:00:00'
    
    @staticmethod
    def _convert_to_date(value: Any) -> str:
        """转换为date格式"""
        if hasattr(value, 'strftime'):
            return value.strftime('%Y-%m-%d')
        
        # 先转为datetime再提取日期部分
        datetime_str = DataValidator._convert_to_datetime(value)
        return datetime_str.split(' ')[0]
    
    @staticmethod
    def _convert_to_int(value: Any) -> int:
        """转换为整数"""
        if hasattr(value, 'item'):
            try:
                value = value.item()
            except Exception:
                pass
        
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return int(float(value))
            except (ValueError, TypeError):
                raise ValueError(f"无法转换为整数: {value}")
    
    @staticmethod
    def _convert_to_decimal(value: Any) -> Decimal:
        """转换为Decimal"""
        if hasattr(value, 'item'):
            try:
                value = value.item()
            except Exception:
                pass
        
        # 处理百分比字符串
        if isinstance(value, str) and '%' in value:
            if re.match(r'^-?\d+(\.\d+)?%$', value.strip()):
                value = float(value.strip().replace('%', '')) / 100
        
        try:
            return Decimal(str(value))
        except (ValueError, TypeError, InvalidOperation):
            raise ValueError(f"无法转换为数值: {value}")


class TableManager:
    """表管理器"""
    
    def __init__(self, connection_manager: DatabaseConnectionManager, collation: str):
        self.conn_mgr = connection_manager
        self.collation = collation
    
    def ensure_database_exists(self, db_name: str):
        """确保数据库存在"""
        db_name = self._sanitize_identifier(db_name)
        
        with self.conn_mgr.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s",
                    (db_name,)
                )
                if not cursor.fetchone():
                    charset = self.conn_mgr.config['charset']
                    sql = f"CREATE DATABASE `{db_name}` CHARACTER SET {charset} COLLATE {self.collation}"
                    cursor.execute(sql)
                    conn.commit()
                    logger.debug('数据库已创建', {'database': db_name})
    
    def table_exists(self, db_name: str, table_name: str) -> bool:
        """检查表是否存在"""
        db_name = self._sanitize_identifier(db_name)
        table_name = self._sanitize_identifier(table_name)
        
        with self.conn_mgr.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
                    (db_name, table_name)
                )
                return bool(cursor.fetchone())
    
    def create_table(self, db_name: str, table_name: str, columns: Dict[str, str], 
                    primary_keys: Optional[List[str]] = None, 
                    unique_keys: Optional[List[List[str]]] = None):
        """创建表"""
        db_name = self._sanitize_identifier(db_name)
        table_name = self._sanitize_identifier(table_name)
        
        # 构建列定义
        column_defs = []
        
        # 始终添加自增ID列作为主键
        column_defs.append("`id` BIGINT NOT NULL AUTO_INCREMENT")
        
        # 添加业务列
        for col_name, col_type in columns.items():
            if col_name.lower() in ['id', 'create_at', 'update_at']:
                continue
            safe_col_name = self._sanitize_identifier(col_name)
            column_defs.append(f"`{safe_col_name}` {col_type} NOT NULL")
        
        # 添加时间戳列
        column_defs.append("`create_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP")
        column_defs.append("`update_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        
        # 主键定义（始终使用id作为主键）
        primary_key_def = "PRIMARY KEY (`id`)"
        
        # 唯一约束定义
        unique_defs = []
        if unique_keys:
            for i, uk in enumerate(unique_keys):
                # 过滤掉系统列
                filtered_uk = [col for col in uk if col.lower() not in ['id', 'create_at', 'update_at']]
                if filtered_uk:
                    safe_uk = [f"`{self._sanitize_identifier(col)}`" for col in filtered_uk]
                    unique_name = f"uniq_{i}"
                    unique_defs.append(f"UNIQUE KEY `{unique_name}` ({','.join(safe_uk)})")
        
        # 组合所有定义
        all_defs = column_defs + [primary_key_def] + unique_defs
        
        charset = self.conn_mgr.config['charset']
        sql = f"""
        CREATE TABLE `{db_name}`.`{table_name}` (
            {','.join(all_defs)}
        ) ENGINE=InnoDB DEFAULT CHARSET={charset} COLLATE={self.collation}
        """
        
        with self.conn_mgr.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                conn.commit()
                logger.debug('表已创建', {'database': db_name, 'table': table_name})
    
    def get_partition_table_name(self, base_name: str, date_value: str, partition_by: str) -> str:
        """获取分表名称"""
        try:
            if isinstance(date_value, str):
                date_obj = pd.to_datetime(date_value)
            else:
                date_obj = date_value
            
            if partition_by == 'year':
                return f"{base_name}_{date_obj.year}"
            elif partition_by == 'month':
                return f"{base_name}_{date_obj.year}_{date_obj.month:02d}"
            else:
                raise ValueError("partition_by必须是'year'或'month'")
        except Exception as e:
            raise ValueError(f"无效的日期值: {date_value}, 错误: {str(e)}")
    
    @staticmethod
    def _sanitize_identifier(identifier: str) -> str:
        """清理标识符"""
        if not identifier or not isinstance(identifier, str):
            raise ValueError(f"无效的标识符: {identifier}")
        
        # 清理特殊字符
        cleaned = re.sub(r'[^\w\u4e00-\u9fff$]', '_', identifier)
        cleaned = re.sub(r'_+', '_', cleaned).strip('_')
        
        if not cleaned:
            raise ValueError(f"标识符清理后为空: {identifier}")
        
        # 检查MySQL关键字
        mysql_keywords = {
            'select', 'insert', 'update', 'delete', 'from', 'where', 'and', 'or',
            'not', 'like', 'in', 'is', 'null', 'true', 'false', 'between'
        }
        
        if len(cleaned) > 64:
            cleaned = cleaned[:64]
        
        if cleaned.lower() in mysql_keywords:
            return f"`{cleaned}`"
        
        return cleaned


class DataProcessor:
    """数据处理器"""
    
    @staticmethod
    def normalize_data(data: Union[Dict, List[Dict], pd.DataFrame]) -> List[Dict]:
        """标准化数据格式为字典列表"""
        if isinstance(data, pd.DataFrame):
            return data.to_dict('records')
        elif isinstance(data, dict):
            return [data]
        elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return data
        else:
            raise ValueError("数据格式必须是字典、字典列表或DataFrame")
    
    @staticmethod
    def prepare_data_for_insert(data: List[Dict], set_typ: Dict[str, str], 
                               allow_null: bool = False) -> List[Dict]:
        """准备插入数据"""
        prepared_data = []
        
        for row_idx, row in enumerate(data, 1):
            prepared_row = {}
            
            for col_name, col_type in set_typ.items():
                # 跳过系统列（id, create_at, update_at由MySQL自动处理）
                if col_name.lower() in ['id', 'create_at', 'update_at']:
                    continue
                
                value = row.get(col_name)
                try:
                    prepared_row[col_name] = DataValidator.validate_and_convert_value(
                        value, col_type, allow_null
                    )
                except ValueError as e:
                    logger.error('数据验证失败', {
                        '行号': row_idx,
                        '列名': col_name,
                        '原始值': value,
                        '错误': str(e)
                    })
                    raise ValueError(f"行{row_idx}列{col_name}验证失败: {str(e)}")
            
            prepared_data.append(prepared_row)
        
        return prepared_data
    
    @staticmethod
    def partition_data_by_date(data: List[Dict], date_column: str, 
                              partition_by: str) -> Dict[str, List[Dict]]:
        """按日期分区数据"""
        partitioned = {}
        table_manager = TableManager(None, None)  # 只用静态方法
        
        for row in data:
            if date_column not in row:
                logger.warning('缺少分区日期列', {'列名': date_column, '行数据': row})
                continue
            
            try:
                partition_suffix = table_manager.get_partition_table_name(
                    '', row[date_column], partition_by
                ).split('_', 1)[1]  # 获取后缀部分
                
                if partition_suffix not in partitioned:
                    partitioned[partition_suffix] = []
                partitioned[partition_suffix].append(row)
            except Exception as e:
                logger.error('分区处理失败', {'行数据': row, '错误': str(e)})
                continue
        
        return partitioned


class DataInserter:
    """数据插入器"""
    
    def __init__(self, connection_manager: DatabaseConnectionManager):
        self.conn_mgr = connection_manager
    
    def insert_data(self, db_name: str, table_name: str, data: List[Dict], 
                   set_typ: Dict[str, str], update_on_duplicate: bool = False) -> Tuple[int, int, int]:
        """插入数据"""
        if not data:
            return 0, 0, 0
        
        # 准备SQL语句（排除系统列）
        columns = [col for col in set_typ.keys() if col.lower() not in ['id', 'create_at', 'update_at']]
        safe_columns = [TableManager._sanitize_identifier(col) for col in columns]
        placeholders = ','.join(['%s'] * len(columns))
        
        sql = f"""
        INSERT INTO `{db_name}`.`{table_name}` 
        (`{'`,`'.join(safe_columns)}`) 
        VALUES ({placeholders})
        """
        
        if update_on_duplicate:
            # 更新时只更新业务列，不更新create_at，update_at会自动更新
            update_clause = ", ".join([f"`{col}` = VALUES(`{col}`)" for col in safe_columns])
            sql += f" ON DUPLICATE KEY UPDATE {update_clause}"
        
        # 批量插入
        return self._execute_batch_insert(sql, data, columns)
    
    def _execute_batch_insert(self, sql: str, data: List[Dict], 
                             columns: List[str]) -> Tuple[int, int, int]:
        """执行批量插入"""
        batch_size = min(1000, len(data))
        total_inserted = 0
        total_skipped = 0
        total_failed = 0
        
        with self.conn_mgr.get_connection() as conn:
            with conn.cursor() as cursor:
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    values_list = []
                    
                    for row in batch:
                        values = [self._ensure_basic_type(row.get(col)) for col in columns]
                        values_list.append(values)
                    
                    try:
                        cursor.executemany(sql, values_list)
                        conn.commit()
                        affected = cursor.rowcount if cursor.rowcount is not None else len(batch)
                        total_inserted += affected
                    except pymysql.err.IntegrityError:
                        conn.rollback()
                        total_skipped += len(batch)
                        logger.debug('批量插入唯一约束冲突，跳过', {'批次大小': len(batch)})
                    except Exception as e:
                        conn.rollback()
                        total_failed += len(batch)
                        logger.error('批量插入失败', {'错误': str(e), '批次大小': len(batch)})
        
        return total_inserted, total_skipped, total_failed
    
    @staticmethod
    def _ensure_basic_type(value):
        """确保值是基本数据类型"""
        if isinstance(value, (dict, list)):
            try:
                return json.dumps(value, ensure_ascii=False)
            except (TypeError, ValueError):
                return str(value)
        return value


def retry_on_failure(max_retries: int = 3, delay: int = 1):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (pymysql.OperationalError, pymysql.InterfaceError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        logger.warning('操作失败，准备重试', {
                            '尝试次数': attempt + 1,
                            '错误': str(e)
                        })
                        time.sleep(delay * (attempt + 1))
                        continue
                    logger.error(f'操作重试{max_retries}次后失败', {'错误': str(e)})
                    raise
                except Exception as e:
                    logger.error('操作失败', {'错误': str(e)})
                    raise
            raise last_exception
        return wrapper
    return decorator


class MySQLUploader:
    """
    MySQL数据上传器 - 重构版本
    
    特性：
    - 自动为每个表添加id（BIGINT自增主键）、create_at、update_at时间戳列
    - 支持自动建表、分表、数据类型推断
    - 高可用连接池管理和重试机制
    - 批量插入优化
    """
    
    def __init__(self, username: str, password: str, host: str = 'localhost', 
                 port: int = 3306, charset: str = 'utf8mb4', 
                 collation: str = 'utf8mb4_0900_ai_ci', pool_size: int = 5,
                 max_retries: int = 3, **kwargs):
        """
        初始化MySQL上传器
        
        :param username: 数据库用户名
        :param password: 数据库密码
        :param host: 数据库主机地址
        :param port: 数据库端口
        :param charset: 字符集
        :param collation: 排序规则
        :param pool_size: 连接池大小
        :param max_retries: 最大重试次数
        """
        self.config = {
            'username': username,
            'password': password,
            'host': host,
            'port': port,
            'charset': charset,
            'pool_size': pool_size,
            **kwargs
        }
        self.collation = collation
        self.max_retries = max_retries
        
        # 初始化组件
        self.conn_mgr = DatabaseConnectionManager(self.config)
        self.table_mgr = TableManager(self.conn_mgr, collation)
        self.data_inserter = DataInserter(self.conn_mgr)
    
    @retry_on_failure(max_retries=3)
    def upload_data(self, db_name: str, table_name: str, 
                   data: Union[Dict, List[Dict], pd.DataFrame],
                   set_typ: Optional[Dict[str, str]] = None,
                   allow_null: bool = False,
                   partition_by: Optional[str] = None,
                   partition_date_column: str = '日期',
                   update_on_duplicate: bool = False,
                   unique_keys: Optional[List[List[str]]] = None) -> bool:
        """
        上传数据到MySQL数据库
        
        注意：系统会自动为每个表添加以下系统列：
        - id: BIGINT自增主键
        - create_at: 创建时间戳（插入时自动设置）
        - update_at: 更新时间戳（插入和更新时自动设置）
        
        :param db_name: 数据库名（会自动转为小写）
        :param table_name: 表名（会自动转为小写）
        :param data: 要上传的数据
        :param set_typ: 列类型定义，如果为None则自动推断（无需包含系统列）
        :param allow_null: 是否允许空值
        :param partition_by: 分表方式('year'或'month')
        :param partition_date_column: 分表日期列名
        :param update_on_duplicate: 遇到重复数据时是否更新
        :param unique_keys: 唯一约束列表（无需包含系统列）
        :return: 上传是否成功
        """
        db_name = db_name.lower()
        table_name = table_name.lower()
        try:
            start_time = time.time()
            
            # 标准化数据
            normalized_data = DataProcessor.normalize_data(data)
            if not normalized_data:
                logger.warning('数据为空，跳过上传')
                return True
            
            # 推断或验证列类型
            if set_typ is None:
                set_typ = DataTypeInferrer.infer_types_from_data(normalized_data)
                logger.info('自动推断数据类型', {'类型映射': set_typ})
            
            # 确保数据库存在
            self.table_mgr.ensure_database_exists(db_name)
            
            # 处理分表逻辑
            if partition_by:
                return self._handle_partitioned_upload(
                    db_name, table_name, normalized_data, set_typ,
                    partition_by, partition_date_column, allow_null,
                    update_on_duplicate, unique_keys
                )
            else:
                return self._handle_single_table_upload(
                    db_name, table_name, normalized_data, set_typ,
                    allow_null, update_on_duplicate, unique_keys
                )
        
        except Exception as e:
            logger.error('数据上传失败', {
                '数据库': db_name,
                '表名': table_name,
                '错误': str(e)
            })
            return False
    
    def _handle_single_table_upload(self, db_name: str, table_name: str,
                                   data: List[Dict], set_typ: Dict[str, str],
                                   allow_null: bool, update_on_duplicate: bool,
                                   unique_keys: Optional[List[List[str]]]) -> bool:
        """处理单表上传"""
        # 确保表存在
        if not self.table_mgr.table_exists(db_name, table_name):
            self.table_mgr.create_table(db_name, table_name, set_typ, 
                                       unique_keys=unique_keys)
        
        # 准备数据
        prepared_data = DataProcessor.prepare_data_for_insert(
            data, set_typ, allow_null
        )
        
        # 插入数据
        inserted, skipped, failed = self.data_inserter.insert_data(
            db_name, table_name, prepared_data, set_typ, update_on_duplicate
        )
        
        logger.info('单表上传完成', {
            '数据库': db_name,
            '表名': table_name,
            '总数': len(data),
            '插入': inserted,
            '跳过': skipped,
            '失败': failed
        })
        
        return failed == 0
    
    def _handle_partitioned_upload(self, db_name: str, base_table_name: str,
                                  data: List[Dict], set_typ: Dict[str, str],
                                  partition_by: str, partition_date_column: str,
                                  allow_null: bool, update_on_duplicate: bool,
                                  unique_keys: Optional[List[List[str]]]) -> bool:
        """处理分表上传"""
        # 按日期分区数据
        partitioned_data = DataProcessor.partition_data_by_date(
            data, partition_date_column, partition_by
        )
        
        total_success = True
        
        for partition_suffix, partition_data in partitioned_data.items():
            partition_table_name = f"{base_table_name}_{partition_suffix}"
            
            success = self._handle_single_table_upload(
                db_name, partition_table_name, partition_data, set_typ,
                allow_null, update_on_duplicate, unique_keys
            )
            
            if not success:
                total_success = False
        
        logger.info('分表上传完成', {
            '数据库': db_name,
            '基础表名': base_table_name,
            '分区数': len(partitioned_data),
            '总体成功': total_success
        })
        
        return total_success
    
    def close(self):
        """关闭连接"""
        if self.conn_mgr:
            self.conn_mgr.close()
    
    def __del__(self):
        try:
            self.close()
        except:
            pass
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# 使用示例
if __name__ == '__main__':
    # 示例代码
    uploader = MySQLUploader(
        username='your_username',
        password='your_password',
        host='localhost',
        port=3306
    )
    
    # 示例数据
    sample_data = [
        {'name': 'Alice', 'age': 25, 'salary': 50000.0, '日期': '2023-01-01'},
        {'name': 'Bob', 'age': 30, 'salary': 60000.0, '日期': '2023-01-02'},
    ]
    
    # 定义列类型（系统会自动添加id、create_at、update_at列）
    column_types = {
        'name': 'VARCHAR(255)',
        'age': 'INT',
        'salary': 'DECIMAL(10,2)',
        '日期': 'DATE'
    }
    
    # 上传数据
    success = uploader.upload_data(
        db_name='test_db',
        table_name='test_table',
        data=sample_data,
        set_typ=column_types,
        allow_null=False,
        update_on_duplicate=True,
        unique_keys=[['name', '日期']]
    )
    
    uploader.close()
    print(f"上传结果: {success}") 