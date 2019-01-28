from module import *

import random

size = 10

frequency = {}

while size != 1000:

	data = random.sample(range(1, size*2), size)

	codingProblem = codingProblem4(data)

	integer = codingProblem.firstMissingPositiveInteger()

	if integer in frequency:
		frequency[integer] = frequency[integer] + 1
	else:
		frequency[integer] = 1

	#Original list
	#print(data)

	#print(integer)

	size = size + 1

# The lowest missing positive integers frequencies in test cases 
print("-------------------------")
for key,value in frequency.items():
	print(str(key) + "=>" + str(value))

