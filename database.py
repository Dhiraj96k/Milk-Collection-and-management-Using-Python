import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('project_database.db')

# Create a cursor object
cursor = conn.cursor()

# Query to get the list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the tables
tables = cursor.fetchall()

# Print all tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
