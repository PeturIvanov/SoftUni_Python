from project.robot import Robot
from unittest import main, TestCase


class RobotTests(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1111", "Military", 50, 30)

    def test_correct_initialization_with_valid_parameters(self):
        self.assertEqual("1111", self.robot.robot_id)
        self.assertEqual("Military", self.robot._Robot__category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(30, self.robot._Robot__price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_with_invalid_category_raises(self):
        with self.assertRaises(ValueError) as ex:
            Robot("1111", "Cleaner", 50, 30)

        expected_message = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected_message, str(ex.exception))

    def test_price_setter_with_negative_price_raises(self):
        with self.assertRaises(ValueError) as ex:
            Robot("1111", "Military", 50, -1)

        expected_message = "Price cannot be negative!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_category_getter_return_correct_data(self):
        result = self.robot.category
        self.assertEqual("Military", result)

    def test_price_getter_return_correct_data(self):
        result = self.robot.price
        self.assertEqual(30, result)

    def test_upgrade_with_new_hardware_components(self):
        result = self.robot.upgrade("SSD", 100)
        expected = 'Robot 1111 was upgraded with SSD.'
        self.assertEqual(["SSD"], self.robot.hardware_upgrades)
        self.assertEqual(180, self.robot.price)
        self.assertEqual(expected, result)

    def test_upgrade_with_existing_hardware_component(self):
        self.robot.hardware_upgrades.append("SSD")
        result = self.robot.upgrade("SSD", 100)
        expected = "Robot 1111 was not upgraded."
        self.assertEqual(expected, result)

    def test_update_with_new_software_and_enough_capacity(self):
        result = self.robot.update(1.1, 25)
        expected_message = 'Robot 1111 was updated to version 1.1.'
        self.assertEqual([1.1], self.robot.software_updates)
        self.assertEqual(25, self.robot.available_capacity)
        self.assertEqual(expected_message, result)

    def test_update_with_new_software_but_not_enough_capacity(self):
        result = self.robot.update(1.1, 60)
        expected_message = "Robot 1111 was not updated."
        self.assertEqual(expected_message, result)

    def test_update_with_old_software_and_enough_capacity(self):
        self.robot.software_updates.append(1.5)
        result = self.robot.update(1.2, 25)
        expected = "Robot 1111 was not updated."
        self.assertEqual(expected, result)

    def test_greater_then_method_return_correct_message_with_first_robot_cost_more(self):
        other_robot = Robot("2222", "Education", 40, 20)
        result = self.robot > other_robot
        expected_message = 'Robot with ID 1111 is more expensive than Robot with ID 2222.'
        self.assertEqual(expected_message, result)

    def test_equal_method_return_correct_message_with_equal_cost(self):
        other_robot = Robot("2222", "Education", 40, 30)
        result = other_robot > self.robot
        expected_message = 'Robot with ID 2222 costs equal to Robot with ID 1111.'
        self.assertEqual(expected_message, result)

    def test_greater_then_method_return_correct_message_with_second_robot_cost_more(self):
        other_robot = Robot("2222", "Education", 40, 100)
        result = other_robot < self.robot
        expected_message = 'Robot with ID 1111 is cheaper than Robot with ID 2222.'
        self.assertEqual(expected_message, result)


if __name__ == "__main__":
    main()