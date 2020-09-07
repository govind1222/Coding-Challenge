from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt

my_data = np.loadtxt("ClusterPlot.csv", delimiter=",", skiprows=1, usecols=(1, 2))
x_values = my_data[:, 0]
y_values = my_data[:, 1]
X = np.array(list(zip(x_values, y_values))).reshape(len(x_values), 2)

sil = []  # array to store silhouette scores for each KMeans model
squared_error = []

for k in range(1, 10):
    # Building and fitting the mode
    kmeanModel = KMeans(n_clusters=k).fit(X)

    squared_error.append(kmeanModel.inertia_)

    # the silhouette method only works with 2 or more clusters
    if k > 1:
        sil.append(silhouette_score(X, kmeanModel.labels_, metric='euclidean'))

# printing out values
print("\n\nValues for inertias")
for key, val in enumerate(squared_error):
    print(str(key) + " : " + str(val))

print("\n\nSilhouette Scores")
for key, val in enumerate(sil):
    print(str(key + 1) + " : " + str(val))

# plotting the squared error values
plot1 = plt.figure(1)
plt.plot(range(1, 10), squared_error, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Inertia')
plt.title('The Elbow Method using Squared Error')

# plotting the silhouette scores
plot2 = plt.figure(2)
plt.plot(range(2, 10), sil, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Silhouette Score')
plt.title("The Silhouette Method")

plt.show()
