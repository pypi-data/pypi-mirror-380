# DB MySQL Tool

A well-encapsulated Python class tool for MySQL database operations, providing easy-to-use CRUD operations and connection management.

## Features

- 🚀 Simple and intuitive API for MySQL operations
- 🔄 Automatic connection management with context manager support
- 📊 Support for both single and bulk operations
- 🛡️ Transaction support with automatic rollback on errors
- 📝 Comprehensive logging
- 🎯 Type hints for better development experience

## Installation

```bash
pip install db-mysql-tool
```

## Quick Start

```python
from db_mysql_tool import MySQLUtils

# 初始化数据库连接
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
    'port': 3306
}

# 使用上下文管理器自动管理连接
with MySQLUtils(**db_config) as db:
    # 创建表
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        age INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    db.execute_update(create_table_sql)
    
    # 插入数据
    user_data = {'name': 'John Doe', 'email': 'john@example.com', 'age': 30}
    user_id = db.insert('users', user_data)
    print(f"Inserted user with ID: {user_id}")
    
    # 查询数据
    users = db.select('users', condition='age > %s', params=(25,))
    for user in users:
        print(user)

# 连接会自动关闭
```

## Advanced Usage

### Bulk Operations

```python
with MySQLUtils(**db_config) as db:
    users_data = [
        {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
        {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
        {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 35}
    ]
    
    affected_rows = db.insert_many('users', users_data)
    print(f"Inserted {affected_rows} users")
```

### Complex Queries

```python
with MySQLUtils(**db_config) as db:
    # 复杂查询
    users = db.select(
        table='users',
        columns='name, email, age',
        condition='age BETWEEN %s AND %s AND name LIKE %s',
        params=(20, 40, '%A%'),
        order_by='age DESC',
        limit=10
    )
```

## API Documentation

### MySQLUtils Class

#### Initialization
```python
MySQLUtils(host, user, password, database, port=3306, charset='utf8mb4')
```

#### Main Methods
- `connect()`: 连接到数据库
- `disconnect()`: 断开数据库连接
- `execute_query(sql, params)`: 执行查询语句
- `execute_update(sql, params)`: 执行增删改操作
- `insert(table, data)`: 插入单条数据
- `insert_many(table, data_list)`: 批量插入数据
- `update(table, data, condition, condition_params)`: 更新数据
- `delete(table, condition, params)`: 删除数据
- `select(table, columns, condition, params, order_by, limit)`: 查询数据
- `select_one(table, columns, condition, params)`: 查询单条数据

## Testing

```bash
# 安装开发依赖
pip install db-mysql-tool[dev]

# 运行测试
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.