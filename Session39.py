"""
    Predictive Analysis
    Regression: Predicting the continuous value
    Linear Regression

    DataSet
    X =[1, 2, 3, 4, 5]
    Y =[2, 4, 5, 4, 5]

    Linear Regression Line Equation
    Y = b0 + b1X
    b0 -> Interceptor
    b1 -> Slope of Line

    Objective: We need to find b0 and b1 from the given data so as to predict

    STEP 1:
    -------
    MEAN OF X (MX) = (1 + 2 + 3 + 4 + 5)/5 -> 3
    MEAN OF Y (MY) = 4

    -------------------------------------------------
    X   Y   X-MX    Y-MY    sq(X-MX)    (X-MX)(Y-MY)
    -------------------------------------------------
    1   2   -2      -2      4           4
    2   4   -1       0      1           0
    3   5    0       1      0           0
    4   4    1       0      1           0
    5   5    2       1      4           2

    STEP 2:
    -------
    SUM OF sq(X-MX) =       10
    SUM OF (X-MX)(Y-MY) =               6

    Slope of Line: [SUM OF (X-MX)(Y-MY)] / [SUM OF sq(X-MX)]
    b1 = 6/10 -> 0.6

    STEP 3:
    -------
    Y = b0 + b1X

    For b0 lets put mean values of X and Y in Equation
    4 = b0 + 0.6 * 3
    b0 = 4 - 1.8
    b0 = 2.2

    Equation of Line:
    Y = 2.2 + 0.6X

    Given any value of X which is Unseen, we can predict the value Y using above equation :)

    STEP 4:
    -------

    We have found the equation of line, but we are not sure for errors
    Hence, lets evaluate errors

    Different Metrics
    1. Mean Squared Error | MSE
    2. R2
    3. Variance

    In the equation of line put the original value of X i.e [1, 2, 3, 4, 5]
    and give Y

    Y = 2.2 + 0.6X

    MEAN OF X (MX) = 3
    MEAN OF Y (MY) = 4

    -------------------------------------------------
    X   Y   Y'   Y-MY    sq(Y-MY)    Y'-MY   sq(Y'-MY)
    -------------------------------------------------
    1   2  2.8   -2      4           -1.2      1.44
    2   4  3.4    0      0           -0.6      0.36
    3   5  4      1      1           0          0
    4   4  4.6    0      0           0.6       0.36
    5   5  5.2    1      1           1.2       1.44
                        ---                   -----
                         6                     3.6

    MSE -> [SUM of sq(Y'-MY)] / [SUM of sq(Y-MY)]
    MSE -> 3.6/6
    MSE -> 0.6

    MSE is 0 -> it means perfect fit of data :)
    But, it may not happen ever
    IDEAL MSE RANGE [0 to 1]

"""

import numpy as np

class LinearRegressionModel:

    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.mse = 0
        self.can_predict = False

    def fit(self, X, Y):
        self.X = X
        self.Y = Y

        # Slope of Line: [SUM OF (X-MX)(Y-MY)] / [SUM OF sq(X-MX)]
        self.b1 = np.sum((self.X - np.mean(self.X)) * (self.Y - np.mean(self.Y))) / np.sum(np.square(self.X - np.mean(self.X)))


        # Interceptor of Line: MY = b0 + b1 MX
        # b0 = MY - b1 MX
        self.b0 = np.mean(self.Y) - (self.b1 * np.mean(self.X))


        print("b0 is:", self.b0)
        print("b1 is:", self.b1)
        print("Equation of Line: Y = {} + {} X".format(self.b0, self.b1))

        # MSE -> [SUM of sq(Y'-MY)] / [SUM of sq(Y-MY)]
        self.mse = np.sum(np.square(self.predict_Y_dash(self.X) - np.mean(self.Y))) / np.sum(np.square(self.Y - np.mean(self.Y)))
        print("MSE is:", self.mse)

        if self.mse >=0 and self.mse <=1:
            self.can_predict = True

        # Return the Tuple of results
        return (self.b0, self.b1, self.mse, self.can_predict)


    def predict_Y_dash(self, X):
        # put original X in Equation of Line :)
        y_dash = self.b0 + np.multiply(self.b1, X)
        return y_dash

    def predict(self, X):
        if self.can_predict:
            Y = self.b0 + np.multiply(self.b1, X)
            return Y
        else:
            return -1 # for no prediction case :(

def main():

    # 1. Create the Data Set
    X = [1, 2, 3, 4, 5]     # Independent Input Variable
    Y = [2, 4, 5, 4, 5]     # Dependent Output Variable

    # 2. Create the Model
    model = LinearRegressionModel()

    # 3. Train the Model
    result = model.fit(X, Y)
    print(result)

    # 4. Predict from the Model
    predicted_y = model.predict(6)
    print("For input 6 predicted value is:", predicted_y)

if __name__ == '__main__':
    main()

# draw a Graph with data points and regression line and share in whatsapp group :)