# Write your solution here
def remove_smallest(input_list):
    smallest=input_list[0]
    for item in input_list:
        if item<smallest:
            smallest=item
    input_list.remove(smallest)
    #return input_list


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)