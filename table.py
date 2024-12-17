import mysql.connector
from mysql.connector import Error

def create_table():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database='parthi_db'
        )

        if connection.is_connected():
            print("Connection established")

            cursor = connection.cursor()  # Create a cursor object

            # Create table query
            cursor.execute("""
                CREATE TABLE ariva (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(200),
                    age INT,
                    address VARCHAR(200),
                    phone_no VARCHAR(20)
                )
            """)
            print("Table 'ariva' created successfully")

    except Error as conn_error:
        print(f"Connection error: {conn_error}")

    finally:
        if connection.is_connected():
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
            print("MySQL connection closed")

# Call the function to create the table
create_table()



