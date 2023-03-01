import matplotlib.pyplot as plt
import pandas as pd
import pandasql as ps
import numpy as np
import plotly.express as px
plt.rcParams.update({'font.size': 12})

#heatmap to show document similarities

with open("similarities.txt", "r", encoding="utf-8") as f:
    sims = f.read().splitlines()
    # print(sims)

data = [[sims[0], sims[1], sims[2]], [sims[3], sims[4], sims[5]], [sims[6], sims[7], sims[8]]]

fig, ax = plt.subplots()
fig = px.imshow(data,
                labels=dict() , x=['Dewey', 'Leeds', 'Universal'],y=['Dewey', 'Leeds', 'Universal'], title='Document Similarities')
fig.show()
