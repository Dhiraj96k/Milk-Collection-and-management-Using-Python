import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('project_database.db')

# Create a cursor object
cursor = conn.cursor()

# List of data to be inserted
data = [
    (1, 'Shubham Tanmay Jamble', '9099590599', 'shubhamjamble@gmail.com'),
    (2, 'Jaydeep Bengare', '8308410205', 'jaydeepbengare@gmail.com'),
    (3, 'Tejas Jadhav', '9552043157', 'tejasjadhav@gmail.com'),
    (4, 'Dhiraj Salunke', '7350397408', 'dhirajsalunke@gmail.com')
]

# Insert multiple records using a parameterized query
cursor.executemany('''
INSERT INTO per_info (code, name, mobno, email) 
VALUES (?, ?, ?, ?)
''', data)

# Commit the transaction to save the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully into the 'per_info' table.")
