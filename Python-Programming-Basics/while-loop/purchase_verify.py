# Verify Purchases

payments = []
transaction_data = {}

command = input("Enter transaction Number or Done to exit:")
while command != "Done":

    while True:
        try:
            transaction_number = int(command)
            break
        except ValueError:
            command = input("Enter a whole integer for transaction number:")

    transaction_data_names = ["amount", "date time", "number of products", "currency", "bank card"]
    for i in range(len(transaction_data_names)):
        while True:
            current_data = input(f"Enter {transaction_data_names[i]}:")
            if transaction_data_names[i] == "amount" or transaction_data_names[i] == "number of products":
                try:
                    current_data = int(current_data)
                    transaction_data[transaction_data_names[i]] = current_data
                    break
                except ValueError:
                    if transaction_data_names[i] == "amount":
                        print(f"You must enter a number for amount payable!")
                    elif transaction_data_names[i] == "number of products":
                        print(f"You must enter a number for number of products!")
            else:
                transaction_data[transaction_data_names[i]] = current_data
                break
    payments.append(transaction_data)
    command = input("Enter transaction Number or Done to exit:")

print(payments)
