from project1.user import User


class Library:
    def __init__(self):
        self.user_records = [User]
        self.books_available = {}   # author: available books
        self.rented_books = {}      # username: {book name: days_left}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, info in self.rented_books.items():
            for name, days in info.items():
                if name == book_name:
                    days_to_return = days
            return f'The book "{book_name}" is already rented and ' \
                   f'will be available in {days_to_return} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"






