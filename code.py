import sqlite3

# Connect to Database
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

# ---------------- FUNCTIONS ---------------- #

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
    print("\n📋 STUDENT TABLE")
    print("=" * 40)
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()

    print(f"{'ID':<5} {'Name':<10} {'Branch':<10}")
    print("-" * 40)

    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<10}")
    print()


def view_marks():
    print("\n📊 MARKS TABLE")
    print("=" * 30)
    cursor.execute("SELECT * FROM Marks")
    rows = cursor.fetchall()

    print(f"{'ID':<5} {'Marks':<10}")
    print("-" * 30)

    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10}")
    print()


def average_marks():
    cursor.execute("SELECT AVG(marks) FROM Marks")
    avg = cursor.fetchone()[0]
    print(f"\n📈 Average Marks: {avg}\n")


def topper():
    cursor.execute("SELECT id, MAX(marks) FROM Marks")
    print("\n🏆 Topper (ID, Marks):", cursor.fetchone(), "\n")


def full_report():
    print("\n📊 FULL STUDENT REPORT")
    print("=" * 50)

    cursor.execute("""
    SELECT Students.id, Students.name, Students.branch, Marks.marks
    FROM Students
    JOIN Marks ON Students.id = Marks.id
    """)

    rows = cursor.fetchall()

    print(f"{'ID':<5} {'Name':<10} {'Branch':<10} {'Marks':<10}")
    print("-" * 50)

    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<10} {row[3]:<10}")
    print()


def search_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("SELECT * FROM Students WHERE id=?", (sid,))
    row = cursor.fetchone()

    if row:
        print(f"\n✅ Found: ID={row[0]}, Name={row[1]}, Branch={row[2]}\n")
    else:
        print("❌ Student Not Found\n")


def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    cursor.execute("DELETE FROM Students WHERE id=?", (sid,))
    cursor.execute("DELETE FROM Marks WHERE id=?", (sid,))
    conn.commit()
    print("🗑️ Student Deleted Successfully!\n")


# ---------------- MENU ---------------- #

while True:
    print("====== 🎓 Student Performance System ======")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Students")
    print("4. View Marks")
    print("5. Average Marks")
    print("6. Topper")
    print("7. Full Report")
    print("8. Search Student")
    print("9. Delete Student")
    print("10. Exit")

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
        full_report()
    elif choice == '8':
        search_student()
    elif choice == '9':
        delete_student()
    elif choice == '10':
        break
    else:
        print("❌ Invalid Choice\n")

conn.close()
