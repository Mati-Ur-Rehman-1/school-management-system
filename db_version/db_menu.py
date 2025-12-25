from db_system import add_student, show_students,remove_students,update_student,all_students

print("\nwelcome to School management System\n")
while True:
        print("1. For Add new Student\n2. For Show student \n3. For remove Student \n4. For update Student\n5. For all data\n6. For exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
             add_student()
        elif choice == 2:
          show_students()
        elif choice == 3:
            remove_students()
        elif choice == 4:
            update_student()
        elif choice == 5:
            all_students()
        elif choice == 6:
            break
        else:
            print("\nwrong input, try again\n")