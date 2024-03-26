from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Stoyan")

    def test_init(self):
        self.assertEqual("Stoyan", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_if_fed_expect_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_cat_not_fed_expect_size_increase(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_sleep_if_not_fed_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep_if_fed_expect_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
