#CHAPTER 11.
#MARKOV CHAINS
#state.
#The probabilities are called transition probabilities.
#The process can remainin the state it is in, and this occurs with probabilitypii.
#An initial probabilitydistribution, defined onS, specifies the starting state.
#Usually this is done byspecifying a particular state as the starting state.
#R. A. Howard1 provides us with a picturesque description of a Markov chain asa frog jumping on a set of lily pads.
#The frog starts on one of the pads and thenjumps from #lily pad to lily pad with the appropriate transition probabilities.
#Example 11.1 According to Kemeny, Snell, and Thompson,
#2 the Land of Oz is blessed by many things, but not by good weather.
#They never have two nice days in a row.
#If they have a nice day, they are just as likely to have snow as rain the next day.
#If they have snow or rain, they have an even chance of having the samethe next day.
#If there is change from snow or rain, only half of the time is this achange to a nice day.
#With this #information we form a Markov chain as follows
#We take as states the kinds of weather R, N, and S.
#From the above informationwe determine the transition probabilities.
#These are most conveniently representedin a square array as
#P=R    N    SR
#   1/2  1/4  1/4N
#   1/2   0   1/2S
#   1/4  1/4  1/2

#most occuring / solution should be B

#EE381 Alexander Fielding
# Project 6 Markov Chain

from pymarkovchain import MarkovChain
import numpy as np

n = 15 # time steps
N = 10000 # number simulations

#mc = MarkovChain("text")

states = ['R','N','S']
initialprobs = [0.25,0.5,0.25]
#mat = np.matrix([(1/3),(1/3),(1/3)],[0.5,0,0.5],[0.25,0.25,0.5])

def detInitialState():
    initialstate = np.random.choice(states,1,p = initialprobs)

    return initialstate

#Main
count = 0
while(count < N):
    count += 1
    state = detInitialState()

    print(state)
