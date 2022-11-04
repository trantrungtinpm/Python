import json

kt = True
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit
- 'd' to delete a book
- 'r' to mark a book read

What would you like to do? """


def add_book():
    books =get_all_books()
    title = input("Title:").strip().title()
    author = input("Author:").strip().title()
    year = input("Year of publication:").strip()

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": "Not read"
    })
    with open("books.json", "w") as reading_list:
        json.dump(books, reading_list)


def get_all_books():

    with open("books.json", "r") as reading_list:
        books = json.load(reading_list)
    return books


def create_book_file():
    try:
        with open("books.json", "x") as reading_list:
            json.dump([], reading_list)
    except FileExistsError:
        pass


def show_books(books):
    print()
    for book in books:
        print("{title}. by {author} ({year}) - {read}".format(**book))
    print()


def find_book():
    books = get_all_books()
    matching_book = []
    user_find_book = input("Enter book name:").strip().lower()
    for book in books:
        if user_find_book == book['title'].lower():
            matching_book.append(book)
    return matching_book


def delete_book(books, book_to_delete):
    books.remove(book_to_delete)


def mark_book(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Read"


def update_reading_list(operator):
    books = get_all_books()
    matching_list = find_book()

    if matching_list:
        operator(books, matching_list[0])

        with open("books.json", "w") as reading_list:
            json.dump(books, reading_list)

    else:
        print("Sorry,we didn't find any books matching that title")
        print()


create_book_file()

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
