#GrPA_1

with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]

if "for" in content:
    print("you should not use for loop or the for word in this exercise")

task = input()

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0: # the terminal condition
        total += n # add n to the total
        n = int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line == "END": # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += quantity * price  # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    while True:
        word = input()
        if word == "STOP":
            break
        if word.endswith("ed") or word.endswith("ing"):
            print(word)


elif task == "reverse_sum_palindrome":
    total = 0
    while True:
        n = int(input())
        if n == -1:
            break
        reverse_n = int(str(n)[::-1])
        if str(n + reverse_n) == str(n + reverse_n)[::-1]:
            print(n)


elif task == "double_string":
    while True:
        s = input()
        if s == "":
            break
        print(s * 2)


elif task == "odd_char":
    s = input()
    while s[-1] != ".":
        print(s[::2], end=" ")
        s = input()
    print(s[::2])
        

elif task == "only_even_squares":
    while True:
        n = int(input())
        if n == 0:
            break
        if n % 2 == 0:
            print(n * n)

elif task == "only_odd_lines":
    result = ""
    lineno = 1
    while True:
      line = input()
      if line == "END":
        break
      if lineno%2:
        result = line + "\n" + result
      lineno += 1
    print(result)


else:
    print("Invalid operation")
