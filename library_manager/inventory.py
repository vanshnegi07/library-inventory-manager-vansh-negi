import json
import os
from library_manager.book import Book

class LibraryInventory:
    def __init__(self, storage_file="catalog.json"):
        self.storage_file = storage_file
        self.books = []
        self.load()

    def add_book(self, book):
        if self.find_by_isbn(book.isbn):
            raise ValueError("ISBN already exists")
        self.books.append(book)
        self.save()

    def find_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_by_title(self, q):
        q = q.strip().lower()
        return [b for b in self.books if q in b.title.lower()]

    def all_books(self):
        return self.books

    def issue_book(self, isbn):
        b = self.find_by_isbn(isbn)
        if not b:
            raise LookupError("Book not found")
        changed = b.issue()
        if changed:
            self.save()
        return changed

    def return_book(self, isbn):
        b = self.find_by_isbn(isbn)
        if not b:
            raise LookupError("Book not found")
        changed = b.return_book()
        if changed:
            self.save()
        return changed

    def load(self):
        if not os.path.exists(self.storage_file):
            self.books = []
            return
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book.from_dict(d) for d in data]
        except Exception:
            self.books = []

    def save(self):
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
        except Exception:
            pass
