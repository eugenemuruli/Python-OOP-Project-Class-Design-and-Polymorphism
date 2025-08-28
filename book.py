# book.py
from datetime import datetime
from typing import List


class Book:
    """Base class representing a book."""
    
    def __init__(self, title: str, author: str, pub_year: int) -> None:
        if pub_year > datetime.now().year:
            raise ValueError("Publication year cannot be in the future.")
        self._title = title
        self._author = author
        self._pub_year = pub_year

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Author cannot be empty.")
        self._author = value

    @property
    def pub_year(self) -> int:
        return self._pub_year

    @pub_year.setter
    def pub_year(self, value: int) -> None:
        if value > datetime.now().year:
            raise ValueError("Publication year cannot be in the future.")
        self._pub_year = value

    def age(self) -> int:
        return datetime.now().year - self._pub_year

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.pub_year})'

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pub_year={self.pub_year})"


class EBook(Book):
    """Subclass for electronic books."""
    
    def __init__(self, title: str, author: str, pub_year: int, file_format: str) -> None:
        super().__init__(title, author, pub_year)
        if file_format.upper() not in ['PDF', 'EPUB', 'MOBI', 'AZW']:
            raise ValueError("Unsupported format. Use: PDF, EPUB, MOBI, AZW.")
        self._file_format = file_format.upper()

    @property
    def file_format(self) -> str:
        return self._file_format

    @file_format.setter
    def file_format(self, value: str) -> None:
        if value.upper() not in ['PDF', 'EPUB', 'MOBI', 'AZW']:
            raise ValueError("Unsupported format.")
        self._file_format = value.upper()

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.pub_year}) [EBook - {self.file_format}]'

    def __repr__(self) -> str:
        return f"EBook(title={self.title!r}, author={self.author!r}, pub_year={self.pub_year}, file_format={self.file_format!r})"


class Audiobook(Book):
    """Subclass for audiobooks."""
    
    def __init__(self, title: str, author: str, pub_year: int, duration_minutes: float) -> None:
        super().__init__(title, author, pub_year)
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive.")
        self._duration_minutes = duration_minutes

    @property
    def duration_minutes(self) -> float:
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Duration must be positive.")
        self._duration_minutes = value

    def duration_hours(self) -> float:
        return round(self._duration_minutes / 60, 2)

    def __str__(self) -> str:
        return f'"{self.title}" by {self.author} ({self.pub_year}) [Audiobook - {self.duration_minutes} min]'

    def __repr__(self) -> str:
        return f"Audiobook(title={self.title!r}, author={self.author!r}, pub_year={self.pub_year}, duration_minutes={self.duration_minutes})"