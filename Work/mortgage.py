# mortgage.py
#
# Exercise 1.7
principal = 500000.0
monthly_pay= 2684.11
rate=0.05
total_paid=0.0
n=1

a=principal*(1+rate/12)/monthly_pay
print(a)

#while principal>0:
    #principal=principal*(1 +rate/12) - monthly_pay
    #total_paid= total_paid+monthly_pay
#print("Total money paid",total_paid)
    


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    if principal<0:
        total_paid=total_paid+principal
        principal=0
    print(total_paid,month,principal)
        
print("Total money paid",total_paid,"Total Months",month)
