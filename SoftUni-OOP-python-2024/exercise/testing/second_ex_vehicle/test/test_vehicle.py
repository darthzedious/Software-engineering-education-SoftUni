from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 233)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(233, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION,
                         self.vehicle.fuel_consumption)

    def test_drive_expect_exception_not_enough_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(500)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_expect_drive(self):
        self.vehicle.drive(2)
        self.assertEqual(97.5, self.vehicle.fuel)

    def test_refuel_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(500)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(5)

        self.assertEqual(55, self.vehicle.fuel)

    def test_string_methood(self):
        self.assertEqual(f"The vehicle has 233 "
               f"horse power with 100 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()