'''
Author: Fanchen Bao
Date: 04/08/2018

Description:
Histogram plot of the distribution of dice result for rolling user-input number of dices for user-input number of times.
This is a demonstration of using hist() function from matplotlib.pyplot
'''

import matplotlib.pyplot as plt
from random import randint
import numpy as np

n_dices = int(input("How many dices to roll: "))
n_rolls = int(input("How many times to roll the dice: "))

# record all the results
results = []
# record the number of occurrence for each result
# actually distribution is not useful in this case, because histogram does the distribution already
distribution = [x * 0 for x in range(n_dices * 6)]

# roll the dice
result = 0
for roll in range(n_rolls):
	for dice in range(n_dices):
		one_roll = randint(1, 6)
		# record the result by combining all dices 
		result += one_roll
	# increase the result's count in its distribution
	distribution[result - 1] += 1
	# record result
	results.append(result)
	result = 0

# a list of values from the min to the max + 1 of all possible dice-rolling outcomes
# need to be max + 1 because it is the right edge of the bin
# argument here is max + 2 due to the range is not inclusive
bins_value = list(range(min(results), (max(results) + 2)))

# determines how much weight each count is. To get probability, the weight of each roll is 1 / n_roll
weights = [1 / n_rolls for i in range(n_rolls)]

fig, (ax1 , ax2) = plt.subplots(2, 1, sharey = True, sharex = True)

# this is to show that when the bin width is 1, using weights is the same as setting density to true.
ax1.hist(results, bins = bins_value, weights = weights, align = 'left', edgecolor = 'black', linewidth = 1)
ax2.hist(results, bins = bins_value, density = True, align = 'left', edgecolor = 'black', linewidth = 1)

ax1.set_title('Use weights', fontsize = 10, y = 0.98)
ax2.set_title('Use density', fontsize = 10, y = 0.98)

# let all bins value show, but don't show the last one, as it is just the right edge
plt.xticks(bins_value[: -1], bins_value[: -1])

# add an overall big plot but hide its frame
fig.add_subplot(111, frameon = False)
# main plot title, the y argument moves the title up
plt.title("Rolling " + str(n_dices) + " Dices " + str(n_rolls) + " Times", y = 1.08)
# hide overall plot's ticks
plt.tick_params(labelcolor = 'none', top = 'off', bottom = 'off', left = 'off', right = 'off')
# shared labels, labelpad is to move the labels down (x label) or left (y label)
plt.xlabel("Outcomes of Each Roll", labelpad = 8)
plt.ylabel("Possibility", labelpad = 20)
plt.show()
