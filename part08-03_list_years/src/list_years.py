# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
    year_list=[]
    for date in dates:
        year_list.append(date.year)
    return sorted(year_list)
    

def main():
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
if __name__=="__main__":
    main()
