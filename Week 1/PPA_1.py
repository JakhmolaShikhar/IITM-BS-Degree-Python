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
