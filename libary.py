import json
import os

if not os.path.exists('library.json'):
    with open('library.json', 'w') as f:
        json.dump({}, f)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    
    try:
        copies_available = int(input("Enter number of copies available: "))  
    except ValueError:
        print("Error: Copies available must be a number!")
        return

    try:
        with open('library.json', 'r') as f:
            data = json.load(f)

        if title in data:
            print("This book already exists!")
            return

        data[title] = {"title": title, "author": author, "isbn": isbn, "copies_available": copies_available}

        with open('library.json', 'w') as f:
            json.dump(data, f, indent=4)  

        print("Your book was added successfully!")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def remove_book():
    title = input("Enter book title: ")
    try:
        with open('library.json', 'r') as f:
            data = json.load(f)
        if title in data:
            del[title]
            return  print("Your book was removed successfully!")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except Exception as e:
        print(f"Unexpected Error: {e}")        

def view_book_records():
    try:
        with open('library.json', 'r') as f:
            data = json.load(f)

        if not data:
            print("No books found in the library!")
            return

        print("\nLibrary Records:")
        for title, book in data.items():
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Copies Available: {book['copies_available']}")

    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")

def search_isbn():
    isbn = input("Enter book ISBN to search: ")
    
    try:
        with open('library.json', 'r') as f:
            data = json.load(f)

        for book in data.values():
            if book['title'] == isbn:
                print(f"Book Found: Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Copies Available: {book['copies_available']}")
                return
        print("Book with the given ISBN not found!")

    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")

def exit_program():
    print("Exiting program. Goodbye!")

def main():
    while True:
        print("\nWelcome to Library Management System")
        print("1. Add a new book record")
        print("2. remove a book")
        print("3. Display all book records")
        print("4. Search for a book by ISBN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2" :
            remove_book()
        elif choice == "3":
            view_book_records()
        elif choice == "4":
            search_isbn()
        elif choice == "5":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
