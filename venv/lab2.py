class Book:
    
    id = 1
    
    def __init__(self, name: str, pages: int):
        self.id = Book.id
        Book.id += 1
        self.name = name
        self.pages = pages
        
    def __str__(self):
        return f'Книга: "{self.name}"'
        
    def __repr__(self):
        return f'Book(id = {self.id}, name = "{self.name}", pages = {self.pages})'

class Library:

    def __init__(self, data = None):
        if data is None:
            self.books = []
        self.books = data

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return self.books[-1]['id'] + 1

    def get_index_by_book_id(self, index):
        for i in range(len(self.books)):
            if self.books[i]['id'] == index:
                return i
            else:
                raise ValueError("Книги с запрашиваемым id не существует")
