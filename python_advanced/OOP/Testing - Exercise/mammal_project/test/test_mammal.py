from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Test", "Test type", "Test sound")

    def test_init_is_correct(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("Test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_return_correct_data(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes Test sound", result)

    def test_get_kingdom_getter(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_return_correct_data(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type Test type", result)


if __name__ == "__main__":
    unittest.main()

