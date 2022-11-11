import json
from typing import List, Dict, Any, Callable

kt = True
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit
- 'd' to delete a book
- 'r' to mark a book read

What would you like to do? """
Book = Dict[str, str]
Operation = Callable[[List[Book], Book], Any]


def add_book():
    title: str = input("Title:").strip().title()
    author: str = input("Author:").strip().title()
    year: str = input("Year of publication:").strip()
    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year},Not read\n")


def get_all_books():
    books: List[Book] = []
    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read_status = book.strip().split(",")
            books.append({
                "title": title,
                "author": author,
                "year": year,
                "read": read_status
            })
    return books


def show_books(books: List[Book]):
    print()
    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['read']}")
    print()


def find_book():
    books: List[Book] = get_all_books()
    matching_book: List[Book] = []
    user_find_book = input("Enter book name:").strip().lower()
    for book in books:
        if user_find_book == book['title'].lower():
            matching_book.append(book)
    return matching_book


def delete_book(books: List[Book], book_to_delete: Book):
    books.remove(book_to_delete)


def mark_book(books: List[Book], book_to_update: Book):
    index = books.index(book_to_update)
    books[index]['read'] = "Read"


def update_reading_list(operator: Operation):
    books: List[Book] = get_all_books()
    matching_list: List[Book] = find_book()

    if matching_list:
        operator(books, matching_list[0])

        with open("books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")
    else:
        print("Sorry,we didn't find any books matching that title")
        print()


while kt:
    user_input = input(menu_prompt).strip().lower()
    if user_input == "q":
        print()
        print("You quit program")
        break
    elif user_input == "a":
        add_book()
    elif user_input == "l":
        reading_list = get_all_books()
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty")
            print()
    elif user_input == "s":
        find_list = find_book()
        if find_list:
            show_books(find_list)
        else:
            print("Sorry,we didn't find any books matching that title")
            print()
    elif user_input == "d":
        update_reading_list(delete_book)
    elif user_input == "r":
        update_reading_list(mark_book)
    else:
        print(f"{user_input} isn't a valid option")