from unittest import TestCase, main
from project.plantation import Plantation


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_correct_initialization(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)


    def test_size_setter_with_negative_number_raises(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-10)

        expected_message = "Size must be positive number!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_hire_new_worker(self):
        self.assertEqual([], self.plantation.workers)
        self.assertEqual(0, len(self.plantation.workers))

        result = self.plantation.hire_worker("worker two")
        expected = "worker two successfully hired."
        self.assertEqual(["worker two"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        self.assertEqual(expected, result)


    def test_hire_worker_that_is_already_hired_raises(self):
        self.plantation.hire_worker("Test worker")
        self.assertEqual(["Test worker"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Test worker")

        expected_message = "Worker already hired!"
        self.assertEqual(expected_message, str(ex.exception))
        self.assertEqual(["Test worker"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))



    def test_len_dunder_method_with_plants_planted(self):
        self.plantation.plants = {"worker two": ["plant1"], "worker one": ["plant2"]}
        result = len(self.plantation)
        self.assertEqual(2, result)


    def test_len_dunder_method_with_not_plants_planted(self):
        result = len(self.plantation)
        self.assertEqual(0, result)

    def test_planting_with_invalid_worker_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test worker", "plant1")

        expected_message = "Worker with name Test worker is not hired!"
        self.assertEqual(expected_message, str(ex.exception))

    def test_start_planting_with_no_size_left_raises(self):
        self.plantation.workers = ["Test worker"]
        self.plantation.plants = {"Test worker": ["plant1", "plant2"]}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test worker", "plant3")
        expected_message = "The plantation is full!"
        self.assertEqual(expected_message, str(ex.exception))



    def test_planting_with_worker_who_has_planted_plants_already(self):
        self.plantation.workers = ["Test worker"]
        self.plantation.plants = {"Test worker": ["plant1"]}
        result = self.plantation.planting("Test worker", "plant2")
        expected_message = "Test worker planted plant2."
        self.assertEqual(expected_message, result)
        self.assertEqual({"Test worker": ["plant1", "plant2"]}, self.plantation.plants)

    def test_worker_plant_his_first_plant(self):
        self.plantation.workers = "New worker"
        result = self.plantation.planting("New worker", "plant1")
        expected_message = "New worker planted it's first plant1."
        self.assertEqual(expected_message, result)
        self.assertEqual({"New worker": ["plant1"]}, self.plantation.plants)

    def test_str_method_return_correct_data(self):
        self.plantation.workers = ["Test worker", "New worker"]
        self.plantation.plants = {"Test worker": ["plant1"], "New worker": ["plant1"]}
        expected = "Plantation size: 2\n" \
                   "Test worker, New worker\n" \
                   "Test worker planted: plant1\n" \
                   "New worker planted: plant1"
        self.assertEqual(expected, str(self.plantation))

    def test_repr_method_represent_instances_correct(self):
        self.plantation.workers = ["Test worker", "New worker"]
        expected = "Size: 2\n" \
                   "Workers: Test worker, New worker"
        self.assertEqual(expected, repr(self.plantation))


if __name__ == "__main__":
    main()