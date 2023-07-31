from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(10)
        self.store.availability_in_store_by_book_titles = {"Warcraft": 3,
                                                           "Club five in the morning": 2,
                                                           "Sherlock Holmes": 1}

    def test_correct_initialization(self):
        store = Bookstore(5)
        self.assertEqual(5, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store._Bookstore__total_sold_books)
        self.assertEqual(5, store._Bookstore__books_limit)

    def test_total_sold_books_getter_return_correct_data(self):
        self.assertEqual(self.store.total_sold_books, self.store._Bookstore__total_sold_books)
        self.assertEqual(0, self.store.total_sold_books)


    def test_books_limit_setter_with_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = -1
        expected_message = "Books limit of -1 is not valid"
        self.assertEqual(expected_message, str(ex.exception))

    def test_books_limit_setter_with_zero_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = 0
        expected_message = "Books limit of 0 is not valid"
        self.assertEqual(expected_message, str(ex.exception))


    def test_dunder_len_method(self):
        result = len(self.store)
        self.assertEqual(6, result)

    def test_receive_new_book_with_not_enough_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Greed light", 5)

        expected_message = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(6, len(self.store))


    def test_receive_new_book_with_enough_capacity(self):
        result = self.store.receive_book("Green light", 3)
        expected_message = "3 copies of Green light are available in the bookstore."
        self.assertEqual(expected_message, result)
        self.assertEqual({"Warcraft": 3,
                          "Club five in the morning": 2,
                          "Sherlock Holmes": 1,
                          "Green light": 3}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_that_already_exist_in_the_store(self):
        result = self.store.receive_book("Warcraft", 2)
        expected_message = "5 copies of Warcraft are available in the bookstore."
        self.assertEqual(expected_message, result)
        self.assertEqual({"Warcraft": 5,
                          "Club five in the morning": 2,
                          "Sherlock Holmes": 1,
                          }, self.store.availability_in_store_by_book_titles)

    def test_selling_book_that_doesnt_exist_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Green light", 3)

        expected_message = "Book Green light doesn't exist!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_selling_book_with_not_enough_copies_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Warcraft", 5)
        expected_message = "Warcraft has not enough copies to sell. Left: 3"
        self.assertEqual(expected_message, str(ex.exception))

    def test_selling_existing_book_with_enough_copies_available(self):
        result = self.store.sell_book("Warcraft", 2)
        expected_message = "Sold 2 copies of Warcraft"
        self.assertEqual(expected_message, result)
        self.assertEqual({"Warcraft": 1,
                          "Club five in the morning": 2,
                          "Sherlock Holmes": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, self.store.total_sold_books)

    def test_selling_existing_book_with_exactly_enough_copies(self):
        result = self.store.sell_book("Warcraft", 3)
        expected_message = "Sold 3 copies of Warcraft"
        self.assertEqual(expected_message, result)
        self.assertEqual({"Warcraft": 0,
                          "Club five in the morning": 2,
                          "Sherlock Holmes": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, self.store.total_sold_books)

    def test_string_dunder_return_correct_message(self):
        result = str(self.store)
        expected = "Total sold books: 0\nCurrent availability: 6\n" \
                   " - Warcraft: 3 copies\n" \
                   " - Club five in the morning: 2 copies\n" \
                   " - Sherlock Holmes: 1 copies"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
