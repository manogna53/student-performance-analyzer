import sqlite3

# Connect DB
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Marks (
    id INTEGER,
    marks INTEGER
)
""")

conn.commit()

# Functions
def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    cursor.execute("INSERT INTO Students VALUES (?, ?, ?)", (id, name, branch))
    conn.commit()
    print("✅ Student Added Successfully!\n")

def add_marks():
    id = int(input("Enter Student ID: "))
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO Marks VALUES (?, ?)", (id, marks))
    conn.commit()
    print("✅ Marks Added!\n")

def view_students():
    print("\n📋 STUDENT LIST")
    print("-" * 30)
    for row in cursor.execute("SELECT * FROM Students"):
        print(f"ID: {row[0]} | Name: {row[1]} | Branch: {row[2]}")
    print()

def view_marks():
    print("\n📊 MARKS LIST")
    print("-" * 30)
    for row in cursor.execute("SELECT * FROM Marks"):
        print(f"ID: {row[0]} | Marks: {row[1]}")
    print()

def average_marks():
    cursor.execute("SELECT AVG(marks) FROM Marks")
    avg = cursor.fetchone()[0]
    print(f"\n📈 Average Marks: {avg}\n")

def topper():
    cursor.execute("SELECT id, MAX(marks) FROM Marks")
    print("\n🏆 Topper (ID, Marks):", cursor.fetchone(), "\n")

# Menu
while True:
    print("====== 🎓 Student Performance System ======")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Students")
    print("4. View Marks")
    print("5. Average Marks")
    print("6. Topper")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_marks()
    elif choice == '3':
        view_students()
    elif choice == '4':
        view_marks()
    elif choice == '5':
        average_marks()
    elif choice == '6':
        topper()
    elif choice == '7':
        break
    else:
        print("❌ Invalid Choice\n")

conn.close()
