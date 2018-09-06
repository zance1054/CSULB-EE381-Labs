# EE 381 project 4
# Alexander Fielding
# problem 2

import numpy as np
import pylab as plt

X = [] # Results
F = []

def expdist(t):
    if t.any() < 0:
        return 0
    else:
        result = 2 ** (-2 * t)
        return result


#Main
count = 0
t = np.random.exponential(1,10000)
f = np.random.exponential(1,10000)

while(count < 9999):
    count = count + 1
    X.append(expdist(t[count]))
    F.append(expdist(f[count]))

    
edgecolor='w';         
bins=[float(x) for x in plt.linspace(0,1,10)]
h1, bin_edges = plt.histogram(X,bins,density=True)
    # Define points on the horizontal axis
be1=bin_edges[0:plt.size(bin_edges)-1]
be2=bin_edges[1:plt.size(bin_edges)]
b1=(be1+be2)/2     
barwidth=b1[1]-b1[0] # Width of bars in the bargraph
plt.close('all') 
# PLOT THE BAR GRAPH 
fig1=plt.figure(1) 
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
plt.title('Exponential Distribution')
plt.ylabel('PDF')
plt.xlabel('Random Variable T')
 #PLOT THE GAUSSIAN FUNCTION
 
plt.plot(b1,,'r')

