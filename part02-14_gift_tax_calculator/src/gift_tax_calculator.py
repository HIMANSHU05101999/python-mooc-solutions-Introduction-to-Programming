# Write your solution here
value=int(input("Value of gift:"))

if 5000<=value<25000:
    lower_limit=5000
    lower_limit_tax=100
    tax_perc=0.08
    tax_amount = lower_limit_tax +(value-lower_limit)*tax_perc
    print("Amount of tax:",tax_amount)
elif 25000<=value<55000:
    lower_limit=25000
    lower_limit_tax=1700
    tax_perc=0.10
    tax_amount = lower_limit_tax +(value-lower_limit)*tax_perc
    print("Amount of tax:",tax_amount)
elif 55000<=value<200000:
    lower_limit=55000
    lower_limit_tax=4700
    tax_perc=0.12
    tax_amount = lower_limit_tax +(value-lower_limit)*tax_perc
    print("Amount of tax:",tax_amount)
elif 200000<=value<1000000:
    lower_limit=200000
    lower_limit_tax=22100
    tax_perc=0.15
    tax_amount = lower_limit_tax +(value-lower_limit)*tax_perc
    print("Amount of tax:",tax_amount)
elif 1000000<value:
    lower_limit=1000000
    lower_limit_tax=142100
    tax_perc=0.17
    tax_amount = lower_limit_tax +(value-lower_limit)*tax_perc
    print("Amount of tax:",tax_amount)
else:
    print("No tax!")