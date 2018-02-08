import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#load pokemon data
pokemon = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/FYP2/Data/pokemon-challenge/pokemon.csv")

#standardize the data
stat = ['HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed']
poke_stat_scaled = StandardScaler().fit_transform(pokemon[stat])

print(poke_stat_scaled[:,0].mean())  # very close to 0
print(poke_stat_scaled[:,0].std())  # very close to 1

#pca (principal component analysis) projection to 2D
pca = PCA(n_components = 0.8) # consider enough components to explain 80% of the variance
pcscores = pd.DataFrame(pca.fit_transform(poke_stat_scaled)) #6 stats -> 4 principle components
print("Number of dimensions after PCA: " + str(len(pcscores.columns)))
pcscores.columns = ['PC'+str(i+1) for i in range(len(pcscores.columns))]

#loading factors
loadings = pd.DataFrame(pca.components_, columns=stat)
loadings.index = ['PC'+str(i+1) for i in range(len(pcscores.columns))]

#visualize the square values of loading factors
load_sqr = loadings**2
ax1 = sns.heatmap(load_sqr.transpose(), linewidths=0.5, cmap="BuGn", annot=True)
ax1.set_xticklabels(ax1.xaxis.get_majorticklabels(), rotation=0)
ax1.set_yticklabels(ax1.yaxis.get_majorticklabels(), rotation=0)
plt.show()

#visualize the actual value of loading factors
ax2 = sns.heatmap(loadings.transpose(), center=0, linewidths=0.5, cmap="RdBu", vmin=-1, vmax=1, annot=True)
ax2.set_xticklabels(ax2.xaxis.get_majorticklabels(), rotation=0)
ax2.set_yticklabels(ax2.yaxis.get_majorticklabels(), rotation=0)
plt.show()
