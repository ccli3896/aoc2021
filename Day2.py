import pandas as pd 

# PART 1
def direct(data, direction):
  return sum(data[1][data[0]==direction])

data = pd.read_csv('Day2_input.txt', sep=' ', header=None)
forward = direct('forward')
depth = direct('down') - direct('up')
print(forward*depth)
# ANSWER 1727835


