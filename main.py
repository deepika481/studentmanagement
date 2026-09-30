from  app.database import Database
from  app.student_service import StudentService


def main():
    service = StudentService(Database())

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = int(input("Student ID: "))
                name = input("Name: ")
                age = int(input("Age: "))
                course = input("Course: ")
                service.add_student(sid, name, age, course)
                print("Student added successfully")

            elif choice == "2":
                for student in service.get_all_students():
                    print(student)

            elif choice == "3":
                sid = int(input("Student ID: "))
                print(service.get_student(sid) or "Not found")

            elif choice == "4":
                sid = int(input("Student ID: "))
                name = input("New name: ")
                age = int(input("New age: "))
                course = input("New course: ")
                if service.update_student(sid, name, age, course):
                    print("Student updated")
                else:
                    print("Student not found")

            elif choice == "5":
                sid = int(input("Student ID: "))
                if service.delete_student(sid):
                    print("Student deleted")
                else:
                    print("Student not found")

            elif choice == "6":
                break

            else:
                print("Invalid choice")

        except (ValueError, Exception) as error:
            print("Error:", error)