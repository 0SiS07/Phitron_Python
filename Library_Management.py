class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"You have borrowed this book: {self._title}")
        else:
            print(f"You already borrowed this book: {self._title}")

    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"You have returned this book: {self._title}")
        else:
            print(f"You did not borrow this book: {self._title}")

    def view_book_info(self):
        if self._availability:
            availability_status = "Available"
        else:
            availability_status = "Not Available"

        print(f"\nBook ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Availability: {availability_status}")

def view_all_books():
    for book in Library.book_list:
        book.view_book_info()

def borrowed_book(book_id):
    for book in Library.book_list:
        if book._book_id == book_id:
            book.borrow_book()
            return book
    print("Invalid book ID. Enter correct ID")


def returned_book(book_id):
    for book in Library.book_list:
        if book._book_id == book_id:
            book.return_book()
            return book
    print("Invalid book ID. Enter correct ID")


def menu():
    while True:
        print("\nChoose your option:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        options = input("\nEnter your choice: ")

        if options == '1':
            view_all_books()
        elif options == '2':
            book_id = int(input("Enter the Book ID to borrow: "))
            borrowed_book(book_id)
        elif options == '3':
            book_id = int(input("Enter the Book ID to return: "))
            returned_book(book_id)
        elif options == '4':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Enter correct input")

book1 = Book(101, "Python Crash Course", "Eric Matthes")
book2 = Book(102, "Head First Python", "Paul Barry")
book3 = Book(103, "A Byte of Python", "C. H. C H Swaroop")
book3 = Book(104, "Python for Data Analysis", "Wes McKinney")
book3 = Book(105, "Learning Python", "Mark Lutz, David Ascher")
menu()