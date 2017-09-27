### Reinforcement Learning - Upper Confidence Bound

## Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


## Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

## Random Selecton for Comparison:
        
import random
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    total_reward = total_reward + reward  

### Gives around 1200 rewards

### IMPLEMENT UCB

## Initial round:
import math                                  ## for sqare root in line 41       
N = 10000                                    ## number of rounds
d = 10                                       ## number of different ads
ads_selected = []                            ## ad that was selected on each round
numbers_of_selections = [0] * d              ## vector of size d containing only zeros for first initial round
sums_of_rewards = [0] * d                    ## vector of size d containing only zeros for first initial round
total_reward = 0
## All the rounds N:

for n in range(0, N):                           ### the average reward of ad i up to round n
        ad = 0
        max_upper_bound = 0
        for i in range(0, d):
            if (numbers_of_selections[i] > 0):    ## For first 10 rounds
                average_reward = sums_of_rewards[i] / numbers_of_selections[i]    
                delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])  ## Confidence interval; add one as indexes starts at zero
                upper_bound = average_reward + delta_i
            else:
                upper_bound = 1e400              ## For first 10 rounds to keep loop going 
            if upper_bound > max_upper_bound:     ## swap to max upper bound for a new selection 
                    max_upper_bound = upper_bound
                    ad = i                           ## to keep track of an index
        ads_selected.append(ad)                     ## append the list
        numbers_of_selections[ad] = numbers_of_selections[ad] + 1   ## increase value of the vector
        reward = dataset.values[n, ad]                             ## get the reward
        sums_of_rewards[ad] = sums_of_rewards[ad] + reward
        total_reward = total_reward + reward

## TOTAL REWARD IS 2178!!!!

### Viusalising the result
plt.hist(ads_selected)
plt.title('Most Popular Ads')
plt.xlabel('Ads')
plt.ylabel('Number of choices')
plt.show()





























