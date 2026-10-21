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
      
elif task == "find_min":
  n = int(input())
  minimum = int(input())
  for i in range(n-1):
    current = int(input())
    if current < minimum:
      minimum = current
      
  print(minimum)
  
elif task == "prime_check":
  n = int(input())
  
  