from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTests(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Punto", "sedan", 250, 500)

    def test_constructor(self):
        self.assertEqual("Punto", self.car.model)
        self.assertEqual("sedan", self.car.car_type)
        self.assertEqual(250, self.car.mileage)
        self.assertEqual(500, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            SecondHandCar("Punto", "sedan", 500, 1)
        expected_message = 'Price should be greater than 1.0!'
        self.assertEqual(expected_message, str(ex.exception))

    def test_mileage_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            SecondHandCar("Punto", "sedan", 100, 500)
        expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_message, str(ex.exception))

    def test_set_new_promotional_price(self):
        self.assertEqual(500, self.car.price)
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(600)
        expected_message = 'You are supposed to decrease the price!'
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(500, self.car.price)

        result = self.car.set_promotional_price(400)
        expected_message = 'The promotional price has been successfully set.'
        self.assertEqual(400, self.car.price)
        self.assertEqual(expected_message, result)

    def test_repair(self):
        self.assertEqual([], self.car.repairs)
        self.assertEqual(500, self.car.price)

        result = self.car.need_repair(300, "new_suspension")
        expected_message = 'Repair is impossible!'
        self.assertEqual(expected_message, result)
        self.assertEqual([], self.car.repairs)
        self.assertEqual(500, self.car.price)

        result = self.car.need_repair(100, "new suspension")
        expected_message = 'Price has been increased due to repair charges.'
        self.assertEqual(expected_message, result)
        self.assertEqual(["new suspension"], self.car.repairs)
        self.assertEqual(600, self.car.price)

    def test_greater_then_dunder_method(self):
        other_car = SecondHandCar("BMW", "coupe", 200, 1000)
        result = self.car > other_car
        expected_message = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_message, result)

        same_car_type = SecondHandCar("BMW", "sedan", 300, 400)
        self.assertTrue(self.car > same_car_type)

        same_car_type.price = 600
        self.assertFalse(self.car > same_car_type)

    def test_str_dunder_method(self):
        expected = f"""Model Punto | Type sedan | Milage 250km\nCurrent price: 500.00 | Number of Repairs: 0"""
        self.assertEqual(expected, str(self.car))



if __name__ == "__main__":
    main()