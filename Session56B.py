"""
    Perceptron as Logical AND
    Perceptron as Logical OR

"""
import numpy as np

class Perceptron:

    def __init__(self):
        print("Perceptron Created")

        # Assuming Weights
        self.weights = np.array([1, 1])

        # Assuming Threshold for Activation Function
        self.theta = 0

        # Assuming a Bias
        # self.bias = -0.5      # Logical OR :)
        self.bias = -1.5        # Logical AND :)

    def pass_input(self, input):
        self.input = input

    def summation_function(self):
        # (Summation has an external bias also)
        self.sum = np.dot(self.input, self.weights) + self.bias

    def activation_function(self):
        if self.sum > self.theta:
            print("For Input: {} Result is: {}".format(self.input, 1))
        else:
            print("For Input: {} Result is: {}".format(self.input, 0))

    def execute(self):
        print("Working on Input", self.input)
        self.summation_function()
        self.activation_function()


def main():

    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    perceptron = Perceptron()

    print()

    perceptron.pass_input(input1)
    perceptron.execute()

    print()

    perceptron.pass_input(input2)
    perceptron.execute()

    print()

    perceptron.pass_input(input3)
    perceptron.execute()

    print()

    perceptron.pass_input(input4)
    perceptron.execute()


if __name__ == '__main__':
    main()