from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("My Shop")

    def test_constrictor(self):
        self.assertEqual("My Shop", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_zero_quantity_food_raises(self):
        self.assertEqual({}, self.shop.food)
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("chicken", 0)
        expected_message = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({}, self.shop.food)

    def test_add_food(self):
        self.assertEqual({}, self.shop.food)

        result = self.shop.add_food("chicken", 10)
        expected_message = "Successfully added 10.00 grams of chicken."
        self.assertEqual(expected_message, result)
        self.assertEqual({"chicken": 10}, self.shop.food)

        result = self.shop.add_food("chicken", 5)
        expected_message = "Successfully added 5.00 grams of chicken."
        self.assertEqual(expected_message, result)
        self.assertEqual({"chicken": 15}, self.shop.food)

    def test_add_pet(self):
        self.assertEqual([], self.shop.pets)
        result = self.shop.add_pet("Aira")
        expected_message = "Successfully added Aira."
        self.assertEqual(expected_message, result)
        self.assertEqual(["Aira"], self.shop.pets)

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Aira")
        expected_message = "Cannot add a pet with the same name"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(["Aira"], self.shop.pets)

    def test_feed_pet_with_invalid_name_raises(self):
        self.assertEqual({}, self.shop.food)
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("chicken", "Aira")
        expected_message = "Please insert a valid pet name"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual({}, self.shop.food)

    def test_feed_pet(self):
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)
        self.shop.add_pet("Aira")
        self.assertEqual(["Aira"], self.shop.pets)

        result = self.shop.feed_pet("chicken", "Aira")
        expected_message = "You do not have chicken"
        self.assertEqual(expected_message, result)
        self.assertEqual(["Aira"], self.shop.pets)
        self.assertEqual({}, self.shop.food)

        self.shop.add_food("chicken", 50)
        self.assertEqual({"chicken": 50}, self.shop.food)
        result = self.shop.feed_pet("chicken", "Aira")
        expected_message = "Adding food..."
        self.assertEqual(expected_message, result)
        self.assertEqual({"chicken": 1050}, self.shop.food)
        self.assertEqual(["Aira"], self.shop.pets)


        result = self.shop.feed_pet("chicken", "Aira")
        expected_message = "Aira was successfully fed"
        self.assertEqual(expected_message, result)
        self.assertEqual({"chicken": 950}, self.shop.food)

    def test_repr_dunder_method(self):
        self.assertEqual([], self.shop.pets)
        self.shop.add_pet("Aira")
        self.shop.add_pet("Nala")
        self.shop.add_pet("Lilith")
        self.assertEqual(["Aira", "Nala", "Lilith"], self.shop.pets)

        result = repr(self.shop)
        expected = "Shop My Shop:\n" \
                   "Pets: Aira, Nala, Lilith"
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()