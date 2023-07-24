from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Test name", 2.5)

    def test_correct_initialization(self):
        self.assertEqual("Test name", self.driver.name)
        self.assertEqual(2.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_with_valid_value(self):
        self.assertEqual(0, self.driver._TruckDriver__earned_money)

    def test_earned_money_setter_with_invalid_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        expected_message = "Test name went bankrupt."
        self.assertEqual(expected_message, str(ex.exception))

    def test_add_cargo_offer_twice_return_correct_message(self):
        result = self.driver.add_cargo_offer("Sofia", 100)
        expected = "Cargo for 100 to Sofia was added as an offer."
        self.assertEqual(expected, result)
        self.assertEqual({"Sofia": 100}, self.driver.available_cargos)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 100)

        expected_message = "Cargo offer is already added."
        self.assertEqual(expected_message, str(ex.exception))

    def test_driver_best_offer_with_no_offers_available(self):
        result = self.driver.drive_best_cargo_offer()
        expected_message = "There are no offers available."
        self.assertEqual(expected_message, result)

    def test_driver_best_offer(self):
        self.driver.add_cargo_offer("Sofia", 100)
        self.driver.add_cargo_offer("Varna", 10000)

        result = self.driver.drive_best_cargo_offer()
        expected_message = "Test name is driving 10000 to Varna."
        self.assertEqual(expected_message, result)
        self.assertEqual(10000, self.driver.miles)
        self.assertEqual(13250.0, self.driver.earned_money)



    def test_check_for_activities_for_eat(self):
        self.driver.earned_money += 300
        self.driver.eat(250)
        self.assertEqual(280, self.driver.earned_money)

    def test_check_for_activities_for_sleep(self):
        self.driver.earned_money += 300
        self.driver.sleep(1000)
        self.assertEqual(255, self.driver.earned_money)

    def test_check_for_activities_for_gas(self):
        self.driver.earned_money += 1000
        self.driver.pump_gas(1500)
        self.assertEqual(500, self.driver.earned_money)

    def test_check_for_activities_for_repair(self):
        self.driver.earned_money += 10000
        self.driver.repair_truck(10000)
        self.assertEqual(2500, self.driver.earned_money)

    def test_repr_method_return_correct_representation(self):
        result = str(self.driver)
        expected = "Test name has 0 miles behind his back."
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
