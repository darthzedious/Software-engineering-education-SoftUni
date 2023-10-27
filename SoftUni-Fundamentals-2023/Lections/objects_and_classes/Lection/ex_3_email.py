class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_letters = []
command = input()
while command != "Stop":
    sender, receiver, content = command.split()
    email_info = Email(sender, receiver, content)
    list_of_letters.append(email_info)
    command = input()
idx = [int(i) for i in input().split(", ")]
for i in idx:
    list_of_letters[i].send()
for current_email in list_of_letters:
    print(current_email.get_info())
