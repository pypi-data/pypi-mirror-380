#!/usr/bin/env python3
"""
命令行工具 - DB MySQL Tool
"""

import argparse
import json
from src.db_mysql_tool.mysql_utils import MySQLUtils


def main():
    parser = argparse.ArgumentParser(description='DB MySQL Tool CLI')
    parser.add_argument('--host', required=True, help='MySQL host')
    parser.add_argument('--user', required=True, help='MySQL username')
    parser.add_argument('--password', required=True, help='MySQL password')
    parser.add_argument('--database', required=True, help='MySQL database')
    parser.add_argument('--port', type=int, default=3306, help='MySQL port')
    parser.add_argument('--query', help='SQL query to execute')
    parser.add_argument('--file', help='SQL file to execute')

    args = parser.parse_args()

    db = MySQLUtils(
        host=args.host,
        user=args.user,
        password=args.password,
        database=args.database,
        port=args.port
    )

    try:
        if db.connect():
            if args.query:
                result = db.execute_query(args.query)
                print(json.dumps(result, indent=2, ensure_ascii=False))
            elif args.file:
                with open(args.file, 'r') as f:
                    sql = f.read()
                result = db.execute_query(sql)
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                print("Please provide either --query or --file argument")
    finally:
        db.disconnect()


if __name__ == '__main__':
    main()