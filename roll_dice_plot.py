'''
Author: Fanchen Bao
Date: 04/08/2018

Description:
A plot of the distribution of dice result for rolling user-input number of dices for user-input number of times.
This is a demonstration of using a simple plot() function from matplotlib.pyplot.
Note that since distribution is calculated during the dice roll and is itself the target of plot, there is no need to use hist() function.
'''

import matplotlib.pyplot as plt
from random import randint

n_dices = int(input("How many dices to roll: "))
n_rolls = int(input("How many times to roll the dice: "))

# record the number of occurrence for each result
distribution = [x * 0 for x in range(n_dices * 6)]
# all possible outcomes of the dice roll
outcomes = list(range(1, n_dices * 6 + 1))

# roll the dice
result = 0
for roll in range(n_rolls):
	for dice in range(n_dices):
		one_roll = randint(1, 6)
		# record the result by combining all dices 
		result += one_roll
	# increase the result's count in its distribution
	distribution[result - 1] += 100 / n_rolls
	result = 0



plt.plot(outcomes, distribution)
axis_range = [1, n_dices * 6, 0, 20]
plt.axis(axis_range)
plt.title("Rolling " + str(n_dices) + " Dices " + str(n_rolls) + " Times")
plt.xlabel("Outcomes of Each Roll")
plt.ylabel("Possibility %")
plt.show()
