from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt

# from scipy.spatial.distance import cdist

my_data = np.loadtxt("ClusterPlot.csv", delimiter=",", skiprows=1, usecols=(1, 2))
x_values = my_data[:, 0]
y_values = my_data[:, 1]

X = np.array(list(zip(x_values, y_values))).reshape(len(x_values), 2)

sil = []
'''distortions = []'''
inertias = []
'''mapping1 = {}'''
mapping2 = {}

for k in range(1, 10):
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(X)
    '''distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / X.shape[0])'''
    inertias.append(kmeanModel.inertia_)

    '''mapping1[k] = sum(np.min(cdist(X, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / X.shape[0]'''
    mapping2[k] = kmeanModel.inertia_

    # the silhouette method only works with 2 or more clusters
    if k > 1:
        sil.append(silhouette_score(X, kmeanModel.labels_, metric='euclidean'))

'''print("Values for distortion")
for key, val in mapping1.items():
    print(str(key) + ' : ' + str(val))
'''
print("\n\nValues for inertias")
for key, val in mapping2.items():
    print(str(key) + " : " + str(val))

print("\n\nSilhouette Scores")
for key, val in enumerate(sil):
    print(str(key + 1) + " : " + str(val))

'''plot1 = plt.figure(1)
plt.plot(K, distortions, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method using Distortion')
'''

plot1 = plt.figure(1)
plt.plot(range(1, 10), inertias, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Inertia')
plt.title('The Elbow Method using Inertia')

plot2 = plt.figure(2)
plt.plot(range(2, 10), sil, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Silhouette Score')
plt.title("The Silhouette Method")

plt.show()
