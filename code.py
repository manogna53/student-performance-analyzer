import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create tables
cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INTEGER, name TEXT, branch TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Marks (id INTEGER, marks INTEGER)")

# Insert data
cursor.execute("DELETE FROM Students")
cursor.execute("DELETE FROM Marks")

cursor.execute("INSERT INTO Students VALUES (1, 'Mahi', 'CSE')")
cursor.execute("INSERT INTO Students VALUES (2, 'Ravi', 'ECE')")

cursor.execute("INSERT INTO Marks VALUES (1, 85)")
cursor.execute("INSERT INTO Marks VALUES (2, 75)")

conn.commit()

# Fetch data
print('--- Students List ---')
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

# Average
cursor.execute("SELECT AVG(marks) FROM Marks")
print('Average Marks:', cursor.fetchone()[0])

conn.close()
