import pyodbc
from datetime import datetime, timedelta

server = 'DESKTOP-D3V5DUN\\SQLEXPRESS'
database = 'master'
db_name = 'abcdefg'
table_name = 'tasks'
driver = '{SQL Server}'

def create_database_and_table_if_not_exists():
    driver = '{SQL Server}'
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    try:
        conn = pyodbc.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM sys.databases WHERE name = '{db_name}'")
        exists = cursor.fetchone()[0]
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"""IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}')
                           CREATE TABLE {table_name} (
                               task_ID INT IDENTITY(1,1) PRIMARY KEY,
                               to_email NVARCHAR(255),
                               task NVARCHAR(255),
                               due_date DATETIME,
                               last_notified DATETIME,
                               status NVARCHAR(50)
                           )""")
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def save_to_database(to_email, task, due_date):
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={db_name};Trusted_Connection=yes;'
    try:
        conn = pyodbc.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {table_name} (to_email, task, due_date, last_notified, status) VALUES ( ?, ?, ?, ?, ?)",
                       (to_email,task, due_date, None, 'pending'))
        print("Data inserted successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_last_inserted_id():
    pass

def delete_task_from_database():
    pass

def complete_task_in_database():
    pass