# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bars
barWidth = 0.25

# set heights of bars
LULS = [7, 0, 0, 0, 0, 0, 1, 1]
DDC = [7, 0, 0, 0, 0, 0, 1, 2]
UDC = [1, 1, 1, 1, 1, 1, 1, 2]

# Set position of bar on X axis
r1 = np.arange(len(LULS))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, LULS, color='#7f6d5f', width=barWidth, edgecolor='white', label='LULS')
plt.bar(r2, DDC, color='#557f2d', width=barWidth, edgecolor='white', label='DDC')
plt.bar(r3, UDC, color='#2d7f5e', width=barWidth, edgecolor='white', label='UDC')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(LULS))], ['CH', 'IS', 'EA', 'HD', 'BU', 'JU', 'OT', 'GE'])

# Create legend & Show graphic
plt.legend()
plt.show()
