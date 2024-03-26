from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Angel",
                             50_000,
                             100
                             )

    def test_correct_init(self):
        self.assertEqual("Angel", self.worker.name)
        self.assertEqual(50_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_enough_energy_expect_money_increase_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_error_not_enough_energy(self):
        self.worker.energy = 0  # Arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # Act

        self.assertEqual('Not enough energy.', str(ex.exception))  # Assert

    def test_worker_rest(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'Angel has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
