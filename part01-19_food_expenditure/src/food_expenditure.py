# Write your solution here
times=int(input("How many times a week do you eat at the student cafeteria?"))
price=float(input("The price of a typical student lunch?"))
spend=float(input("How much money do you spend on groceries in a week?"))
weekly=times*price+spend
daily=weekly/7
print("")
print(f"Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros")