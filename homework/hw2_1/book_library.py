import random
class Book:
    def __init__(self, zagolovok, avtor):
        self.title = zagolovok
        self.author = avtor

    def display(self):
        print('Имя: {}. автор: {}'.format(self.title, self.author))

library = []


for i in range(1, 501):
    book_title = f"Книга {i}"
    book_author = f"Автор {i}"

    new_book = Book(book_title, book_author)
    library.append(new_book)

for i in library:
    print(i.display())
