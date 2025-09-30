import unittest
from unittest.mock import patch,Mock
from src.db_mysql_tool.mysql_utils import MySQLUtils

class TestMySQLUtils(unittest.TestCase):
    def setUp(self):
        """测试前准备"""
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '123456',
            'database': 'scrapy_db',
            'port': 3306
        }
        self.db = MySQLUtils(**self.db_config)

    @patch('pymysql.connect')
    def test_connect_success(self, mock_connect):
        """测试成功连接数据库"""
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        result = self.db.connect()

        self.assertTrue(result)
        mock_connect.assert_called_once()

    @patch('pymysql.connect')
    def test_connect_failure(self, mock_connect):
        """测试连接数据库失败"""
        mock_connect.side_effect = Exception("Connection failed")

        result = self.db.connect()

        self.assertFalse(result)

    def test_insert_data(self):
        """测试插入数据"""
        test_data = {
            'name': 'Test User',
            'email': '123456@example.com',
            'age': 30
        }

        # 这里可以使用mock来测试，避免真实数据库操作
        with patch.object(self.db, 'execute_update') as mock_execute:
            mock_execute.return_value = 1
            result = self.db.insert('users', test_data)

            self.assertEqual(result, 1)
            mock_execute.assert_called_once()

    def test_select_data(self):
        """测试查询数据"""
        with patch.object(self.db, 'execute_query') as mock_execute:
            mock_data = [{'id': 6, 'name': 'Test User'}]
            mock_execute.return_value = mock_data

            result = self.db.select('users')

            self.assertEqual(result, mock_data)
            mock_execute.assert_called_once()

    # def test_context_manager(self):
    #     """测试上下文管理器"""
    #     with patch.object(self.db, 'connect') as mock_connect, \
    #             patch.object(self.db, 'disconnect') as mock_disconnect:
    #         with self.db:
    #             mock_connect.assert_called_once()
    #
    #         mock_disconnect.assert_called_once()

if __name__ == '__main__':
    unittest.main()