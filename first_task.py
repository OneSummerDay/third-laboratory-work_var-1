class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_number, book_info):
        self.books[book_number] = book_info

    def remove_book(self, book_number):
        if book_number in self.books:
            del self.books[book_number]
            print(f"Книга з порядковим номером {book_number} видалена з бібліотеки.")
        else:
            print(f"Книга з порядковим номером {book_number} відсутня в бібліотеці.")

    def search_books(self, search_params):
        found_books = []
        for book_number, book_info in self.books.items():
            match = all(book_info.get(param) == value for param, value in search_params.items())
            if match:
                found_books.append((book_number, book_info))
        return found_books

    def access_book(self, book_number):
        return self.books.get(book_number, None)


library = Library()

# Adding books
library.add_book(1, {"author": "Жюль Верн", "title": "10000 льє під водою", "publisher": "Видавництво1", "genre": "Фантастика", "year": 1937})
library.add_book(2, {"author": "Саббатини", "title": "Одисея Капітана Блада", "publisher": "Видавництво2", "genre": "Роман", "year": 1911})
library.add_book(3, {"author": "Шевченко", "title": "Заповіт", "publisher": "Видавництво3", "genre": "Роман", "year": 1863})

# Searching
search_params = {"author": "Жюль Верн", "genre": "Фантастика"}
result_books = library.search_books(search_params)
print("Результати пошуку:")
for book_number, book_info in result_books:
    print(f"Книга {book_number}: {book_info}")

# Searching with an id
book_number_to_access = 2
accessed_book = library.access_book(book_number_to_access)
print(f"\nДоступ до книги за номером {book_number_to_access}: {accessed_book}")

# Remove book with an id
book_number_to_remove = 1
library.remove_book(book_number_to_remove)


