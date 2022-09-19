# Algoritimo Two Sum: O seu objetivo é retornar o índice dos dois números no array que, quando somados, possuem o valor igual ao número alvo.

import time
import matplotlib.pyplot as plt

def two_sum(nums, target, quantities):
	n = len(nums)
	start = time.time()
	for i in range(n):
		for j in range(i):
			if nums[i] + nums[j] == target:
				end = time.time()
				print("Registers: "+str(quantities)+" - time: " '%.2f' % (end-start))
				return ('%.2f' % (end-start))



numbers3000 = []
numbers6500 = []
numbers10300 = []
numbers1000 = []

with open("10382.txt") as file:
	    for line in file:
	        numbers10300.append(int(line))


with open("6500.txt") as file:
	    for line in file:
	        numbers6500.append(int(line))



with open("3k.txt") as file:
	    for line in file:
	        numbers3000.append(int(line))

with open("1Kints.txt") as file:
	    for line in file:
	        numbers1000.append(int(line))


quartaData = two_sum(numbers1000, 0, 1000)
terceiraData = two_sum(numbers3000, 0, 3000)
segundaData = two_sum(numbers6500, 0, 6500)
primeiraData = two_sum(numbers10300, 0, 10300)


# plt.plot(["1000 rows", "3000 rows", "6500 rows", "10300 rows"], [quartaData, terceiraData, segundaData, primeiraData],color ='orange', marker ='o', markersize = 12, )
# plt.ylabel('Time executing')
# plt.show()