import numpy as np

# Part 1
ins = np.loadtxt('Day1_input.txt')
print(sum((ins[1:]-ins[:-1])>0))
# Answer: 1696

# Part 2
slides = ins[:-2] + ins[1:-1] + ins[2:]
print(sum(slides[1:]-slides[:-1]>0))
# Answer: 1737

