# Part 1: Create the Library class
class Library:
    _book_list = []  # Private class attribute

    @classmethod
    def entry_book(cls, book):
        """Inserts a Book object into the book_list."""
        cls._book_list.append(book)
        print(f"Book '{book._title}' by '{book._author}' has been added to the library.")

# Part 2, 3: Create and Initialize the Book class
class Book:
    def __init__(self, book_id, title, author):
        # Part 9: Data Privacy
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True  # Initially, a book is always available

        # Part 3: Initialize Book Object
        Library.entry_book(self)

    # Part 4: Implement borrow_book() method
    def borrow_book(self):
        """Checks and changes the book's availability to False."""
        if self._availability:
            self._availability = False
            print(f"You have successfully borrowed '{self._title}'.")
            return True
        else:
            print(f"Sorry, '{self._title}' is currently not available for borrowing.")
            return False

    # Part 5: Implement return_book() method
    def return_book(self):
        """Changes the book's availability back to True."""
        if not self._availability:
            self._availability = True
            print(f"You have successfully returned '{self._title}'.")
            return True
        else:
            print(f"This book, '{self._title}', was not borrowed.")
            return False

    # Part 6: Implement view_book_info() method
    def view_book_info(self):
        """Displays the details of the book."""
        status = "Available" if self._availability else "Not Available"
        print(f"Book ID: {self._book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Status: {status}")

# Part 3: Manual Book Initialization
# Create some book objects to populate the library
book1 = Book("001", "The Alchemist", "Paulo Coelho")
book2 = Book("002", "1984", "George Orwell")
book3 = Book("003", "To Kill a Mockingbird", "Harper Lee")
book4 = Book("004", "The Great Gatsby", "F. Scott Fitzgerald")
book5 = Book("005", "Brave New World", "Aldous Huxley")

# Part 7: Menu System
def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                print("\n--- All Books ---")
                if not Library._book_list:
                    print("No books in the library.")
                else:
                    for book in Library._book_list:
                        book.view_book_info()
                        print("-" * 20)

            elif choice == "2":
                book_id = input("Enter the Book ID to borrow: ")
                # Part 8: Error Handling for Invalid book ID
                book_to_borrow = None
                for book in Library._book_list:
                    if book._book_id == book_id:
                        book_to_borrow = book
                        break
                if book_to_borrow:
                    # Part 8: Error Handling for already borrowed book is handled inside borrow_book()
                    book_to_borrow.borrow_book()
                else:
                    print("Error: Invalid Book ID. Please try again.")

            elif choice == "3":
                book_id = input("Enter the Book ID to return: ")
                # Part 8: Error Handling for Invalid book ID
                book_to_return = None
                for book in Library._book_list:
                    if book._book_id == book_id:
                        book_to_return = book
                        break
                if book_to_return:
                    # Part 8: Error Handling for not borrowed book is handled inside return_book()
                    book_to_return.return_book()
                else:
                    print("Error: Invalid Book ID. Please try again.")

            elif choice == "4":
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()