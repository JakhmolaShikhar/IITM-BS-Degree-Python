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