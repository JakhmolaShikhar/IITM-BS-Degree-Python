#GrPA_4

number = input()
if number == "odd_num_check":
    number = int(input())
    if number % 2 != 0:
        print("yes")
    else:
        print("no")
elif number == "perfect_square_check":
    number = int(input())
    if (number ** 0.5).is_integer():
        print("yes")
    else:
        print("no")
elif number == "vowel_check":
    text = input()
    if any(vowel in text.lower() for vowel in "aeiou"):
        print("yes")
    else:
        print("no")

elif number == "divisibility_checK":
    number = int(input())
    if number % 2 == 0 and number % 3 == 0:
        print("divisible by 2 and 3")
    elif number % 2 == 0:
        print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif number == "palindrominator":
    text = input()
    print(text + text[::-1][1:])

elif number == "simple_interest":
    principal_amount = int(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = principal_amount * n_years * interest_rate
    print(round(simple_interest))

else:
    print("Invalid Operation")