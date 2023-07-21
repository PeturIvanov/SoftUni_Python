from cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def test_init_is_corrected_initialized(self):
        cat = Cat("Nala")
        self.assertEqual("Nala", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_eat_method_before_eat_and_after_eat(self):
        cat = Cat("Nala")
        self.assertEqual("Nala", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

        cat.eat()
        self.assertEqual("Nala", cat.name)
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(1, cat.size)

        with self.assertRaises(Exception) as ex:
            cat.eat()

        expected_message = 'Already fed.'
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual("Nala", cat.name)
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(1, cat.size)

    def test_sleep_method_when_cat_is_hungry_and_when_is_fed(self):
        cat = Cat("Nala")
        self.assertEqual("Nala", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        expected_message = 'Cannot sleep while hungry'
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual("Nala", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

        cat.eat()
        cat.sleep()
        self.assertEqual("Nala", cat.name)
        self.assertTrue(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(1, cat.size)


if __name__ == "__main__":
    unittest.main()




