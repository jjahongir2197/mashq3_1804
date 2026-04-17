class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            b.display()
            print("-----------")


def main():
    b1 = Book("Python Basics", "John", 250)
    b2 = Book("Flask Guide", "Mike", 300)

    lib = Library()

    lib.add_book(b1)
    lib.add_book(b2)

    lib.show_books()


main()
