class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)

    def search_book(self):
        book = input("Enter book name to search: ")

        if book in self.books:
            print("Book found.")
        else:
            print("Book not found.")

    def remove_book(self):
        book = input("Enter book name to remove: ")

        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")


library = Library()

while True:

    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.search_book()

    elif choice == 4:
        library.remove_book()

    elif choice == 5:
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice.")