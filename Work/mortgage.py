# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000.00
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
number_payments = 0

while principal > 0:
    number_payments += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment

    if extra_payment_start_month <= number_payments <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    print(f"{round(number_payments, 2)} {round(total_paid, 2)} {round(principal, 2)}")

    if principal < payment:
        number_payments += 1
        total_paid += principal
        principal -= principal
        print(f"{round(number_payments, 2)} {round(total_paid, 2)} {round(principal, 2)}")

print('Total paid', round(total_paid, 2))
print("Months", number_payments)
