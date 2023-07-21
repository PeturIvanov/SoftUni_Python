from list import IntegerList
import unittest

class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3)

    def test_get_data_return_correct_data(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_init_with_different_types_and_integers(self):
        my_list = IntegerList("a", 2.3, [], {}, 5, ())
        self.assertEqual([5], my_list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_add_method_adding_not_integer_type_raises(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        different_types = ["a", 2.4, [], {}, (), True]
        for el in different_types:
            with self.assertRaises(ValueError) as ex:
                self.list.add(el)

            expected_message = "Element is not Integer"
            self.assertEqual(expected_message, str(ex.exception))
            self.assertEqual([1, 2, 3], self.list.get_data())
            self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_add_method_with_integer(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        result = self.list.add(5)
        self.assertEqual([1, 2, 3, 5], result)

        self.assertEqual([1, 2, 3, 5], self.list.get_data())
        self.assertEqual([1, 2, 3, 5], self.list._IntegerList__data)

    def test_remove_index_method_with_invalid_index_raises(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(3)

        expected_message = "Index is out of range"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(5)

        expected_message = "Index is out of range"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_remove_index_method_with_valid_index(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        result = self.list.remove_index(0)
        self.assertEqual(1, result)
        self.assertEqual([2, 3], self.list.get_data())
        self.assertEqual([2, 3], self.list._IntegerList__data)

    def test_get_method_with_invalid_index(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.get(3)

        expected_message = "Index is out of range"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.get(4)

        expected_message = "Index is out of range"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_get_method_with_valid_index(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        result = self.list.get(0)
        self.assertEqual(1, result)
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_insert_method_with_invalid_index(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.insert(3, 4)

        expected_message = "Index is out of range"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_insert_method_with_invalid_type(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            self.list.insert(0, "a")

        expected_message = "Element is not Integer"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_insert_method_with_valid_index_and_valid_type(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        self.list.insert(0, 4)
        self.assertEqual([4, 1, 2, 3], self.list.get_data())
        self.assertEqual([4, 1, 2, 3], self.list._IntegerList__data)

    def test_get_biggest_element_in_list(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        result = self.list.get_biggest()
        self.assertEqual(3, result)

        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_get_index_method_with_valid_element(self):
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

        result = self.list.get_index(3)
        self.assertEqual(2, result)
        self.assertEqual([1, 2, 3], self.list.get_data())
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

if __name__ == "__main__":
    unittest.main()




























