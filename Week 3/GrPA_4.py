#GrPA_4

any = None
all = None
min = None

task = input()


if task == "factors":
  n = int(input())
  for i in range(1, n + 1):
    if n % i == 0:
      print(i)