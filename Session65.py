"""
    Coding ANN
    Part-IV

    Training Model
    Use Backpropagation with learning rate

"""

import pandas as pd
import numpy as np
import math
import random


class DataSetHelper:

    def __init__(self):
        print("Preparing DataSet for ANN...")

    def preapre_data_set(self, file, target, normalize=False):

        df = pd.read_csv(file)
        target_indexes = {target: idx for idx, target in enumerate(sorted(list(set(df[target].values))))}

        X = df.drop([target], axis=1).values
        Y = np.vectorize(lambda x: target_indexes[x])(df[target].values)
        num_of_classes = len(target_indexes)

        if normalize:
            X = (X - X.mean(axis=0)) / X.std(axis=0)

        return X, Y, num_of_classes

    def kFold_cross_validation(self, n, folds):
        np.random.seed(1)  # Seed to begin randomization
        indexes = np.random.permutation(n)  # they are shuffled for us

        n_fold = int(n / folds)

        index_folds = []

        for i in range(folds):
            start_idx = i * n_fold
            end_idx = min([(i + 1) * n_fold, n])

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

        # we have no hidden layer and ANN will just have IL and OL
        if len(hidden_layer) == 0:
            self.network.append(self.create_layer(input=input_layer, output=output_layer))
        # we have hidden layer(s)
        else:
            # the very first will always be input and 0th index of hidden layer
            # for our use case we have hidden_layer = [5]
            self.network.append(self.create_layer(input=input_layer, output=hidden_layer[0]))

            # for our other cases where have hidden_layer = [5, 4, 6]
            for i in range(1, len(self.hidden_layer)):
                self.network.append(self.create_layer(input=hidden_layer[i-1], output=hidden_layer[i]))


            # last layer must be connected to the output layer
            self.network.append(self.create_layer(input=hidden_layer[-1], output=output_layer))

    def create_layer(self, input, output):
        random.seed(1)
        layer = []

        for i in range(output):
            weights = [random.random() for _ in range(input)]
            node = {
                "weights": weights,
                "output": None,
                "delta": None
            }
            layer.append(node)
        return layer

    # Train the Model
    def fit(self, X, Y, epochs):

        for i in range(epochs):
            for (x, y) in zip(X, Y):
                # 1. Feed Forward the Data
                self.feed_forward(x)

                # 2. Convert the Target into One Hot Encoding i.e. we have classes as 1s and 0s for the model
                y_one_hot = self.one_hot_encoding(y, self.output_layer)

                # 3. Feed Backward the Data i.e. Errors to compute delta
                self.feed_backward(y_one_hot)

                # 4. update Weights accordingly so as to optimize in next iteration
                self.update_weights(x)


    def predict(self, X):
       y_prediction = np.array([np.argmax(self.feed_forward(x) for x in X)], dtype=np.int)
       return y_prediction


    def feed_forward(self, x):
        # Iterate in Layers
        for layer in self.network:
            output = []

            for node in layer:
                # perform summation on every perceptron
                sum = self.summation(inputs=x, weights=node["weights"])
                node["output"] = self.sigmoid(sum=sum)
                output.append(node["output"])

            # lets make the output of current layer as input for the next layer
            x = output

        # the final output of the model shall be returned back here
        return x

    def feed_backward(self, y_one_hot):

        num_of_layers = len(self.network)

        # Iterate Backward
        for i in reversed(range(num_of_layers)):
            # Last Layer Case is basically the computation of error in very firstly
            if i == num_of_layers-1:
                for j, node in enumerate(self.network[i]):
                                # computed - actual
                    error = node["output"] - y_one_hot[j]
                    node["delta"] = error * self.sigmoid_derivation(node["output"])
            # Other Layers
            else:
                for j, node in enumerate(self.network[i]):
                    # error = node["output"] - y_one_hot[j]
                    error = sum([n["weights"][j] * n["delta"] for n in self.network[i+1]])
                    node["delta"] = error * self.sigmoid_derivation(node["output"])

    def update_weights(self, x):

        # Step to update the weights
        learning_rate = 0.5

        for i, layer in enumerate(self.network):
            # for 1st layer input values are x
            if i == 0:
                inputs = x
            # inputs of current layer becomes outputs of previous layers
            else:
                inputs = [node["output"] for node in self.network[i-1]]

            # Update Weights
            for node in layer:
                for j, input in enumerate(inputs):
                    # updated_weight = -learning_rate * (error * activation_function) * input
                    node["weights"][j] += -learning_rate * node["delta"] * input

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

    def one_hot_encoding(self, index, output):
        x = np.zeros(output, dtype=np.int)
        x[index] = 1
        return x


    def print_ann_model(self):
        print("ANN MODEL")
        print("LAYERS:", len(self.network))

        for i in range(len(self.network)):
            print("LAYER", i)
            for node in self.network[i]:
                print(node)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")


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

    # Create the ANN Model
    # input layer will have 7 nodes/perceptrons
    # output layer will have 3 nodes/perceptrons
    # hidden layer will have 5 nodes/perceptrons -> knob i.e. we can increase decrease nodes/perceptrons and test for accuracy
    # hidden_layer = [5] -> 1 hidden layer with 5 nodes/perceptrons
    # hidden_layer = [5, 4, 6] -> 3 hidden layers with 1st having 5 nodes/perceptrons, 2nd having 4 nodes/perceptrons, 3rd having 6 nodes/perceptrons

    model = ANN(input_layer=input_features, hidden_layer=[5], output_layer=num_of_classes)
    model.print_ann_model()

    accuracy_training_scores = []
    accuracy_testing_scores = []

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

        # Training the Model in 4 folds :)
        model.fit(X=X_train, Y=Y_train, epochs=25)

        y_prediction_train = model.predict(X_train)
        y_prediction_test = model.predict(X_test)

        print("y_prediction_train:", y_prediction_train)
        print("y_prediction_test:", y_prediction_test)

        accuracy_score_training = 100 * np.sum(Y_train == y_prediction_train) / len(Y_train)
        accuracy_score_testing = 100 * np.sum(Y_test == y_prediction_test) / len(Y_test)

        print("************************")
        print("MODEL TRAINING ACCURACY SCORE FOR FOLD", i, accuracy_score_training)
        print("MODEL TESTING ACCURACY SCORE FOR FOLD", i, accuracy_score_testing)
        print("************************")

        # Have scores added in the list for 4 different folds
        accuracy_training_scores.append(accuracy_score_training)
        accuracy_testing_scores.append(accuracy_score_testing)


    print()

    print("************************")
    print("OVERALL MODEL ACCURACY FOR 4 FOLDS")
    print("MODEL TRAINING ACCURACY SCORE FOR FOLD", sum(accuracy_training_scores)/len(accuracy_training_scores))
    print("MODEL TESTING ACCURACY SCORE FOR FOLD", sum(accuracy_testing_scores)/len(accuracy_testing_scores))
    print("************************")

if __name__ == '__main__':
    main()

