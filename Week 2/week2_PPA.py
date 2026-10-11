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