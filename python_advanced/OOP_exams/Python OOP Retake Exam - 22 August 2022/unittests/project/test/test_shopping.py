from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Test", 50)
        self.cart.products = {"Lego": 30, "Puzzle": 10}
        self.other = ShoppingCart("Other", 100)
        self.other.products = {"Cup": 10, "Monopoly": 80}

    def test_correct_initialization(self):
        cart = ShoppingCart("Testcart", 50)
        self.assertEqual("Testcart", cart.shop_name)
        self.assertEqual(50, cart.budget)
        self.assertEqual({}, cart.products)

    def test_name_setter_with_only_lower_letters_raises(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("testname", 50)
        expected_message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_name_setter_with_digits_raises(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("Testcart2", 50)
        expected_message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_name_setter_with_white_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("Test name", 50)
        expected_message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_name_setter_with_symbols_raises(self):
        with self.assertRaises(ValueError) as ex:
            ShoppingCart("Test-name", 50)
        expected_message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_name_setter_with_valid_name(self):
        self.assertEqual("Test", self.cart._ShoppingCart__shop_name)

    def test_adding_to_cart_product_that_cost_equal_to_the_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("Laptop", 100)

        expected_message = "Product Laptop cost too much!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_product_to_the_cart_that_cost_over_the_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("Iphone", 150)
        expected_message = "Product Iphone cost too much!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_adding_to_cart_new_product(self):
        result = self.cart.add_to_cart("t-shirt", 25)
        self.assertEqual({"Lego": 30, "Puzzle": 10, "t-shirt": 25}, self.cart.products)
        expected_message = "t-shirt product was successfully added to the cart!"
        self.assertEqual(expected_message, result)

    def test_remove_non_existing_product_from_the_cart_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.remove_from_cart("Iphone")

        expected_message = "No product with name Iphone in the cart!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_remove_valid_product_from_the_cart(self):
        result = self.cart.remove_from_cart("Lego")
        self.assertEqual({"Puzzle": 10}, self.cart.products)
        self.assertEqual("Product Lego was successfully removed from the cart!", result)

    def test_add_dunder_method_creat_correct_instance(self):
        new_shopping_cart = self.cart + self.other
        self.assertIsInstance(new_shopping_cart, ShoppingCart)
        self.assertEqual("TestOther", new_shopping_cart.shop_name)
        self.assertEqual(150, new_shopping_cart.budget)
        self.assertEqual({"Lego": 30, "Puzzle": 10, "Cup": 10, "Monopoly": 80}, new_shopping_cart.products)

    def test_buy_products_with_not_enough_budget_raises(self):
        self.cart.products["Mouse"] = 40
        total_sum = sum(self.cart.products.values())
        self.assertEqual(80, total_sum)
        with self.assertRaises(ValueError) as ex:
            self.cart.buy_products()
        expected_message = "Not enough money to buy the products! Over budget with 30.00lv!"
        self.assertEqual(expected_message, str(ex.exception))


    def test_buy_products_with_enough_budget(self):
        total_sum = sum(self.cart.products.values())
        self.assertEqual(40, total_sum)
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 40.00lv.', result)

    def test_buy_products_with_equal_budget_and_cost(self):
        self.cart.products["Mouse"] = 10
        total_sum = sum(self.cart.products.values())
        self.assertEqual(50, total_sum)
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 50.00lv.', result)

if __name__ == "__main__":
    main()
