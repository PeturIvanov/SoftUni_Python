from worker import Worker
import unittest

class WorkerTests(unittest.TestCase):
    def test_init_is_correct(self):
        worker = Worker("Test", 100, 50)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_work_with_no_energy_raises(self):
        worker = Worker("Test", 100, 0)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works_and_increase_money_and_decrease_energy(self):
        worker = Worker("Test", 100, 50)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

        worker.work()
        self.assertEqual(100, worker.salary)
        self.assertEqual(49, worker.energy)
        self.assertEqual(100, worker.money)

        worker.work()
        self.assertEqual(100, worker.salary)
        self.assertEqual(48, worker.energy)
        self.assertEqual(200, worker.money)

    def test_worker_rest_and_gain_energy(self):
        worker = Worker("Test", 100, 50)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

        worker.rest()
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(51, worker.energy)
        self.assertEqual(0, worker.money)

    def test_get_info_return_correct_str(self):
        worker = Worker("Test", 100, 50)
        expect = "Test has saved 0 money."
        self.assertEqual(expect, worker.get_info())

if __name__ == "__main__":
    unittest.main()
