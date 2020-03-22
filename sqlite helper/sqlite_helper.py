import sqlite3
from sqlite3 import Error


DATABASE_NAME = "common/database/chinook.db"


def execute_none_query(query: str) -> None:
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)


def execute_select_query(query: str) -> list:
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        descriptions = []
        for item in cursor.description:
            descriptions.append(item[0])
        list_data = []  # return this
        for row in rows:
            data = {}
            for index, value in enumerate(row):
                data[descriptions[index]] = value
            list_data.append(data)
        return list_data
    except Error as e:
        print("execute_select_query error", query)
        print(e)
        return []


def execute_paginate_query(
        query: str,
        page_size: int = 20,
        page_number: int = 1) -> list:
    try:
        ignore_rows = page_size*(page_number - 1)
        fetch_next = page_size
        query += f" limit {ignore_rows}, {fetch_next}"
        data = execute_select_query(query)
        print("execute_paginate_query", query)
        return data
    except Error as e:
        print("execute_select_query error", query)
        print(e)
        return []


def execute_count_query(query: str) -> list:
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows[0]
    except Error as e:
        print("execute_select_query error", query)
        print(e)
        return []


def execute_select_and_count(
        select_query: str,
        count_query: str,
        page_size: int = 20,
        page_number: int = 1):
    try:
        data = execute_paginate_query(select_query, page_size, page_number)
        total = execute_count_query(count_query)
        return (data, total)
    except Error as e:
        print("execute_select_and_count error", e)
        return ([], 0)


if __name__ == "__main__":
    select_employee = f"""
    select count(*) from employees
    """
    execute_count_query(select_employee)
