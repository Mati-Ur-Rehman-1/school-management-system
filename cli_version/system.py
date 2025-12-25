Students=[]
def add_student():
     name =input("Enter Student name: ")
     f_name =input("Enter Father name: ")
     Class=input("Enter Class name: ")
     roll_no=input("Enter your roll_no: ")

     student = {
        "name": name,
        "f_name": f_name,
        "Class" : Class,
        "roll_no": roll_no
     }
     Students.append(student)
     print("\nStudent add successfully..\n")


def show_students():
     num = input("Enter your registered roll number : ")

     for i in Students:
         if num == i["roll_no"]:
             print(f"\nStudent name: {i['name']} | Father name: {i['f_name']} | Class: {i['Class']}\n")


def remove_students():
    num = input("Enter roll number: ")
    for i in Students:
        if num == i["roll_no"]:
         Students.remove(i)
         print("\nStudent removed\n")
        else:
         print("Wrong input")


def update_student():
        num = input("Enter roll number: ")
        for i in Students:
            if num == i["roll_no"]:
             i["name"] =input("Enter new name: ")
             i["f_name"] =input("Enter new Father name: ")
             i["Class"] =input("Enter new Class name: ")
             print("\nUpdated\n")
            else:
                print("wrong input")


def all_students():
    for i in Students:
       print(f"Student name: {i['name']} | Father name: {i['f_name']} | Class: {i['Class']} | Roll_no. {i['roll_no']}")



