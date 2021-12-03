import numpy as np 
import pandas as pd 

data = pd.read_csv('Day2_input.txt', sep=' ', header=None)
directs = list(data[0])
nums = list(data[1])

aim = 0
depth = 0
for i in range(len(directs)):
  if directs[i]=='down':
    aim += nums[i]
  elif directs[i]=='up':
    aim -= nums[i]
  elif directs[i]=='forward':
    depth += aim*nums[i]
# Forward was 1905
print(depth)
print(depth*1905
# 810499
# 1544000595