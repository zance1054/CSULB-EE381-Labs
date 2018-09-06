#Alexander Fielding
# EE 381 Problem 4

import random

#globals

pknot = 0.4
epsilon = 0.03
epsilonknot = 0.02

# Determine Message
def message(m):
    if( m <= pknot):
        S = 0
    else:
        S = 1

    return S

#Determine Recieved Message
def received(t,S):
    if( S == 0 and t <= epsilonknot):
        R = 1
    elif( S == 0 and t > epsilonknot):
        R = 0
    elif( S == 1 and t <= epsilon):
        R = 1
    elif( S == 1 and t > epsilon):
        R = 0

    return R
        

