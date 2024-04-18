from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):

    def __init__(self, name, hours_worked):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        earnings = self.hours_worked * 15.0
        return earnings

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
