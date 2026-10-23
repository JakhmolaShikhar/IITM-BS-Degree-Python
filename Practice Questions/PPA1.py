''' Accept a positive integer 
n
n as input and print the first 
n
n positive integers, one number on each line.
'''

n = int(input())
i = 0
while i < n:
  i += 1
  print(i)
  
# another way

n = int(input())
i = 1
while i <= n:
  print(i)
  i += 1