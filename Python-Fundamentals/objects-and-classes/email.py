# Email

class Email:

    is_sent = False

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


command = input()
send_index = 0
information = []
while command != "Stop":
    information.append(command.split())
    command = input()

# print(information)

sent_emails = [int(x) for x in input().split(", ")]

for new_mail in range(len(information)):
    new_sender = information[new_mail][0]
    new_receiver = information[new_mail][1]
    new_content = information[new_mail][2]

    email = Email(new_sender, new_receiver, new_content)
    if new_mail in sent_emails:
        email.send()
    email.get_info()

