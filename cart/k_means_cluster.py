#This program is used to represent the k-means cluster algorithm as presented in class
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("C:\\Users\David\Documents\CS445\GMM_data_fall2019.txt")
k= 7
len = data.__len__()
centroids = np.zeros((k,2))

#Get random points for the centroids
for i in range(0,k):
 rand_index = np.random.choice(data.__len__(),1)
 centroids[i] = data[rand_index]

#Assigns each point to a cluster
#Goes each datapoint and finds the centroid closest to it
#Places the point in the corresopnding cluster
def get_clusters(data, centroids):
    clusters = [[] for i in range(k)]
    for i in range(0,len):
        min_dist = 1000.0
        for j in range(0,k):
           p1 = centroids[j]
           p2 = data[i]
           dist = np.linalg.norm(p1 - p2)
           if dist < min_dist:
               index = j
               min_dist = dist
        point = data[i]
        clusters[index].append(point)
    return clusters

#Calculates the new_means for each cluster
#Finds the total x and y value for each cluster, then divides each by the length of the cluster
#Returns the list of new means/ centroids
def get_means(clusters):
    new_means = np.zeros((k, 2))

    for i in range(0,k):
        x_tot = 0
        y_tot = 0
        cluster_len = clusters[i].__len__()
        for j in range(0,cluster_len):
            point = clusters[i][j]
            x_tot += point[0]
            y_tot += point[1]

        if cluster_len == 0:
            cluster_len = 1

        new_means[i] = [x_tot/float(cluster_len), y_tot/float(cluster_len)]
    return new_means

#Checks if the difference between the old centroids and the new ones are different
#Returns False if they are
#Returns True if they aren't
#Has a tolerance of .2 in difference
def check_means(centroids, new_means):
    done = True
    for i in range(0,k):
        centroid_x = round(centroids[i][0],2)
        new_means_x = round(new_means[i][0],2)
        centroid_y = round(centroids[i][1],2)
        new_means_y = round(new_means[i][1],2)

        if np.abs(centroid_x-new_means_x) >= .2 or np.abs(centroid_y-new_means_y) >= .2:
           done = False

    return done

done = False
count = 0
#Execute the k-means algorithm until done or 100 times
while not done and count <= 100:
    clusters = get_clusters(data,centroids)
    new_means = get_means(clusters)
    done = check_means(centroids,new_means)
    count += 1
    if not done:
        centroids = new_means

#Handle Plotting
colors = ['r','b','g','y','k','c','m']
#assign each data point to the correct cluster by color for the plot
for i in range(0,k):
    for j in range(0,clusters[i].__len__()):

        plt.scatter(clusters[i][j][0],clusters[i][j][1],15,c=colors[i])

plt.show()











