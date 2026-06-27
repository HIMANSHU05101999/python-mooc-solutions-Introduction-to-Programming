# Write your solution here
pw=input("Password:")
while True:
    pwchk=input("Repeat password:")
    if pw==pwchk:
        break
    print("They do not match!")
print("User account created!")       