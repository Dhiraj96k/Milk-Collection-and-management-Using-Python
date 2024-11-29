import sqlite3

# Function to query the milk_info table based on code
def query_milk_info_by_code(code):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('project_database.db')
        cursor = conn.cursor()

        # SQL query with a placeholder for the code
        query = "SELECT * FROM milk_info WHERE code = ?"

        # Execute the query with the provided code
        cursor.execute(query, (code,))

        # Fetch all rows that match the condition
        results = cursor.fetchall()

        # Check if any records were returned
        if results:
            print(f"Records found for code {code}:")
            for row in results:
                print(row)
        else:
            print(f"No records found for code {code}.")

        # Close the connection
        conn.close()

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")

# Example usage: Query milk_info table with a specific code
query_milk_info_by_code(5)  