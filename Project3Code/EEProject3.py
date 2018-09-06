import random
import numpy as np
import pylab as plt
from scipy import stats

def diceroll():
    die = random.randint(1,6)
    return die
    
#Main
X = []
count = 0
countb = 0

while( countb < 10000):
    countb +=1
    success = 0
    while(count < 1001):
        count +=1
        alist = []
        i = 0
        while(i < 3):
            i+=1
            nxt = diceroll()
            if nxt != 6:
                i = 3
            else:
                alist.append(nxt)
                if len(alist) == 3:
                    success +=1          
        X.append(success)

num_bins = 16
counts, bins = np.histogram(X, bins=num_bins)
bins = bins[:-1] + (bins[1] - bins[0])/2
probs = counts/float(counts.sum())

xk = np.arange(len(probs))
pk = probs
custm = stats.rv_discrete(name='custm', values=(xk, pk))

fig, ax = plt.subplots(1, 1)
ax.plot(xk, custm.pmf(xk), 'ro', ms=8, mec='r')
ax.vlines(xk, 0, custm.pmf(xk), colors='r', linestyles='-', lw=2)
plt.title('Experiment Results')
plt.ylabel('Probability of Success')
plt.xlabel('Number of successes in n=1000 trials')
plt.show()




