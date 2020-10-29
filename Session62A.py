"""
    ANN in Making
    Part-I

    Normalization and Standardization
    ANN Model Errors (Absolute and Squared Errors)
    BackPropagation Algorithm to fine tune weights for reducing the errors

"""


import pandas as pd
import numpy as np

class DataSetHelper:

    def __init__(self):
        print("Preparing DataSet for ANN...")


    def preapre_data_set(self, file, target, normalize=False):

        df = pd.read_csv(file)
        # print(df)


        target_indexes = {target: idx for idx, target in enumerate(sorted(list(set(df[target].values))))}
        # print(target_indexes)

        X = df.drop([target], axis=1).values
        # print(X)

        # print()
        Y = np.vectorize(lambda x : target_indexes[x])(df[target].values)
        # print(Y)


        # classes = target_indexes.keys()
        # print(classes)

        num_of_classes = len(target_indexes)

        if normalize:
            # Lets Standardize the data set
            X = (X - X.mean(axis=0)) / X.std(axis=0)

            # Normalization :) -> implement yourself

        return X, Y, num_of_classes


    # Reference Link: K-Folds cross-validator
    # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
    # to train test split the data set
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