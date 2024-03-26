from unittest import TestCase, main
from expected_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(5.5, 2, 4, "abc")

    def test_integer(self):
        self.assertEqual([2, 4], self.integer_list.get_data())

    def test_add_invalid_elements_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(6.2)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_valid_element_to_the_list(self):
        expected_list = self.integer_list.get_data().copy()
        expected_list.append(4)

        self.integer_list.add(4)
        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_remove_invalid_index_element_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_index_element(self):
        self.integer_list.remove_index(0)

        self.assertEqual([4], self.integer_list.get_data())

    def test_get_invalid_index_result_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_valid_index_element(self):
        result = self.integer_list.get(0)

        self.assertEqual(2, result)

    def test_insert_invalid_index_element_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10, 10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_invalid_type_element_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_data(self):
        result = self.integer_list.insert(0, 5)

        self.assertEqual([5, 2, 4], self.integer_list.get_data())

    def test_get_biggest_number_in_the_list(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(4, result)

    def test_get_index(self):
        result = self.integer_list.get_index(4)

        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
