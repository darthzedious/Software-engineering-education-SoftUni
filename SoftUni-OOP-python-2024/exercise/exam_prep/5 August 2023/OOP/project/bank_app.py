from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        #client = [client for client in self.clients if client.client_id == client_id][0]
        #loan = [loan for loan in self.loans if loan.LOAN_TYPE == loan_type][0]
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.LOAN_TYPE == loan_type, self.loans))

        if not loan_type == client.POSSIBLE_LOAN_TYPE:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        filtered_loans = [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]
        [loan.increase_interest_rate() for loan in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        filtered_clients = [client for client in self.clients if client.interest < min_rate]
        [client.increase_clients_interest() for client in filtered_clients]
        return f"Number of clients affected: {len(filtered_clients)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        granted_sum = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        result = f"Active Clients: {total_clients_count}\n" \
                 f"Total Income: {total_clients_income:.2f}\n" \
                 f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
                 f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n" \
                 f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result
