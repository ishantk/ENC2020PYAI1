import pandas as pd
import numpy as np
import math

class DataSetHelper:

    def __init__(self):
        print("Preparing DataSet for ANN...")


    def preapre_data_set(self, file, target, normalize=False):

        df = pd.read_csv(file)
        target_indexes = {target: idx for idx, target in enumerate(sorted(list(set(df[target].values))))}

        X = df.drop([target], axis=1).values
        Y = np.vectorize(lambda x : target_indexes[x])(df[target].values)
        num_of_classes = len(target_indexes)

        if normalize:
            X = (X - X.mean(axis=0)) / X.std(axis=0)

        return X, Y, num_of_classes


    def kFold_cross_validation(self, n, folds):
        np.random.seed(1) # Seed to begin randomization
        indexes = np.random.permutation(n) # they are shuffled for us

        n_fold = int(n/folds)

        index_folds = []

        for i in range(folds):
            start_idx = i*n_fold
            end_idx = min([(i+1)*n_fold, n])

            index_folds.append(indexes[start_idx: end_idx])

        return index_folds


class ANN:

    def __init__(self, input_layer=None,
                 hidden_layer=None,
                 output_layer=None):

        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer

        self.network = []

        print("[ANN] MODEL CREATED")

        print("[ANN] MODEL DETAILS")
        print("[ANN] IL: {} HL: {} OL: {}".format(self.input_layer, self.hidden_layer, self.output_layer))

        print("[ANN] NETWORK DETAILS")
        print("NET: {}, LENGTH: {}".format(self.network, len(self.network)))

    def fit(self, X, Y, epochs):
        pass

    def predict(self, X):
        pass

    def feed_forward(self):
        pass

    def feed_backward(self):
        pass

    def update_weights(self):
        pass

    def summation(self, inputs, weights):
        """
        :param inputs:  [1, 2, 3, 4, 5]
        :param weights: [1, 1, 2, 3, 1]
        :return: dot product of inputs and weights
            zip -> [[1, 1], [2, 1], [3, 2], [4, 3], [5, 1]]
        """
        return sum([i * w for (i, w) in zip(inputs, weights)])

    def sigmoid(self, sum):
        return 1.0 / (1.0 + math.exp(-sum))

    def sigmoid_derivation(self, sigmoid):
        return sigmoid * (1.0 - sigmoid)

    def one_hot_encoding(self):
        pass


def main():
    file_name = "seeds.csv"
    helper = DataSetHelper()
    X, Y, num_of_classes = helper.preapre_data_set(file=file_name, target="y", normalize=True)

    print("INPUT X")
    print(X)

    print()

    print("OUTPUT Y")
    print(Y)

    print()

    print("NUM OF CLASSES")
    print(num_of_classes)

    print()

    print("====================")

    print()

    num_of_observations, input_features = X.shape
    print("num_of_observations", num_of_observations)
    print("input_features", input_features)

    print()

    print("ALL INDEXES")
    index_all = np.arange(num_of_observations)
    print(index_all)

    # Lets divide observations into 4 folds :)
    index_folds = helper.kFold_cross_validation(n=num_of_observations, folds=4)

    print("FOLD INDEXES: ", len(index_folds))
    print(index_folds)

    print()
    print("Iterating in Folds")
    print("~~~~~~~~~~~~~~~~~~~~~")

    # Loop will run 4 times as we have 4 folds
    # hence we will train the model on 4 different data set parts :)
    for i, index_test in enumerate(index_folds):
        print(i)
        print(index_test)

        # index_test should be considered indexes for the observations to be tested
        # training data set would be all - testing
        # i.e. index_train = index_all - index_test

        index_train = np.delete(index_all, index_test)

        print(index_train)

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # Prepare DataSet to train Model based on Indexes :)
        X_train, Y_train = X[index_train], Y[index_train]
        X_test, Y_test = Y[index_test], Y[index_test]

        print("------------------")

        print(X_train)
        print(Y_train)

        print()

        print(X_test)
        print(Y_test)

        print("------------------")
        print()




if __name__ == '__main__':
    main()