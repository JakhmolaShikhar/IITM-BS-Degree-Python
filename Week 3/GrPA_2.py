Write a multi functional program that takes input task from standard input and does the corresponding taks accordingly. Note that the usage of while loop is not allowed in this exercise.

Part 1 - while loop to for loop
factorial - print factorial of a given non-negative integer n (Type: Accumulation)
Input - n:int
even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
Input - n:int
power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in multiple lines, where n is taken from the input(Type: Mapping)
Input - n:int
Part 2 - for loop With range
sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
Input - n:int
from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
Input - n:int, k:int
part 3 - for loop with iterables.
string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
Input - s:str
list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
Input - l:list
if task == 'factorial':
    n = int(input())
    result = 1
    i = 1
    for i in range(1, n + 1):
        result*=i
        print(result)

              
elif task == 'even_numbers':
    n = int(input())
    for i in range(0, n+1, 2):
        print(i)

elif task == 'power_sequence':
    n = int(input())
    result = 1
    for _ in range(n):
        print(result)
        result*=2

elif task == 'sum_not_divisible':
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)


elif task == 'from_k':
    n = int(input())
    k = int(input())


elif task == 'string_iter':
    ...

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input

else:
    print("Invalid")