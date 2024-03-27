from unittest import TestCase, main
from project.mammal import Mammal

class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Stoyan", "Chovek", "maina")

    def test_init(self):
        self.assertEqual("Stoyan", self.mammal.name)
        self.assertEqual("Chovek", self.mammal.type)
        self.assertEqual("maina", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"Stoyan makes maina", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"Stoyan is of type Chovek", self.mammal.info())

if __name__ == "__main__":
    main()