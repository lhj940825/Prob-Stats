import random

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# funtion in order to save figures.
def saveFig(plt, num_sample):
    import os

    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'Figures/')
    file_name = "Coin_Toss_numSample:" + str(num_sample) + ".png"

    # in case the directory does not exist, create a directory for saving figures.
    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)

    plt.savefig(results_dir + file_name)


# number of sampling
num_sample = 1000

# # random variable 'Xi': Result of the coin toss which is either Tail or Head in i-th trials
# Experiment: toss one coin, 0:tail, 1:head,
samples = [random.randint(0, 1) for i in range(num_sample)]
samples = np.array(samples)


# amass the number of Heads and the value in each index of the list denotes the total number of resulted heads until the index-th trial.
cummulative_Head_cnt = np.cumsum(samples)


# the sample mean Zn = (X1+X2....+Xn)/n
# calculate the sample mean by number of trials
num_trial = np.array([i for i in range(1, num_sample + 1)])
sample_means = np.divide(cummulative_Head_cnt, num_trial)



# plotting the line chart of the Zn
plt.plot(num_trial,sample_means)
plt.ylabel('Y axis: Sum of Heads / Num of trials')
plt.xlabel('X axis: Num of Experiments')
plt.title('Coin Toss Example')
saveFig(plt,num_sample)
plt.show()
