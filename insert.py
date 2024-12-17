import mysql.connector
from mysql.connector import Error

# def insert_table():

def view_table():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database='parthi_db'
        )

        if connection.is_connected():
            print("Connection established")

            cursor = connection.cursor()

            # SQL query and values
            # sql = "INSERT INTO ariva (name, age, address, phone_no) VALUES (%s, %s, %s, %s)"
            # val = [
            #     ('Arjun', 25, '123 Park Avenue', '9876543210'),
            #     ('Bhavana', 30, '456 Maple Street', '9876543211'),
            #     ('Charan', 22, '789 Oak Avenue', '9876543212'),
            #     ('Deepika', 28, '321 Elm Street', '9876543213'),
            #     ('Eshan', 35, '654 Pine Lane', '9876543214'),
            #     ('Farah', 26, '876 Birch Boulevard', '9876543215'),
            #     ('Girish', 29, '135 Cedar Road', '9876543216'),
            #     ('Hema', 24, '246 Willow Drive', '9876543217'),
            #     ('Ishan', 32, '369 Walnut Way', '9876543218'),
            #     ('Janvi', 27, '987 Cherry Circle', '9876543219'),
            #     ('Karan', 31, '741 Maple Avenue', '9876543220'),
            #     ('Leena', 23, '852 Aspen Court', '9876543221'),
            #     ('Mohan', 34, '963 Fir Terrace', '9876543222'),
            #     ('Nisha', 28, '147 Redwood Street', '9876543223'),
            #     ('Omkar', 26, '258 Spruce Way', '9876543224'),
            #     ('Priya', 30, '369 Magnolia Path', '9876543225'),
            #     ('Rohan', 29, '123 Sequoia Avenue', '9876543226'),
            #     ('Sneha', 25, '456 Sycamore Lane', '9876543227'),
            #     ('Tarun', 33, '789 Alder Boulevard', '9876543228'),
            #     ('Vidya', 27, '321 Palm Drive', '9876543229')
            # ]

            # # Execute the SQL query
            # cursor.executemany(sql, val)

            # # Commit changes
            # connection.commit()

            # print("Data inserted successfully")


            cursor.execute("select * from ariva")

            result = cursor.fetchall()

    except Error as conn_error:
        print(f"Connection error: {conn_error}")

    finally:
        if connection.is_connected():
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
            print("MySQL connection closed")

# Call the function to insert the data
view_table()
