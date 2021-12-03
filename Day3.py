import numpy as np 
from scipy import stats

def eliminate(gas, bins):
  # 'o' or 'c'
  nums,digs = bins.shape
  lefts = np.arange(nums)

  for d in range(digs):
    remaining = bins[lefts,d]

    modes = stats.mode(remaining)

    if modes[1][0]==len(remaining)/2:
      if gas=='o':
        most = 1
      else:
        most = 0
    else:
      most = modes[0].flatten()
      if gas=='c':
        most = 1 if most==0 else 0

    lefts = lefts[remaining==most]

    if len(lefts)==1:
      gas = np.sum(bins[lefts]*twos)
      return gas


# Load data and put it in a nice array
data = np.loadtxt('Day3_input.txt',dtype=str)
bins = []
for d in data:
  bins.append([x for x in d])
bins = np.array(bins).astype(int)


gamma = stats.mode(bins,axis=0)[0].flatten()
eps = [1 if g==0 else 0 for g in gamma]
twos = np.flip(np.power(np.ones(len(eps))*2, range(len(eps)))).astype(int)

print(sum(gamma*twos)*sum(eps*twos))
# Answer 3901196

# Part 2
oxygen = eliminate('o', bins)
co2 = eliminate('c', bins)
print('O2',oxygen,'CO2',co2)
print('GASEOUS PRODUCT', oxygen*co2)

# OXYGEN 1639
# CO2 2692
# Answer 4412188
