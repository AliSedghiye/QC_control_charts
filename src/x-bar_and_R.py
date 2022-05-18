import numpy as np
import matplotlib.pyplot as plt
import statistics


# generate data
x = np.array([list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=17, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5)),
        list(np.random.normal(loc=10, scale=2, size=5))])

x_bar = []
R = []

for samples in x:
    x_bar.append(samples.mean())
    R.append(samples.max() - samples.min())

# Plot x and R charts
fig, axs = plt.subplots(2, figsize = (20,10))

# x chart
axs[0].plot(x_bar, linestyle='-', marker='o', color='black')
axs[0].axhline((statistics.mean(x_bar)+0.577*statistics.mean(R)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)-0.577*statistics.mean(R)), color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(x_bar)), color='blue')
axs[0].set_title('x-bar Chart')
axs[0].set(xlabel='Group', ylabel='Mean')

# R chart
axs[1].plot(R, linestyle='-', marker='o', color='black')
axs[1].axhline((2.574*statistics.mean(R)), color='red', linestyle='dashed')
axs[1].axhline((0*statistics.mean(R)), color='red', linestyle='dashed')
axs[1].axhline((statistics.mean(R)), color='blue')
axs[1].set_ylim(bottom=0)
axs[1].set_title('R Chart')
axs[1].set(xlabel='Group', ylabel='Range')


plt.savefig('R_chart.png', dpi=300, bbox_inches='tight')
plt.show()