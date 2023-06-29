from library.user import User
from library.library import Library


class Registration:
    @staticmethod
    def add_user(user: User, library: Library) -> str or None:
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library) -> None or str:
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library) -> str:
        try:
            user = next(filter(lambda u: user_id == u.user_id, library.user_records))

        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username != new_username:
            if user.username in library.rented_books:
                library.rented_books[new_username] = library.rented_books[user.username]
                del library.rented_books[user.username]

            user.username = new_username

            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return "Please check again the provided username - it should be different than the username " \
               "used so far!"


import unittest


class TestsUser(unittest.TestCase):
    def setUp(self):
        self.user = User(12, 'Valentina')
        self.library = Library()
        self.register = Registration()

    # LIBRARY CLASS TESTS
    def test_get_book_method_with_book_available_in_the_library_should_add_it_in_the_books_list(self):
        self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Deathly Hallows',
                                                             'Harry Potter and the Order of the Phoenix']})
        result = self.library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.user)
        self.assertEqual(result, 'Harry Potter and the Deathly Hallows successfully rented for the next 17 days!')
        self.assertEqual(self.user.books, ["Harry Potter and the Deathly Hallows"])
        self.assertEqual(self.library.rented_books, {'Valentina': {'Harry Potter and the Deathly Hallows': 17}})
        self.assertEqual(self.library.books_available, {'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
                                                                        'Harry Potter and the Philosopher\'s Stone',
                                                                        'Harry Potter and the Order of the Phoenix']})

    def test_get_book_method_with_book_already_rented_should_return_a_message(self):
        self.library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Philosopher\'s Stone',
                                                             'Harry Potter and the Deathly Hallows',
                                                             'Harry Potter and the Order of the Phoenix']})
        self.library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.user)
        second_user = User(13, 'Peter')
        result = self.library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17, self.user)
        self.assertEqual(result,
                         'The book "Harry Potter and the Deathly Hallows" is already rented and will be available in 17 days!')
        self.assertEqual(self.user.books, ["Harry Potter and the Deathly Hallows"])
        self.assertEqual(second_user.books, [])
        self.assertEqual(self.library.rented_books, {'Valentina': {'Harry Potter and the Deathly Hallows': 17}})
        self.assertEqual(self.library.books_available, {'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
                                                                        'Harry Potter and the Philosopher\'s Stone',
                                                                        'Harry Potter and the Order of the Phoenix']})

