import mysql.connector

# Step 1: Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host="localhost",    # Replace with your MySQL server host
        user="root",         # Replace with your MySQL username
        password="12345678"  # Replace with your MySQL password
    )

    # Step 2: Create a cursor object
    cursor = connection.cursor()

    # Step 3: Write an SQL query to create a database
    db_name = "my_new_database"
    create_db_query = f"CREATE DATABASE {db_name}"

    # Step 4: Execute the query
    cursor.execute(create_db_query)
    print(f"Database '{db_name}' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Step 5: Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
