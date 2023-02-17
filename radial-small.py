import matplotlib.pyplot as plt
import pandas as pd
import pandasql as ps
from math import pi
plt.rcParams.update({'font.size': 12})

pd.set_option('display.max_rows', None)
#df = pd.read_csv('categories.csv')

df = pd.DataFrame({
'group': ['LULS', 'DDC', 'UDC'],
'CH': [7 ,7, 1],
'IS': [0, 0, 1],
'EA': [0, 0, 1],
'HD': [0, 0, 1],
'BU': [0, 0, 1],
'JU': [0, 0, 1],
'OT': [1, 1, 1],
'GE': [1, 2, 2]
})


#num vars
categories=list(df)[1:]
N = len(categories)

# angle of each axis in the plot
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

#spider plot
ax = plt.subplot(111, polar=True)

#first axis on top
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#one axe per variable + add labels
plt.xticks(angles[:-1], categories)

#ylabels
ax.set_rlabel_position(0)
plt.ylim(0,7)

#PLOTTING
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="LULS")
ax.fill(angles, values, 'b', alpha=0.1)

# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="DDC")
ax.fill(angles, values, 'r', alpha=0.1)

# Ind3
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="UDC")
ax.fill(angles, values, 'g', alpha=0.1)

#legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the graph
plt.show()
