# Write your solution here
from datetime import datetime
def how_old():
    day=int(input("Day: "))
    month=int(input("Month:"))
    year=int(input("Year:"))
    dob=datetime(year,month,day)
    diff=datetime(1999,12,31)-dob
    if (diff)>(datetime(1999,12,31)-datetime(1999,12,31)):
        return(f"You were {diff.days} days old on the eve of the new millennium.")
    else:
        return("You weren't born yet on the eve of the new millennium.")
def main():
    print(how_old())
main()