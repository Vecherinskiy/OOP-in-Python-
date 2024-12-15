BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(id_={self.id}, "
            f"name='{self.name}', "
            f"pages={self.pages})"
        )


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, id_) -> int:
        if type(id_) != int:
            raise TypeError("id_ must be an integer")
        if id_ < 0 or id_ > len(self.books):
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            for ind, book in enumerate(self.books):
                if book.id == id_:
                    return ind


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())

    list_books = [
        Book(
            id_=book_dict["id"],
            name=book_dict["name"],
            pages=book_dict["pages"]
        ) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))
