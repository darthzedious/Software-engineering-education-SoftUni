from project.clients.base_client import BaseClient
from math import floor

class RegularClient(BaseClient):
    TYPE = "Regular"

    def __init__(self, name):
        super().__init__(name, membership_type=self.TYPE)

    def earning_points(self, order_amount):
        points_earned = order_amount // 10
        self.points += floor(points_earned)
        return floor(points_earned)
