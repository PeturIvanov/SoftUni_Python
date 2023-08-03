from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("My Library")

    def test_constructor(self):
        self.assertEqual("My Library", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_with_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            Library("")
        expected_message = "Name cannot be empty string!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_add_book(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Me", "Tests")
        self.assertEqual({"Me": ["Tests"]}, self.library.books_by_authors)

        self.library.add_book("Me", "Tests")
        self.assertEqual({"Me": ["Tests"]}, self.library.books_by_authors)

        self.library.add_book("Me", "Project")
        self.assertEqual({"Me": ["Tests", "Project"]}, self.library.books_by_authors)

        self.library.add_book("Raq", "Good mother")
        self.assertEqual({"Me": ["Tests", "Project"], "Raq": ["Good mother"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.assertEqual({}, self.library.readers)
        result = self.library.add_reader("Sofiya")
        self.assertEqual({"Sofiya": []}, self.library.readers)
        self.assertEqual(None, result)

        result = self.library.add_reader("Sofiya")
        expected_message = "Sofiya is already registered in the My Library library."
        self.assertEqual({"Sofiya": []}, self.library.readers)
        self.assertEqual(expected_message, result)

    def test_rent_book(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book("Me", "Project")
        self.library.add_book("Raq", "Good mother")
        self.assertEqual({"Me": ["Project"], "Raq": ["Good mother"]}, self.library.books_by_authors)

        self.assertEqual({}, self.library.readers)
        self.library.add_reader("Sofiya")
        self.assertEqual({"Sofiya": []}, self.library.readers)

        result = self.library.rent_book("Vasko", "Me", "Project")
        expected_message = "Vasko is not registered in the My Library Library."
        self.assertEqual(expected_message, result)
        self.assertEqual({"Me": ["Project"], "Raq": ["Good mother"]}, self.library.books_by_authors)
        self.assertEqual({"Sofiya": []}, self.library.readers)

        result = self.library.rent_book("Sofiya", "Ivan Vazov", "New Earth")
        expected_message = "My Library Library does not have any Ivan Vazov's books."
        self.assertEqual(expected_message, result)
        self.assertEqual({"Me": ["Project"], "Raq": ["Good mother"]}, self.library.books_by_authors)
        self.assertEqual({"Sofiya": []}, self.library.readers)

        result = self.library.rent_book("Sofiya", "Me", "Tests")
        expected_message = """My Library Library does not have Me's "Tests"."""
        self.assertEqual(expected_message, result)
        self.assertEqual({"Me": ["Project"], "Raq": ["Good mother"]}, self.library.books_by_authors)
        self.assertEqual({"Sofiya": []}, self.library.readers)

        result = self.library.rent_book("Sofiya", "Me", "Project")
        expected = None
        self.assertEqual(expected, result)
        self.assertEqual({"Me": [], "Raq": ["Good mother"]}, self.library.books_by_authors)
        self.assertEqual({"Sofiya": [{"Me": "Project"}]}, self.library.readers)

if __name__ == "__main__":
    main()