# Upper Confidence Bound

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
N = 10000                               ## number of rounds
d = 10                                  ## advert variations 
ads_selected = integer(0)               ## vector of 10000 ads selected ine ach round 
numbers_of_selections = integer(d)      ## vector of size d that contains number of selections
sums_of_rewards = integer(d)            ## vector of size d that contains number of selections
total_reward = 0                        ## 
for (n in 1:N) {                        ## for total number of rounds N...
  ad = 0                                ## initialize tracker
  max_upper_bound = 0                   ## initialized in each new round - highest upper confidence bound
  for (i in 1:d) {                      ## for each version of ad 
    if (numbers_of_selections[i] > 0) {               ## if  version of ad was selected more than once       
      average_reward = sums_of_rewards[i] / numbers_of_selections[i]      ## as in UCB formula
      delta_i = sqrt(3/2 * log(n) / numbers_of_selections[i])             ## as in UCB formula
      upper_bound = average_reward + delta_i                              ## as in UCB formula
    } else {                                          ## if not then
        upper_bound = 1e400
    }      
    if (upper_bound > max_upper_bound) {                         ## swap upper bound to the new highest upper bound
      max_upper_bound = upper_bound                       
      ad = i                                                     ## to track index
    }
  }
  ads_selected = append(ads_selected, ad)                        ## storing ads selected
  numbers_of_selections[ad] = numbers_of_selections[ad] + 1      ## update number of adsselection
  reward = dataset[n, ad]                                        ## reward
  sums_of_rewards[ad] = sums_of_rewards[ad] + reward             
  total_reward = total_reward + reward                           ## total amount of rewards
}

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')