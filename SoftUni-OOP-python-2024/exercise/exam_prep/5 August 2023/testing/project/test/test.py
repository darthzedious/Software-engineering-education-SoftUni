from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Opel", "astra", 200_000, 12_500.0)

    def test_init(self):
        self.assertEqual("Opel", self.car.model)
        self.assertEqual("astra", self.car.car_type)
        self.assertEqual(200_000, self.car.mileage)
        self.assertEqual(12_500.0, self.car.price)

    def test_price_setter_if_price_lower_equal_to_one(self):

        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_if_mileage_less_equal_to_hundred(self):

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_if_new_price_higher_equal_to_car_price_expect_error(self):

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(50_000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_happy_case(self):

        output = 'The promotional price has been successfully set.'
        work = self.car.set_promotional_price(5_000)
        self.assertEqual(output, work)
        self.assertEqual(self.car.price, 5_000)

    def test_need_repair_repair_impossible(self):
        car = SecondHandCar("Opel", "astra", 200_000, 2_000.0)

        work = car.need_repair(1_001.0, "engine")
        output = 'Repair is impossible!'
        self.assertEqual(output, work)

    def test_need_repair_repair_possible(self):
        car = SecondHandCar("Opel", "astra", 200_000, 2_000)

        work = car.need_repair(200.0, "engine")
        output = f'Price has been increased due to repair charges.'

        self.assertEqual(output, work)
        self.assertEqual(car.price, 2_200.0)
        self.assertEqual(car.repairs[-1], "engine")

    def test_gt_method_mismatch_case(self):
        other_car = SecondHandCar("Opel", "zafira", 200_000, 12_500.0)

        compare = self.car.__gt__(other_car)
        output = 'Cars cannot be compared. Type mismatch!'

        self.assertEqual(output, compare)

    def test_get_method_happy_case(self):
        other_car = SecondHandCar("Opel", "astra", 200_000, 1_500.0)

        compare = self.car.__gt__(other_car)
        self.assertTrue(compare)

    def test_second_hand_car_string_mathood(self):
        compare = self.car.__str__()
        expected_output = f"""Model Opel | Type astra | Milage 200000km
Current price: 12500.00 | Number of Repairs: 0"""

        self.assertEqual(expected_output, compare)


if __name__ == "__main__":
    main()
