# http://adventofcode.com/2017/day/2
import sys

data = sys.stdin.readlines()

total = 0
for line in data:  
  items = line.strip().split() # split by space
  largest = float('-inf')
  smallest = float('inf') 
  # The problem asserts that only two items in each line divide evenly. 
  for i,x in enumerate(items):
    for j,y in enumerate(items):
      if i != j: # don't compare to yourself 
        if int(x) % int(y) == 0:    
          # print("Found %s %s" % (x, y))
          total += (int(x) / int(y)) 
    
print(total)




