"""
    Perceptron as Logical AND
    Perceptron as Logical OR

"""
import numpy as np

class Perceptron:

    def __init__(self):
        print("Perceptron Created")

        # Assuming Weights for AND Operation (Hit & Trial)
        # self.weights = np.array([0.6, 0.6])

        # Assuming Weights for OR Operation (Hit & Trial)
        self.weights = np.array([1.1, 1.1])

        # Assuming Threshold for Activation Function
        self.theta = 1

    def pass_input(self, input):
        self.input = input

    def summation_function(self):
        self.sum = np.dot(self.input, self.weights)

    # def activation_function(self):
    #     if self.sum >= self.theta:
    #         return 1
    #     else:
    #         return 0

    # def execute(self):
    #     self.summation_function()
    #     return self.activation_function()

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


    perceptron.pass_input(input1)
    # print("For Input: {} Result is: {}".format(input1, perceptron.execute()))
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