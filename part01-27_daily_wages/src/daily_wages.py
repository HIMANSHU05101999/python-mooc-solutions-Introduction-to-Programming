# Write your solution here
wage=float(input("Hourly wage: "))
hours=int(input("Hours worked: "))
day=input("Day of the week: ")
if day == "Sunday":
    print(f"Daily wages: {2*wage*hours} euros")
else:
    print(f"Daily wages: {wage*hours} euros")  