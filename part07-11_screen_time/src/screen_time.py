# Write your solution here
from datetime import datetime,timedelta

if False:
        file_name="abc.txt"
        start_date="1.1.2021"
        start_date=datetime.strptime(start_date,"%d.%m.%Y")
        initial_date=start_date
        num_of_days=3
else:
        file_name=input("Filename:")
        start_date=input("Starting date:")
        start_date=datetime.strptime(start_date,"%d.%m.%Y")
        initial_date=start_date
        num_of_days=int(input("How many days:"))

print("Please type in screen time in minutes on each day (TV computer mobile):")
    
total_time=0
empty_list=[]
data_list=[]
    

for i in range(num_of_days):
            screen_time=input(f"Screen time {start_date.strftime('%d.%m.%Y')}: ")
            data_list.append(f"{start_date.strftime('%d.%m.%Y')}: {screen_time.replace(' ','/')}")
            empty_list=screen_time.split()
            #print(empty_list)
            for item in empty_list:
                total_time+=int(item)
            #print(total_time)
            start_date=start_date + timedelta(days=1)
            #print(data_list)
with open(file_name,"w") as file:
        file.write(f"Time period: {initial_date.strftime('%d.%m.%Y')}-{(initial_date+timedelta(days=num_of_days-1)).strftime('%d.%m.%Y')}\nTotal minutes: {total_time}\nAverage minutes: {total_time/num_of_days}")
        for item in data_list:
            file.write("\n"+item)   
print(f"Data stored in file {file_name}")  


