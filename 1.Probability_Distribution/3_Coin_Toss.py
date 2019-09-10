import random

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# funtion in order to save figures.
def saveFig(plt, num_sample):
    import os

    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'Distribution/')
    file_name = "3_Coin_Toss_numSample:"+str(num_sample)+".png"

    # in case the directory does not exist, create a directory for saving figures.
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.savefig(results_dir + file_name)



# number of sampling
num_sample = 100000

# 0:tail, 1:head
samples = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)] for i in range(num_sample)]

# random variable 'X': total number of heads, possible values of X is from 0 to 3
X_values_cnt = [0, 0, 0, 0]


for sample in samples:
    X_values_cnt[sum(sample)] = X_values_cnt[sum(sample)] + 1

print(X_values_cnt)

# all possible values of random variable X
X_values = ('0', '1', '2', '3')

# number of possible values of X
num_X_values = np.arange(len(X_values))

# probabilities of occuring each outcome
val_probs = [x / num_sample for x in X_values_cnt]


# plotting the bar chart of the probability distribution of random variable 'X'
plt.bar(num_X_values, val_probs, align='center', alpha=0.5)
plt.xticks(num_X_values, X_values)
plt.ylabel('Probability')
plt.title('3_Coin_Toss, Number of Sampling:{}'.format(num_sample))
saveFig(plt,num_sample)
plt.show()

