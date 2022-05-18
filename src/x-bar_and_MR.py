import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import statistics 

# generate data
x = pd.Series(np.random.normal(loc=10, scale=2, size=10))

MR = [np.nan]

# 1 to len(x) because MR range equal to ( x range - 1 ) 
for i in range(1, len(x)):
    MR.append(abs(x[i] - x[i-1]))

MR = pd.Series(MR)

data = pd.concat([x, MR], axis = 1).rename(columns={0:"x", 1:"MR"})

# Plot x and mR charts
fig, axs = plt.subplots(2, figsize = (20,10), sharex=True)

# x chart
axs[0].plot(data['x'], linestyle='-', marker='o', color='black')
axs[0].axhline(statistics.mean(data['x']), color='blue')
axs[0].axhline(statistics.mean(data['x'])+3*statistics.mean(data['MR'][1:len(data['MR'])])/1.128, color = 'red', linestyle = 'dashed')
axs[0].axhline(statistics.mean(data['x'])-3*statistics.mean(data['MR'][1:len(data['MR'])])/1.128, color = 'red', linestyle = 'dashed')
axs[0].set_title('Individual Chart')
axs[0].set(xlabel='Unit', ylabel='Value')

# MR chart
axs[1].plot(data['MR'], linestyle='-', marker='o', color='black')
axs[1].axhline(statistics.mean(data['MR'][1:len(data['MR'])]), color='blue')
axs[1].axhline(statistics.mean(data['MR'][1:len(data['MR'])])+3*statistics.mean(data['MR'][1:len(data['MR'])])*0.8525, color='red', linestyle ='dashed')
axs[1].axhline(statistics.mean(data['MR'][1:len(data['MR'])])-3*statistics.mean(data['MR'][1:len(data['MR'])])*0.8525, color='red', linestyle ='dashed')
axs[1].set_ylim(bottom=0)
axs[1].set_title('MR Chart')
axs[1].set(xlabel='Unit', ylabel='Range')


plt.savefig('MR_chart.png', dpi=300, bbox_inches='tight')
plt.show()
