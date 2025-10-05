class Library:
    # class attribute
    __book_list = []

    @classmethod
    def entry_book(cls, book_obj):
        """Insert book object into book_list"""
        cls.__book_list.append(book_obj)

    @classmethod
    def get_all_books(cls):
        """Return all books in the library"""
        return cls.__book_list

    @classmethod
    def find_book(cls, book_id):
        """Find book by ID"""
        for book in cls.__book_list:
            if book.get_book_id() == book_id:
                return book
        return None


class Book:
    def __init__(self, book_id, title, author, availability=True):
        # private attributes
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

        # Insert book into Library when created
        Library.entry_book(self)

    # ------------------- Getter Methods -------------------
    def get_book_id(self):
        return self.__book_id

    def is_available(self):
        return self.__availability

    # ------------------- Book Actions -------------------
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"✅ '{self.__title}' borrowed successfully!")
        else:
            print(f"❌ '{self.__title}' is already borrowed!")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"✅ '{self.__title}' returned successfully!")
        else:
            print(f"❌ '{self.__title}' was not borrowed!")

    def view_book_info(self):
        status = "Available" if self.__availability else "Borrowed"
        print(f"ID: {self.__book_id}, Title: {self.__title}, "
              f"Author: {self.__author}, Status: {status}")


# ------------------- Menu Driven System -------------------

# Sample Books
b1 = Book(1, "Python Programming", "John Doe")
b2 = Book(2, "Data Structures", "Jane Smith")
b3 = Book(3, "Machine Learning", "Andrew Ng")

while True:
    print("\n====== Library Menu ======")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("\n📚 All Books:")
        for book in Library.get_all_books():
            book.view_book_info()

    elif choice == "2":
        try:
            book_id = int(input("Enter Book ID to borrow: "))
            book = Library.find_book(book_id)
            if book:
                book.borrow_book()
            else:
                print("❌ Invalid Book ID!")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    elif choice == "3":
        try:
            book_id = int(input("Enter Book ID to return: "))
            book = Library.find_book(book_id)
            if book:
                book.return_book()
            else:
                print("❌ Invalid Book ID!")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    elif choice == "4":
        print("👋 Exiting Library System. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")
