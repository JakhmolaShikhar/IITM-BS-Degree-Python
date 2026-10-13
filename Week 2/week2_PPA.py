#PPA_1

room_type = input()
is_weekend = input() == "True"
is_loyalty_member = input() == "True"
is_online_payment = input() == "True"

if room_type == "standard":
    cost = 2000
elif room_type == "deluxe":
    cost = 3500
elif room_type == "suite":
    cost = 5000
else:
   print("Invalid Room Type")
   exit()

if is_weekend:
    cost *= 1.2

if is_loyalty_member:
    cost *= 0.9

if is_online_payment:
    cost *= 1.03

print(f"{cost:.02f}")

#PPA_2


#PPA_3

age = int(input())
monthly_income = int(input())
credit_score = int(input())

if age < 21 or monthly_income < 25000:
    print("rejected")
else:
    if age >= 21 and monthly_income >= 25000 and credit_score >= 650:
        print("approved")
    else:
        print("conditionally approved")


#PPA_4

units = int(input())
has_solar = input() == "True"

if units <= 100:
    rate = 5
elif units <= 300:
  rate = 7
else:
    rate = 10

total = units * rate

if has_solar:
    total *= 0.8

print(f"{total:.02f}")


#PPA_5


number = input()

if number == "is_prime_check":
  if number < 2:
      print("no")
  else:
      for i in range(2, int(number ** 0.5) + 1):
          if number % i == 0:
              print("no")
              break
          else:
              print("yes")

elif number == "capitalize_check":
    text = input()
    if text[0].isupper():
        print("yes")
    else:
        print("no")

elif number == "bmi_category":
    weight_kg = float(input())
    height_m = float(input())
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        print("underweight")
    elif 18.5 <= bmi < 25:
        print("normal")
    elif 25 <= bmi < 30:
        print("overweight")
    else:
        print("obese")

elif number == "max_of_three":
    a = int(input())
    b = int(input())
    c = int(input())

    print(max(a, b, c))

elif number == "string_length_check":
    text = input()
    length = len(text)

    if length < 5:
        print('short')
    elif 5 <= length < 10:
        print("medium")
    else:
        print("long")

else:
    print("invalid operation")