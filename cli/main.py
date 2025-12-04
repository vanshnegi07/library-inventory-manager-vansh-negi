"""
gradebook.py
Simple GradeBook Analyzer CLI
Name: Vansh Negi
Course: B.Tech CSE AI & ML - 1st Year
Section: A
Enrollment Number: 2501730158
Subject: Programming for Problem Solving using Python
# I made this for Lab Assignment 3
"""


# cli/main.py
import sys
from pathlib import Path
# allow running with "python cli/main.py" too
sys.path.append(str(Path(__file__).resolve().parent.parent))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def input_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Please enter something.")

def main():
    inv = LibraryInventory("catalog.json")
    while True:
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Issue book")
        print("3. Return book")
        print("4. View all books")
        print("5. Search by title")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            title = input_nonempty("Title: ")
            author = input_nonempty("Author: ")
            isbn = input_nonempty("ISBN: ")
            try:
                b = Book(title, author, isbn)
                inv.add_book(b)
                print("Book added :)")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            isbn = input_nonempty("ISBN to issue: ")
            try:
                ok = inv.issue_book(isbn)
                if ok:
                    print("Issued successfully.")
                else:
                    print("Book was already issued.")
            except LookupError as e:
                print("Error:", e)

        elif choice == "3":
            isbn = input_nonempty("ISBN to return: ")
            try:
                ok = inv.return_book(isbn)
                if ok:
                    print("Returned successfully.")
                else:
                    print("Book was not issued.")
            except LookupError as e:
                print("Error:", e)

        elif choice == "4":
            books = inv.all_books()
            if not books:
                print("No books found.")
            else:
                for i, b in enumerate(books, 1):
                    print(f"{i}. {b}")

        elif choice == "5":
            q = input_nonempty("Enter title keyword: ")
            res = inv.search_by_title(q)
            if res:
                for b in res:
                    print(b)
            else:
                print("No match found.")

        elif choice == "6":
            print("Bye!")
            sys.exit(0)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
