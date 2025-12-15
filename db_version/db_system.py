from database import connection

Students=[]
def add_student():
     name =input("Enter Student name: ")
     f_name =input("Enter Father name: ")
     Class=input("Enter Class name: ")
     roll_no=input("Enter your roll_no: ")

     conn = connection()
     cur = conn.cursor()

     cur.execute("""
         INSERT INTO students (roll_no, name, f_name, class_name)
         VALUES (%s, %s, %s, %s)
     """, (roll_no, name, f_name, Class))

     conn.commit()
     cur.close()
     conn.close()


     print("Student add successfully..\n")

def show_students():
     num = input("Enter your registered roll number : ")

     conn = connection()
     cur = conn.cursor()

     cur.execute("SELECT name, f_name, class_name FROM students WHERE roll_no = %s", (num,))
     student = cur.fetchone()

     cur.close()
     conn.close()
     if num == student["roll_no"]:
             print(f"Student name: {student['name']} | Father name: {student['f_name']} | Class: {student['Class']}")


def remove_students():
    num = input("Enter roll number: ")
    conn = connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE roll_no = %s", (num,))
    conn.commit()
    if cur.rowcount > 0:
     print("Student removed")
    else:
     print("Wrong input")


def update_student():
    num = input("Enter roll number: ")

    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE roll_no = %s", (num,))
    if not cur.fetchone():
        print("Roll number not found.")
        cur.close()
        conn.close()
        return

    name = input("Enter new name: ")
    f_name = input("Enter new Father name: ")
    class_name = input("Enter new Class name: ")

    cur.execute("""
        UPDATE students SET name=%s, f_name=%s, class_name=%s WHERE roll_no=%s
    """, (name, f_name, class_name, num))

    conn.commit()
    cur.close()
    conn.close()
    print("Updated successfully!")


def all_students():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name, f_name, class_name, roll_no FROM students")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    for i in rows:
        print(f"Student name: {i[0]} | Father name: {i[1]} | Class: {i[2]} | Roll_no: {i[3]}")



