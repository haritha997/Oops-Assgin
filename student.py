import random
import json
import os

if not os.path.exists('students.json'):
    with open('students.json', 'w') as f:
        json.dump({}, f)

def add_student():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    try:
        with open('students.json', 'r+') as f:
            data = json.load(f)
            if roll_number in data:
                print("Roll number already exists!")
            else:
                data[roll_number] = {"name": name, "marks": int(marks)}
                f.seek(0)
                json.dump(data, f)
                f.truncate()
                print("Student record added successfully!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except ValueError:
        print("Error: Invalid data type!")

def view_students():
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            print("Student Records:")
            for roll_number, student in data.items():
                print(f"Roll No: {roll_number}, Name: {student['name']}, Marks: {student['marks']}")
    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")

def search_student():
    roll_number = input("Enter Roll Number to search: ")

    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
            if roll_number in data:
                student = data[roll_number]
                print(f"Student Found: Name: {student['name']}, Marks: {student['marks']}")
            else:
                print("Roll number not found!")
    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")

def exit_program():
    print("Exiting program. Goodbye!")

def main():
    while True:
        print("\nWelcome to Student Management System")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Search Student by Roll Number")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()