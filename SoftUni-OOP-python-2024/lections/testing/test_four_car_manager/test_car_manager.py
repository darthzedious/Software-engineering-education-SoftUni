from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Mercedes", "S class", 10, 100)

    def test_correct_init(self):
        self.assertEqual("Mercedes", self.car.make)
        self.assertEqual("S class",  self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_car_blank_value_return_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_car_blank_value_return_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_car_less_or_equal_to_zero_return_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_car_less_or_equal_to_zero_return_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_car_less_than_zero_return_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_fuel_less_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_to_max_capacity(self):
        self.car.fuel_capacity = 100
        self.car.refuel(110)

        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_car_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(110)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_fuel_decreases_fuel(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(99, self.car.fuel_amount)


if __name__ == "__main__":
    main()
