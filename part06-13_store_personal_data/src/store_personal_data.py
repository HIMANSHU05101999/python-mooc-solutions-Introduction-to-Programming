# Write your solution here
def store_personal_data(person: tuple):
    people=""
    with open("people.csv","a") as file:
        for i in range(len(person)):
            if i<len(person)-1:
                people+=(f"{person[i]};")
            else:
                people+=(f"{person[i]}\n")
        file.write(people)     



def main():
    store_personal_data(("DDD",27,178))
if __name__=="__main__":
    main()