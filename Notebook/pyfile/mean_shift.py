import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import MeanShift
from mpl_toolkits.mplot3d import Axes3D

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

#clustering 
ms = MeanShift()
ms.fit(pcscores)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

n_clusters_ = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters_)
#print(labels)
colors = ['c','r','b','g','k','y','m']
pcscores_arr = np.array(pcscores)
#2D visualization
fig, ax = plt.subplots()
for i in range(len(pcscores_arr)):
    ax.scatter(pcscores_arr[i][2], pcscores_arr[i][3], c=colors[labels[i]])
ax.scatter(cluster_centers[:,2],cluster_centers[:,3], marker="x",color='k', s=150, linewidths = 5, zorder=10)
plt.title('2D Pokemon Clusters')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
plt.show()

"""#3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(pcscores_arr)):
    ax.scatter(pcscores_arr[i][0], pcscores_arr[i][1], pcscores_arr[i][2], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:,0],cluster_centers[:,1],cluster_centers[:,2], marker="x",color='k', s=150, linewidths = 5, zorder=10)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
plt.show()
print("Clusters centers points:")
print(cluster_centers)"""