

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title,author):
        book = Book(title,author)
        self.books.append(book)
        print(f"'{title}' added to the library.")

    def remove_book(self,title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"'{title}' removed")
                return
        print(f"'{title}' not found")

    def list_books(self):
        if not self.books:
            print("Library is empty")
        else:
            print("Available books")
            for book in self.books:
                print(f"- {book.title} by {book.author}")


library = Library()
library.add_book("python","nehal")
library.add_book("hamza","c++")
library.list_books()

library.remove_book("hamza")
library.list_books()