"""
    Unsupervised Learning
    Where we have data but no labels :(
    Somehow ML Model should be classifying the data to form some classes itslef


    k - means Clustering
    k is the number of classes we expect the model to create


    P   X   Y
    ----------
    A   1   1
    B   1   0
    C   0   2
    D   2   4
    E   3   5


    We have data-set as an example above for 5 observations
    each observation has 2 attributes

    We need to find the classes or clustuers :)

    Step-1
    ------
    Decide the value of k
    k -> 2
    k value 2 means, we will have 2 clusters or 2 classes

    We need to now choose 2 Random Points which serves as Centroids for 2 Clusters
    Randomly choosing A and C
    C1: A (1, 1)
    C2: C (0, 2)

    Step-2
    ------
    Calculate distance of every point from 2 centroids which we have randomly picked up
    Eucilidean Distance -> sqrt[square(x2-x1) + square(y2-y1)]


    P   X   Y   C1(1, 1)    C2(0, 2)
    --------------------------------
    A   1   1       0         1.4
    B   1   0       1         2.2
    C   0   2       1.4        0
    D   2   4       3.2       2.8
    E   3   5       4.5       4.2

    Step-3
    ------
    Arrange the Points as per distance for Centroids and create real clusters
    P   CLUSTER
    -----------
    A   C1
    B   C1
    C   C2
    D   C2
    E   C2

    Step-4
    ------
    Re-Check the Distances from newly created centroids by caluclating mean

    P   X   Y   NearestTo
    --------------------
    A   1   1   C1
    B   1   0   C1

    C   0   2   C2
    D   2   4   C2
    E   3   5   C2

    Cluster1Mean -> C1Mean = (1+1)/2, (1+0)/2       => (1, 0.5)
    Cluster2Mean -> C2Mean = (0+2+3)/3, (2+4+5)/3   => (1.7, 3.7)

    P   X   Y   C1Mean(1, 0.5)    C2Mean(1.7, 3.7)
    ----------------------------------------------
    A   1   1      0.5              2.7
    B   1   0      0.5              3.7
    C   0   2      1.8              2.4
    D   2   4      3.6              0.5
    E   3   5      4.9              1.9

    Based on above calculations, we have seen the new distances
    Let us, put the data points again in the clusters

    P   X   Y   NearestTo
    --------------------
    A   1   1   C1
    B   1   0   C1
    C   0   2   C1

    D   2   4   C2
    E   3   5   C2

    Step-5
    ------
    Repeat the Step#4 again and check if cluster changes or not
    In case cluster changes, redo the step4 and in case it wont change stop the algo and we have got our clusters

    P   X   Y   NearestTo
    --------------------
    A   1   1   C1
    B   1   0   C1
    C   0   2   C1

    D   2   4   C2
    E   3   5   C2

    Cluster1Mean -> C1Mean = (1+1+0)/3, (1+0+2)/3   => (0.7, 1)
    Cluster2Mean -> C2Mean = (2+3)/2, (4+5)/2       => (2.5, 4.5)

    Answer : Cluster Remains same :)

"""

import matplotlib.pyplot as plt
X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]

plt.scatter(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()