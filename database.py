import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('project_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the SELECT query
cursor.execute("SELECT * FROM per_info")

# Fetch all results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
