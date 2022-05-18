import numpy as np
import matplotlib.pyplot as plt
import statistics

# generate data
x = np.array([list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=13, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11)),
        list(np.random.normal(loc=10, scale=2, size=11))])

x_bar = []
s = [] 
for samples in x:
    x_bar.append(samples.mean())
    s.append(np.std(samples))

# Plot x and S charts
fig, axs = plt.subplots(2, figsize=(20,10))

# x chart
axs[0].plot(x_bar, linestyle='-', marker='o', color='black')
axs[0].axhline((statistics.mean(x_bar)+0.927*statistics.mean(s)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)-0.927*statistics.mean(s)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)), color='blue')
axs[0].set_title('x-bar Chart')
axs[0].set(xlabel='Group', ylabel='Mean')

# S chart
axs[1].plot(s, linestyle='-', marker='o', color='black')
axs[1].axhline((1.649*statistics.mean(s)), color='red', linestyle='dashed')
axs[1].axhline((0.321*statistics.mean(s)), color='red', linestyle='dashed')
axs[1].axhline((statistics.mean(s)), color='blue')
axs[1].set_title('s Chart')
axs[1].set(xlabel='Group', ylabel='Range')


plt.savefig('S_chart.png', dpi=300, bbox_inches='tight')
plt.show()