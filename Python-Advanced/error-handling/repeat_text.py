# Repeat text

# try:
#     text = input()
#     times = int(input())
# except ValueError:
#     print("Variable times must be an integer")
# else:
#     print(text * times)

# -- Inheritance

class PaymentError(Exception):
    pass


raise PaymentError("Payment Cannot be processed at the moment."
                   " Please try again later.")
