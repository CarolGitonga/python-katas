"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""
def descending_order(num):
    #convert the number to a string and split its numbers
    numbers = list(str(num))
    #join the sorted numbers 
    numbers.sort(reverse=True)
    #convert them back to an integer
    sorted_num = int(''.join(numbers))
    return sorted_num
print(descending_order (1234567890))
