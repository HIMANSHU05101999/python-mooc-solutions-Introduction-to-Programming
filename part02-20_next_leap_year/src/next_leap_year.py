# Write your solution here

year=int(input("Year:"))
initialyear=year
while True:
    
    year+=1
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"The next leap year after {initialyear} is {year}")
        break
