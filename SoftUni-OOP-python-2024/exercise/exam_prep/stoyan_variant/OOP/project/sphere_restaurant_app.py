from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_VALID_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENTS_VALID_TYPES = {"VIPClient": VIPClient, "RegularClient": RegularClient}

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worked):
        if waiter_type not in self.WAITER_VALID_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."

        try:
            next(filter(lambda a: a.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:
            new_waiter = self.WAITER_VALID_TYPES[waiter_type](waiter_name, hours_worked)
            self.waiters.append(new_waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type, client_name):
        if client_type not in self.CLIENTS_VALID_TYPES.keys():
            return f"{client_type} is not a recognized client type."

        try:
            next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:
            new_client = self.CLIENTS_VALID_TYPES[client_type](client_name)
            self.clients.append(new_client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name):
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name, order_amount):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name):
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            discount_and_remaining_points = client.apply_discount()
            return f"{client_name} received a {discount_and_remaining_points[0]}% discount. Remaining points {discount_and_remaining_points[1]}"
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        sorted_waiters_by_earning = sorted(self.waiters, key=lambda w: -w.earnings)
        total_earnings = sum(waiter.earnings for waiter in self.waiters)
        total_client_points = sum(client.apply_discount()[1] for client in self.clients if hasattr(client, 'points'))
        total_clients_count = len(self.clients)

        report = f"$$ Monthly Report $$\n"
        report += f"Total Earnings: ${total_earnings:.2f}\n"
        report += f"Total Clients Unused Points: {total_client_points}\n"
        report += f"Total Clients Count: {total_clients_count}\n"
        report += "** Waiter Details **\n"
        for waiter in sorted_waiters_by_earning:
            report += str(waiter) + "\n"

        return report
