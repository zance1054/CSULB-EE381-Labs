# EE 381 project 4
# Alexander Fielding
# problem 3

import pylab as plt
import numpy as np

def gaussian(mu,sig,z):
     f=np.exp(-(z-  mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
     return f 
 
lifespan = 45       
stnddeviation = 45 * np.sqrt(24)
mean = 24 * 45

count = 0
X = []
Result = []

while(count < 10000):
    count = count + 1
    carton = np.random.exponential(lifespan,24)
    C = 0 #Sum 
    for i in carton:
        C += i
    X.append(C)
    Result.append(np.cumsum(C))
    

nbins=30;
# Number of books ; Number of bins
edgecolor='w';      
# Color separating bars in the bargraph     
#    
# Create bins and histogram     
bins=[float(x) for x in plt.linspace(400,1800,nbins+1)]
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
 #PLOT THE GAUSSIAN FUNCTION
f=gaussian(mean,stnddeviation,b1) 

plt.plot(b1,f,'r')
plt.title('PDF of battery lifespan')
plt.ylabel('Probability')
plt.xlabel('LifeSpan')   
