import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('project_database.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 4: Insert data including the 'password' column
cursor.execute('''
INSERT INTO admin (username, email, password) 
VALUES (?, ?, ?)
''', ('admin-dhiraj', 'dhirajsalunke7350@gmail.com', 'admin-login'))

# Step 5: Commit the changes
conn.commit()

# Step 6: Verify the inserted data
cursor.execute('SELECT * FROM admin')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Step 7: Close the connection
conn.close()

