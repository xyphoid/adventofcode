# http://adventofcode.com/2017/day/2
import sys

data = sys.stdin.readlines()

total = 0
for line in data:  
  items = line.strip().split() # split by space
  largest = float('-inf')
  smallest = float('inf') 
  for i in items:
    if int(i) < smallest:
      smallest = int(i)
    if int(i) > largest:
      largest = int(i)
  total += (largest - smallest) 
    
print(total)




