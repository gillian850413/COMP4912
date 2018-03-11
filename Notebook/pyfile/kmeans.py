import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import MeanShift
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

#load pokemon data
pokemon = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/COMP4912/Data/pokemon-challenge/pokemon.csv")

#standardize the data
stat = ['HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed']
poke_stat_scaled = StandardScaler().fit_transform(pokemon[stat])

print("mean: "+str(poke_stat_scaled[:,0].mean()))  # very close to 0
print("SD: "+str(poke_stat_scaled[:,0].std()))  # very close to 1

#pca
pca = PCA(n_components = 'mle',svd_solver='full') #maximum likelihood estimation
pcscores = pd.DataFrame(pca.fit_transform(poke_stat_scaled)) 
pcscores.columns = ['PC'+str(i+1) for i in range(len(pcscores.columns))]
#print(pca.explained_variance_ratio_)
#print(pca.explained_variance_)

print("Number of principle components: "+str(pca.n_components_))
pcaVarRatioSum = 0
for i in range(pca.n_components_):
    pcaVarRatio = pca.explained_variance_ratio_.tolist()
    pcaSingleVarRatio = "{:.2%}".format(pcaVarRatio[i])
    print("PC"+str(i+1)+": "+str(pcaSingleVarRatio))
    pcaVarRatioSum = pcaVarRatioSum + pcaVarRatio[i]

cluster_num = 3
kmeans = KMeans(n_clusters=cluster_num)
kmeans.fit(pcscores)

centroids = kmeans.cluster_centers_
klabels = kmeans.labels_
#print(centroids)

gname = []
gcenters = []
for i in range(cluster_num):
    gname.append(i)
    center = centroids[i].tolist()
    (x, y) = (center[0], center[1])
    gcenters.append((x, y))
    groups = dict(zip(gname, gcenters))

for i in range(cluster_num):
    group = 'cluster'+str(i+1)
    print("Count of "+group+' :', str(klabels.tolist().count(i)))

pcscores_arr = np.array(pcscores)
pkmeans = pokemon.copy()
pkmeans['klabel'] = klabels
KmeansPoke = pd.concat([pkmeans, pcscores], axis=1)

colors = plt.cm.Pastel1(np.linspace(0, 1, 10))

plt.figure()
groups_keys = list(groups.keys())
#loop through labels and plot each cluster
for i, label in enumerate(groups.keys()):

    #add data points 
    plt.scatter(x=KmeansPoke.loc[KmeansPoke['klabel']==label, 'PC1'], 
                y=KmeansPoke.loc[KmeansPoke['klabel']==label,'PC2'],
                color=colors[i])
    
    #add label
    plt.annotate(label, xy = groups[groups_keys[i]],
                 horizontalalignment='center', verticalalignment='center',
                 size=20, color='k') 
    

plt.title('2D Pokemon Kmeans Clustering')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
plt.legend(groups_keys, loc='best')
plt.show()
 


