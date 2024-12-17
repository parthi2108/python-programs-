import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678"
    )

    if conn.is_connected():
        print("Connected to MySQL Server")

        cursor = conn.cursor()
        create_db_query = "CREATE DATABASE IF NOT EXISTS parthi_db"

        try:
            cursor.execute(create_db_query)
            print("Database 'parthi_db' created successfully")
        except Error as query_error:
            print(f"Error executing query: {query_error}")

except Error as conn_error:
    print(f"conn error: {conn_error}")

# finally:
#     if conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("MySQL conn closed") 



