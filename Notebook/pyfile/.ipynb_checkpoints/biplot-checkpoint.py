import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
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

# Create labels based on Type 1
labels = set(pokemon['Type 1'])
pokemon['type'] = pokemon['Type 1']
lab_dict = dict()
for i, elem in enumerate(labels):
    lab_dict[elem] = i
pokemon = pokemon.replace({'type' : lab_dict})

pc_types = pcscores.copy()
pc_types['Type'] = pokemon['Type 1']

# Biplots
def biplot(pcscores, loadings, xval=0, yval=1, max_arrow=0.2, alpha=0.4):
    n = loadings.shape[1]
    pcx = pcscores.iloc[:, xval]
    pcy = pcscores.iloc[:, yval]
    scalex = 1.0 / (pcx.max() - pcx.min())  # Rescaling to be from -1 to +1
    scaley = 1.0 / (pcy.max() - pcy.min())
    print(pcx)
    print(scalex)
    pcx = pcx * scalex
    pcy = pcy * scaley
    print(pcx)
    
    g = sns.lmplot(x='PC{}'.format(xval + 1), y='PC{}'.format(yval + 1), hue='Type', data=pcscores,
                   fit_reg=False, size=6, palette='muted')
    

    for i in range(n):
        lx = loadings.iloc[xval, i]
        ly = loadings.iloc[yval, i]
        # Only plot the longer ones
        
        length = sqrt(lx ** 2 + ly ** 2)
        if length < max_arrow:
            continue

        plt.arrow(0, 0, lx, ly, color='k', alpha=0.9)
        plt.text(lx * 1.15, ly * 1.15,
                 loadings.columns.tolist()[i], color='k', ha='center', va='center')

    g.set(ylim=(-1, 1))
    g.set(xlim=(-1, 1))
    
# Actually make a biplot (PC3 vs PC4)
biplot(pc_types, loadings, 2, 3, max_arrow=0.3)
    
    