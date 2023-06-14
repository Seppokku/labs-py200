class Book:
    def __init__(self, name:str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f'Книга: "{self._name}, {self._author}"'

    def __repr__(self):
        return f'Book(name = "{self._name}", author = {self._author})'


class PaperBook(Book):
    def __init__(self, name, author, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('количество страниц должно быть int')
        if pages <= 0:
            raise ValueError('количество страниц должно быть больше нуля')
        self.pages = pages

    def __str__(self):
        return f'Книга: "{self._name}, {self._author}, {self.pages} страниц"'

    def __repr__(self):
        return f'PaperBook(name = "{self._name}", author = {self._author}, pages = {self.pages})'

class AudioBook(Book):
    def __init__(self, name, author, duration: float):
        if not isinstance(duration, float):
            raise TypeError('продолжительность должна быть типа float')
        if duration <= 0:
            raise ValueError('продолжительность книги должна быть больше нуля')
        super().__init__(name, author)
        self.duration = duration


    def __str__(self):
        return f'Книга: "{self._name}", {self._author} продолжительностью {self.duration}"'

    def __repr__(self):
        return f'AudioBook(name = "{self._name}", author = {self._author}, duration = {self.duration})'



