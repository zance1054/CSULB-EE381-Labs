#most occuring / solution should be B for number 2

#EE381 Alexander Fielding
# Project 6 Markov Chain

import numpy as np
from matplotlib import pylab as pyplt
from matplotlib.legend_handler import HandlerLine2D

n = 16 # time steps + 1
N = 10000 # number simulations
X = []
a = 0
b = 1
nbins = 50


#mc = MarkovChain("text")

states = ['R','N','S']
initialprobs = [0.25,0.5,0.25]
stateR = [(1/3),0.5,0.25]
stateN = [(1/3),0.5,0.25]
stateS = [(1/3),0.5,0.25]
probR = []
probN = []
probS = []

def detInitialState():
    initialstate = np.random.choice(states,1,p = initialprobs)

    return initialstate

def nextState(probs):
    nextState = np.random.choice(states,1,probs)
    return nextState

def detprobability():
    return p
#Main
count = 0
state = detInitialState()
X.append(state)
nums = []
while(count < n):
    nums.append(count)
    count += 1
    if(state == 'R'):
        state = nextState(stateR)
        probR.append(1)
        probN.append(0)
        probS.append(0)
    elif(state == 'N'):
        state = nextState(stateN)
        probN.append(1)
        probS.append(0)
        probR.append(0)
    elif(state == 'S'):
        state = nextState(stateS)
        probS.append(1)
        probR.append(0)
        probN.append(0)
    X.append(state)

line1, = pyplt.plot(nums,probR,linestyle='--',label='R')
line2, = pyplt.plot(nums,probS,linestyle='--',label='S')
line3, = pyplt.plot(nums,probN,linestyle='--',label='N')
pyplt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
pyplt.title('Three-State Markov Chain Result from 10,000 simulations')
pyplt.ylabel('Probability')
pyplt.xlabel('Step Number')
pyplt.show()
