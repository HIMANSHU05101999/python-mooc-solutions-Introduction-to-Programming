# Write your solution here
year=int(input("Please type in a year:"))
leapyear= False
if year % 100 ==0:
    if year%400==0:
        leapyear=True
elif year%4==0:
        leapyear=True
if leapyear:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")