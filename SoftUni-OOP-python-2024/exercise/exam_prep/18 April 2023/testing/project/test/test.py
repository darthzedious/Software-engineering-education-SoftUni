from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot_one = Robot("2", "Military", 10, 200)
        self.robot_two = Robot("3", "Military", 10, 100)

    def test_init(self):
        self.assertEqual("2", self.robot_one.robot_id)
        self.assertEqual("Military", self.robot_one.category)
        self.assertEqual(10, self.robot_one.available_capacity)
        self.assertEqual(200, self.robot_one.price)
        self.assertEqual(1.5, self.robot_one.PRICE_INCREMENT)

    def test_category_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot_one.category = "Mango"

        expected_result = f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected_result, str(ve.exception))

    # def test_category_setter_happy_case(self):
    #     self.robot.category = "Military"
    #     self.assertEqual("Military", self.robot.category)

    def test_price_setter_expect_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot_one.price = -1
        result = "Price cannot be negative!"
        self.assertEqual(result, str(ve.exception))

    def test_upgrade_part_already_upgraded_expect_fail(self):
        self.robot_one.upgrade("1234", 100)
        self.assertEqual(["1234"], self.robot_one.hardware_upgrades)
        self.assertEqual(350, self.robot_one.price)

        result_message = f"Robot 2 was not upgraded."
        result_action = self.robot_one.upgrade("1234", 100)
        self.assertEqual(result_message, result_action)
        self.assertEqual(["1234"], self.robot_one.hardware_upgrades)
        self.assertEqual(350, self.robot_one.price)

    def test_upgrade_happy_case_expect_success(self):
        result_action = self.robot_one.upgrade("1234", 100)
        self.assertEqual(["1234"], self.robot_one.hardware_upgrades)
        self.assertEqual(350, self.robot_one.price)

        result_message = f'Robot 2 was upgraded with 1234.'

        self.assertEqual(result_message, result_action)

    def test_update_not_enough_capacity_expect_fail(self):
        result_message = f"Robot 2 was not updated."
        self.robot_one.available_capacity = 2
        result_first_try = self.robot_one.update(2, 5)
        self.assertEqual(result_message, result_first_try)

    def test_update_expect_lower_version_expect_fail(self):
        result_message = f"Robot 2 was not updated."

        self.robot_one.update(2, 5)
        self.assertEqual([2], self.robot_one.software_updates)
        self.assertEqual(5, self.robot_one.available_capacity)

        result_action = self.robot_one.update(1, 5)
        self.assertEqual(result_message, result_action)
        self.assertEqual([2], self.robot_one.software_updates)
        self.assertEqual(5, self.robot_one.available_capacity)

    def test_update_happy_case(self):
        result_message = f'Robot 2 was updated to version 2.'
        result_action = self.robot_one.update(2, 5)

        self.assertEqual(result_message, result_action)
        self.assertEqual([2], self.robot_one.software_updates)
        self.assertEqual(5, self.robot_one.available_capacity)

    def test_gt_method_robot_one_has_greater_price(self):
        result_message = f'Robot with ID 2 is more expensive than Robot with ID 3.'
        result_action = self.robot_one.__gt__(self.robot_two)

        self.assertEqual(result_message, result_action)

    def test_gt_method_robot_two_has_greater_price(self):
        self.robot_one.price = 1
        result_message = f'Robot with ID 2 is cheaper than Robot with ID 3.'
        result_action = self.robot_one.__gt__(self.robot_two)

        self.assertEqual(result_message, result_action)

    def test_gt_method_both_robots_have_equal_price(self):
        self.robot_one.price = self.robot_two.price
        result_message = 'Robot with ID 2 costs equal to Robot with ID 3.'
        result_action = self.robot_one.__gt__(self.robot_two)

        self.assertEqual(result_message, result_action)


if __name__ == "__main__":
    main()