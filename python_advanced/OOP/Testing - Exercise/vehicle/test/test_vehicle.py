from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(5.5, 100.5)

    def test_correct_initializing(self):
        self.assertEqual(5.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_the_vehicle_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(20)

        expected_message = "Not enough fuel"
        self.assertEqual(expected_message, str(ex.exception))

    def test_drive_the_vehicle_with_enough_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(3, self.vehicle.fuel)

    def test_overflow_the_vehicle_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        expected_message = "Too much fuel"
        self.assertEqual(expected_message, str(ex.exception))

    def test_refuel_the_vehicle(self):
        self.vehicle.drive(2)
        self.vehicle.refuel(2)
        self.assertEqual(5, self.vehicle.fuel)

    def test_string_method_return_correct_message(self):
        expected = f"The vehicle has 100.5 " \
               f"horse power with 5.5 fuel left and " \
                   f"1.25 fuel consumption"

        result = str(self.vehicle)
        self.assertEqual(expected, result)



if __name__ == "__main__":
    main()