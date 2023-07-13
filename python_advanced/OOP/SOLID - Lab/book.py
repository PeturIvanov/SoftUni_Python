from typing import List


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.page = 0

    def __repr__(self) -> str:
        return f"Title: {self.title}," \
               f" Author: {self.author}," \
               f" Pages: {self.pages}"

    @property
    def current_page(self):
        return f"You are on page {self.page} with content ..."

    def turn_page(self, page):
        if page > self.pages:
            raise ValueError(f"Invalid page!! The book has {self.pages}pages")

        self.page = page

        return self.current_page

    def next_page(self):
        if self.page + 1 > self.pages:
            return f"Congratulations you finish a book {self.title}"

        self.page += 1
        return self.current_page

class Library:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.books: List[Book] = []

    def __repr__(self):
        return f"Library: {self.name}," \
               f" Address: {self.address}," \
               f" Available books: ({', '.join([str(b) for b in self.books])})"

    def add_book(self, book: Book) -> str:
        self.books.append(book)

        return f"{book} added to the Library"

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            raise ValueError(f"Sorry we dont have book with title: {title}!")

b1 = Book("Warcraft", "Christie Golden", 350)
print(b1)
b1.next_page()
print(b1.current_page)
library = Library("Orange", "Paradise Center")
library.add_book(b1)
print(library.find_book("Warcraft"))
library.add_book(b1)
print(library)