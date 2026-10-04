#GrPA_2
a = 5
price1, discount1 = 50, 4
price2, discount2 = 60, 8

output1 = a >= 5 # bool: True if a greater than or equal to 5

output2 = a % 5 == 0 # bool: True if a is divisible by 5

output3 = a % 2 == 1 and a < 10 # bool: True if a is odd number less than 10

output4 = a % 2 == 1 and -10 < a < 10 # bool: True if a is an odd number within the range -10 and 10

output5 = len(str(a)) % 2 == 0 and 1 <= len(str(a)) <= 10 # bool: True if a has even number of digits but not more than 10 digits

discounted_price1 = price1 * (1 - (discount1 / 100))
discounted_price2 = price2 * (1 - (discount2 / 100))

is_offer1_cheaper = discounted_price1 < discounted_price2 # bool: True if the offer1 is strictly cheaper