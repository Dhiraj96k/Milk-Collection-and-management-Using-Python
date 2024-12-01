import sqlite3

def describe_table():
    try:
        # Connect to your SQLite database
        conn = sqlite3.connect('project_database.db')
        cursor = conn.cursor()

        # Use PRAGMA to get table information
        cursor.execute("PRAGMA table_info(per_info);")

        # Fetch all the results
        columns = cursor.fetchall()

        # Display column details
        print("Table structure of 'milk_info':")
        for column in columns:
            print(f"Column Name: {column[1]}, Data Type: {column[2]}, Not Null: {column[3]}, Default Value: {column[4]}, Primary Key: {column[5]}")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if conn:
            conn.close()

# Run the function
describe_table()
