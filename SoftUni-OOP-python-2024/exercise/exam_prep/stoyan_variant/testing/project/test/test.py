from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.restaurant = Restaurant("Bistro", 400)

    def test_correct_innit(self):
        self.assertEqual("Bistro", self.restaurant.name)
        self.assertEqual(400, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name_not_value(self):
        with self.assertRaises(ValueError):
            self.restaurant.name = ""

    def test_name_strip(self):
        with self.assertRaises(ValueError):
            self.restaurant.name = "  "

    def test_capacity(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.capacity = -2
        self.assertEqual("Invalid capacity!", str(ex.exception))

    # def test_get_waiters(self):
    #     expected = [{'name': 'Angel', 'total_earnings': 100},
    #                 {'name': 'Stoyan', 'total_earnings': 110}]
    #     result = self.restaurant.get_waiters(90, 150)
    #     self.assertEqual(result, expected)
    #
    # def test_get_waiters_equal(self):
    #     expected = [{'name': 'Angel', 'total_earnings': 100}]
    #     result = self.restaurant.get_waiters(100, 100)
    #     self.assertEqual(expected, result)

    def test_get_waiters_no_filter(self):
        filtered_waiters = self.restaurant.get_waiters()
        self.assertEqual(filtered_waiters, self.restaurant.waiters)

    def test_get_waiters_if_min_earning_is_not_none(self):
        expected = []
        result = self.restaurant.get_waiters(min_earnings=100)
        self.assertEqual(result, expected)

    def test_get_waiters_if_max_earning_is_not_none(self):
        expected = []
        result = self.restaurant.get_waiters(max_earnings=100)
        self.assertEqual(result, expected)

    def test_get_waiters_if_minand_max_earning_is_not_none(self):
        expected = []
        result = self.restaurant.get_waiters(min_earnings=100, max_earnings=100)
        self.assertEqual(result, expected)

    def test_get_waiter_working_case(self):
        expected = self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        result = self.restaurant.get_waiters(min_earnings=100, max_earnings=200)
        self.assertEqual(result, expected)

    def test_get_waiter_working_case_two(self):
        expected = self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        result = self.restaurant.get_waiters(min_earnings=300, max_earnings=200)
        self.assertEqual(result, expected)

    def test_add_waiter(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        self.restaurant.capacity = 1
        result = self.restaurant.add_waiter("Kristiyan")
        self.assertEqual(result, "No more places!")

    def test_add_waiter_existing_waiter(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        result = self.restaurant.add_waiter('Angel')
        self.assertEqual(result, f"The waiter Angel already exists!")

    def test_add_waiter_new_waiter(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        result = self.restaurant.add_waiter("Kristiyan")
        self.assertEqual(result, f"The waiter Kristiyan has been added.")

    def test_remove_waiter(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100},
                                   {'name': 'Stoyan', 'total_earnings': 110}]
        result = self.restaurant.remove_waiter("Stoyan")
        self.assertEqual(result, "The waiter Stoyan has been removed.")

    def test_remove_waiter_no_waiter_to_remove(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100}]
        result = self.restaurant.remove_waiter("Stoyan")
        self.assertEqual(result, "No waiter found with the name Stoyan.")

    def test_get_total_earnings(self):
        self.restaurant.waiters = [{'name': 'Angel', 'total_earnings': 100},
                                   {'name': 'Stoyan', 'total_earnings': 110}]
        result = self.restaurant.get_total_earnings()
        self.assertEqual(result, 210)


if __name__ == "_main_":
    main()
