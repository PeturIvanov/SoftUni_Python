from car import Car
import unittest


class CarTests(unittest.TestCase):
    def test_init_is_initialized_correct(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual("a", car.make)
        self.assertEqual("a", car._Car__make)

        self.assertEqual("b", car.model)
        self.assertEqual("b", car._Car__model)

        self.assertEqual(1, car.fuel_consumption)
        self.assertEqual(1, car._Car__fuel_consumption)

        self.assertEqual(4, car.fuel_capacity)
        self.assertEqual(4, car._Car__fuel_capacity)

        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)



    def test_make_setter_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("", "b", 1, 4)

        expected_message  = "Make cannot be null or empty!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_model_setter_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "", 1, 4)

        expected_message  = "Model cannot be null or empty!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_fuel_consumption_setter_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 0, 4)

        expected_message  = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("a", "b", -1, 4)

        expected_message = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_fuel_capacity_setter_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("a", "b", 1, 0)

        expected_message  = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("a", "b", 1, -1)

        expected_message  = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_fuel_amount_setter_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 1, 4)
            car.fuel_amount = -1

        expected_message  = "Fuel amount cannot be negative!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_refuel_the_car_with_no_fuel_amount_raises(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        expected_message = "Fuel amount cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)

        expected_message = "Fuel amount cannot be zero or negative!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

    def test_refuel_car_with_valid_amount_of_fuel(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)
        self.assertEqual(4, car.fuel_capacity)
        self.assertEqual(4, car._Car__fuel_capacity)

        car.refuel(3)
        self.assertEqual(3, car.fuel_amount)
        self.assertEqual(3, car._Car__fuel_amount)
        self.assertEqual(4, car.fuel_capacity)
        self.assertEqual(4, car._Car__fuel_capacity)

        car.refuel(2)
        self.assertEqual(4, car.fuel_amount)
        self.assertEqual(4, car._Car__fuel_amount)
        self.assertEqual(4, car.fuel_capacity)
        self.assertEqual(4, car._Car__fuel_capacity)

    def test_drive_the_car_with_not_enough_fuel_raises(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.drive(100)

        expected_message = "You don't have enough fuel to drive!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

    def test_drive_the_car_with_enough_fuel(self):
        car = Car("a", "b", 1, 4)

        self.assertEqual(0, car.fuel_amount)
        self.assertEqual(0, car._Car__fuel_amount)

        car.refuel(3)
        self.assertEqual(3, car.fuel_amount)
        self.assertEqual(3, car._Car__fuel_amount)

        car.drive(200)

        self.assertEqual(1, car.fuel_amount)
        self.assertEqual(1, car._Car__fuel_amount)


if __name__ == "__main__":
    unittest.main()











