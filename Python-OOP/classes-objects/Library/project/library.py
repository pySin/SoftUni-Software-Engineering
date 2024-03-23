from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                self.rented_books[user.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            for check_user in self.rented_books:
                # print(check_user)
                for current_book in self.rented_books[check_user]:
                    if current_book == book_name:
                        return f'The book "{book_name}" is already rented and will be available ' \
                               f'in {self.rented_books[check_user][current_book]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
