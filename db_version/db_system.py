from database import connection


def add_student():
     name =input("Enter Student name: ")
     f_name =input("Enter Father name: ")
     Class=input("Enter Class name: ")
     roll_no=int(input("Enter your roll_no: "))

     conn = connection()
     cur = conn.cursor()

     cur.execute("""
         INSERT INTO student (roll_no, name, f_name, class_name)
         VALUES (%s, %s, %s, %s)
     """, (roll_no, name, f_name, Class))

     conn.commit()
     cur.close()
     conn.close()


     print("\nStudent added successfully..\n")

def show_students():
     num = int(input("Enter your registered roll number : "))

     conn = connection()
     cur = conn.cursor()

     cur.execute("SELECT name, f_name, class_name FROM student WHERE roll_no = %s", (num,))
     student = cur.fetchone()

     cur.close()
     conn.close()
     if student:
             print(f"\nStudent name: {student[0]} | Father name: {student[1]} | Class: {student[2]}\n")
     else:
         print("\nStudent not found\n")


def remove_students():
    num = int(input("Enter roll number: "))
    conn = connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM student WHERE roll_no = %s", (num,))
    conn.commit()
    if cur.rowcount > 0:
     print("\nStudent removed\n")
    else:
     print("\nWrong input\n")

    cur.close()
    conn.close()

def update_student():
    num = int(input("Enter roll number: "))

    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student WHERE roll_no = %s", (num,))
    if not cur.fetchone():
        print("\nRoll number not found.\n")
        cur.close()
        conn.close()
        return

    name = input("Enter new name: ")
    f_name = input("Enter new Father name: ")
    class_name = input("Enter new Class name: ")

    cur.execute("""
        UPDATE student SET name=%s, f_name=%s, class_name=%s WHERE roll_no=%s
    """, (name, f_name, class_name, num))

    conn.commit()
    cur.close()
    conn.close()
    print("\nUpdated successfully!\n")


def all_students():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name, f_name, class_name, roll_no FROM student")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    for i in rows:
        print(f"\nStudent name: {i[0]} | Father name: {i[1]} | Class: {i[2]} | Roll_no: {i[3]}\n")



