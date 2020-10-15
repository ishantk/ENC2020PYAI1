"""
    KNN - K Nearest Neighbours
"""

import math

# Euclidean Distance Formula | sqrt of sq(x1-x2) + sq(y2-y1)
def euclidean_distance(point1, point2):

    sum = 0

    for i in range(len(point1)):
        sum += math.pow( (point1[i] - point2[i]), 2)

    return math.sqrt(sum)


def main():

    # data set of height and weight
    data_set = [
        [65.2, 120.22],
        [71.5, 60.77],
        [69.8, 153.11],
        [67.2, 148.35],
        [68.5, 133.11],
        [69.1, 148.55],
        [70.5, 160.22],
        [70.8, 112.10],
        [67.3, 112.88],
        [66.4, 127.11]
    ]

    # Predict the weight for the given height
    given_height = [60]

    # KNN - k value 3 means consider the closest 3 neighbours :)
    k = 3

    # 1. Evaluate Distance for all the data points
    neighbour_distances = []

    for idx, data_point in enumerate(data_set):
        distance = euclidean_distance(data_point[:-1], given_height)
        print("Distance between {} and {} is: {}".format(data_point[:-1], given_height, distance))

        neighbour_distances.append((distance, idx))

    neighbour_distances = sorted(neighbour_distances)
    print(neighbour_distances)

    k_nearest_neighbours = neighbour_distances[:k]
    print("k_nearest_neighbours")
    print(k_nearest_neighbours)


    # This is a Regression Problem
    # We must compute the mean of output labels

    output_labels = []
    for neighbour in k_nearest_neighbours:
        idx = neighbour[1]
        output_labels.append(data_set[idx][1])

    print(output_labels)


    predicted_weight = sum(output_labels)/len(output_labels)
    print("Predicted Weight for Given Height", given_height, "is:", predicted_weight)

    # If it is a classification problem we need to take the mode :)

if __name__ == '__main__':
    main()