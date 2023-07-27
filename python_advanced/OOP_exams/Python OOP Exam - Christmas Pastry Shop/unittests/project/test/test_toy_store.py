from unittest import main, TestCase
from project.toy_store import ToyStore


class ToyStoreTests(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()
        self.store.toy_shelf["A"] = "some toy"

    def test_correct_initialization(self):
        test_store = ToyStore()
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, test_store.toy_shelf)

    def test_adding_toy_to_invalid_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("W", "iron man")
        expected_message = "Shelf doesn't exist!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_toy_that_is_already_in_the_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "some toy")

        expected_message = "Toy is already in shelf!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_toy_to_filled_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Thrall")
        expected_message = "Shelf is already taken!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_new_toy_to_existing_empty_shelf_return_correct_message_and_modify_the_shelf(self):
        result = self.store.add_toy("B", "Thrall")
        expected_shelf = {
            "A": "some toy",
            "B": "Thrall",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_shelf, self.store.toy_shelf)
        self.assertEqual("Toy:Thrall placed successfully!", result)

    def test_remove_toy_from_not_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("W", "some toy")
        expected_message = "Shelf doesn't exist!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_remove_not_existing_toy_from_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Thrall")
        expected_message = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_remove_toy_work_correctly_with_valid_parameters(self):
        result = self.store.remove_toy("A", "some toy")
        expected_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_shelf, self.store.toy_shelf)
        self.assertEqual("Remove toy:some toy successfully!", result)


if __name__ == "__main__":
    main()