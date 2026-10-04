# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
students = 47
teachers = 3
bus_capacity = 20
ticket_price = 75
snack_price = 12.5
# <eoi>
# Use students and teachers to find total_people.
# Use bus_capacity with // to find completely filled buses.
# Use bus_capacity with % to find how many people are left.
# Use multiplication to find ticket and snack amounts.
# Use int() to convert the final amount to an integer.

total_people = students + teachers # int: add students and teachers
full_buses = total_people // bus_capacity # int: divide total_people by bus_capacity using //
people_left = total_people % bus_capacity # int: find the remainder after filling buses
ticket_amount = total_people * ticket_price # int: multiply total_people and ticket_price
snack_amount = total_people * snack_price # float: multiply total_people and snack_price
total_amount = ticket_amount + snack_amount # float: add ticket_amount and snack_amount
rounded_total = int(total_amount) # int: convert total_amount to an integer using int()

print(total_people, full_buses, people_left, ticket_amount, snack_amount, total_amount, rounded_total)

#PPA2

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
n = 24
# <eoi>
# Use comparison operators like >, >=, <=, and ==.
# Use % to check divisibility.
# Use and and not to combine or change boolean results.

is_positive = n > 0 # bool: check whether n is greater than 0
is_two_digit = 10 <= n <= 99 # bool: check whether n is from 10 to 99, including both 10 and 99
is_even = n % 2 == 0 # bool: check whether n gives remainder 0 when divided by 2
is_multiple_of_3 = n % 3 == 0 # bool: check whether n gives remainder 0 when divided by 3
is_good_number = is_positive and is_two_digit and n % 6 == 0 # bool: check whether n is positive, two-digit, and divisible by 6
is_not_small = n >= 10 # bool: check whether n is not less than 10

#PPA3

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
code = "BK24M157"
# <eoi>
# Use slicing to get more than one character.
# Use indexing to get one character.
# Use int() to convert the last 3 characters into a number.
# Use reverse slicing to reverse the code.

product_type = code[:2] # str: get the first 2 characters of code
year_text = code[2:4] # str: get the year part from code as text
batch = code[4] # str: get the batch character from code
product_number = int(code[-3:]) # int: get the last 3 characters and convert them to int
first_half = code[:4] # str: get the first 4 characters of code
last_half = code[-4:] # str: get the last 4 characters of code
reverse_code = code[::-1] # str: get code in reverse order