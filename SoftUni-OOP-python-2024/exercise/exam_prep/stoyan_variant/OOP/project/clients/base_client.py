from abc import ABC, abstractmethod


class BaseClient(ABC):
    VALID_MEMBERSHIP_TYPES = ["Regular", "VIP"]

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.VALID_MEMBERSHIP_TYPES:
            raise ValueError(f"Invalid membership type. Allowed types: {', '.join(self.VALID_MEMBERSHIP_TYPES)}.") # can cause problem
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount):
        ...

    def apply_discount(self):
        if self.points >= 100:
            discount_percentage = 10
            remaining_points = self.points - 100
        elif 50 <= self.points < 100:
            discount_percentage = 5
            remaining_points = self.points - 50
        else:
            discount_percentage = 0
            remaining_points = self.points

        return (discount_percentage, remaining_points)
