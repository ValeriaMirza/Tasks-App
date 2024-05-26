import pyodbc
from datetime import datetime, timedelta
from config import server

database = 'master'
db_name = 'abcdefgiJ'
table_name = 'tasks'
driver = '{SQL Server}'


def get_conn_str(db):
    return (f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={db};'
            'Trusted_Connection=yes;')


def create_database_and_table_if_not_exists():
    conn_str = get_conn_str(database)
    try:
        conn = pyodbc.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) "
                       f"FROM sys.databases WHERE name = '{db_name}'")
        exists = cursor.fetchone()[0]
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"""
                            IF NOT EXISTS (
                                SELECT *
                                 FROM INFORMATION_SCHEMA.TABLES
                                 WHERE TABLE_NAME = '{table_name}'
                            )
                            CREATE TABLE {table_name} (
                                task_ID INT IDENTITY(1,1) PRIMARY KEY,
                                to_email NVARCHAR(255),
                                task NVARCHAR(255),
                                due_date DATETIME,
                                last_notified DATETIME,
                                status NVARCHAR(50)
                            )
                        """)
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def save_to_database(to_email, task, due_date):
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"""
                            INSERT INTO {table_name} (
                                to_email,
                                task,
                                due_date,
                                last_notified,
                                status
                            )
                             VALUES (?,?,?,?,?)
                        """, (to_email, task, due_date, None, 'pending'))

        print("Data inserted successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    finally:
        cursor.close()
        conn.close()


def get_tasks_due_within_hour():
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        now = datetime.now()
        one_hour_later = now + timedelta(hours=1)
        print("Current Time:", now.strftime('%Y-%m-%d %H:%M'))
        print("One Hour Later:", one_hour_later.strftime('%Y-%m-%d %H:%M'))

        cursor.execute(f"""SELECT task_ID, to_email, task, due_date
                            FROM {table_name}
                            WHERE due_date BETWEEN ? AND ?
                            AND status <> 'completed'
                            AND (last_notified IS NULL OR
                             last_notified < ?)""",
                       (now, one_hour_later, now - timedelta(hours=1)))
        tasks = cursor.fetchall()
        return tasks
    except Exception as e:
        print(f"An error occurred while fetching due tasks: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()


def update_last_notified(task_id):
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute(f"UPDATE {table_name} SET last_notified = ? "
                       "WHERE task_ID = ?", (now, task_id))
        conn.commit()
        print(f"Updated last_notified for ID {task_id} to {now}")
    except Exception as e:
        print(f"An error occurred while updating last_notified: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def complete_task_in_database(task_id):
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {table_name} SET status = 'completed' "
                       "WHERE task_ID = ?", (task_id,))
        conn.commit()
        print(f"Task with ID {task_id} marked as completed in the database.")
    except Exception as e:
        print(f"An error occurred while marking task as completed: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_last_inserted_id():
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(f"SELECT MAX(task_ID) FROM {table_name}")
        last_id = cursor.fetchone()[0]
        return last_id
    except Exception as e:
        print("An error occurred while fetching "
              f"the last inserted ID: {str(e)}")
        return None
    finally:
        cursor.close()
        conn.close()


def delete_task_from_database(task_id):
    conn_str = get_conn_str(db_name)
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} "
                       "WHERE task_ID = ?", (task_id,))
        conn.commit()
        print(f"Task with ID {task_id} deleted from the database.")
    except Exception as e:
        print(f"An error occurred while deleting task from database: {str(e)}")
    finally:
        cursor.close()
        conn.close()
