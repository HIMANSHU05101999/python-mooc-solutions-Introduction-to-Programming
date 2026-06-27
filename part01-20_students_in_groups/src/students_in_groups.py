# Write your solution here
total=int(input("How many students on the course?"))
group=int(input("Desired group size?"))

if (total%group)>0:
    print(f"Number of groups formed: {total//group + 1}")

if (total%group)==0:
    print(f"Number of groups formed: {total//group}")

