class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.title for book in self.books]

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return f"{book.title}! was found"
        return "No such book!"

lib = Library()
b1 = Book("Street Smart Entrepreneur")
lib.add_book(b1)

print(lib.list_books())
print(lib.find_book("Street Smart Entrepreneur"))
