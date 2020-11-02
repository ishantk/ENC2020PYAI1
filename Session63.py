"""
    Coding ANN
    Part-II

    Understanding KFold
    Coding Parts of ANN
"""

"""
    KFold Validation
    
    Consider the data set with several observation/records (100)
    eg:
    X1  X2  Y   
    1   2   1
    
    
    We divide the observations in n parts
    fold = 4
    
    fold1   25 observations
    fold2   25 observations
    fold3   25 observations
    fold4   25 observations
    
    Train the model with all of these 4 folds
    as we will use all of the data and for better accuracy as compared to other approaches
    
    100
    70:30
    70 for training and 30 for testing
    
    Approach
    we will be using all the records and dividing them further for testing and training
    
    X1  X2  Y   
0   1   2   1
1   3   4   2
2   1   2   3
3   3   4   4

    We have to divide the dataset in n-folds based on indexes :)

"""

import numpy as np
from sklearn.model_selection import KFold

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]]) # Input Features
Y = np.array([1, 2, 3, 4])

kFold = KFold(n_splits=2)
print("Splits for my DataSet:", kFold.get_n_splits())

# print(kFold.split(X, Y)) -> we will get generator object to iterate

for train_index, test_index in kFold.split(X, Y):
    print("===INDEXES====")
    print(train_index, test_index)
    print("==============")

    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    print("*****FOLD*****")
    print("X_train", X_train, "| X_test", X_test)
    print("Y_train", Y_train, "| Y_test", Y_test)
    print("**************")

    print()