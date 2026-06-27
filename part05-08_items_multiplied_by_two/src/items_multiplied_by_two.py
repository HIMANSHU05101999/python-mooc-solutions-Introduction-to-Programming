# Write your solution here
def double_items(input: list):
    new_list=[]
    for item in input:
        item*=2
        new_list.append(item)
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)