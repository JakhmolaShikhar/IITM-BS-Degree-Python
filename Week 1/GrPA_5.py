#GrPA 5

age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob.split('/')[0]), int(dob.split('/')[1]), int(dob.split('/')[2]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = f"{day}/{month}/{year+5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year + age}" # str: last birthday formatted as day/month/year

tenth_month = f"{day}/{((month - 1) + 10) % 12 + 1}/{year + ((month - 1) + 10) // 12}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(f"{tenth_month}, {fifth_birthday}, {last_birthday}")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = f"{int(weight)} kg {int((weight - int(weight)) * 1000)} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)