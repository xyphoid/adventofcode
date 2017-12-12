# http://adventofcode.com/2017/day/1
# read in stdin
# build total
# iterate through all characters
# if character = character+1 then add character to sum
# output total

import sys

# fetch input and trim newline etc
data = sys.stdin.read().strip()
print("Found %i chars." % len(data))

total = 0
length = len(data)
for i,c in enumerate(data):
  j = (i+length/2) % length # calculate the next index in the string 
  if c == data[j]: # if the next index has the same value as this one
    total += int(c)
 
print(total)




