"""
    Introduction to Deep Learning
    Writing Perceptron

    1. Inputs -> Input and Weight
    2. Summation  Function
    3. Activation Function

"""

class Perceptron:

    def __init__(self, inputs=None):
        self.inputs = inputs
        print("Perceptron Created")
        print("Inputs and Weights")
        print(inputs)
        print()

        self.summation_function()
        self.activation_function()


    def summation_function(self):
        print("Summation Function in Action")
        self.sum = 0

        for i in range(len(self.inputs)):
            self.sum += self.inputs[i][0]*self.inputs[i][1]

        print("Summation Function Output is:", self.sum)
        print()


    def activation_function(self):

        theta = 0.5

        print("Activation Function in Action with theta", theta)

        # binary step function
        if self.sum > theta:
            print("Output is 1")
            print("Decision is Taken and is as YES or TRUE")
        else:
            print("Output is 0")
            print("Decision is Not Taken and is as NO or FALSE")

def main():

    # inputs = [
    #     [input, weight]
    # ]

    inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1],
    ]

    # perceptron = Perceptron(inputs=inputs)
    # perceptron.summation_function()
    # perceptron.activation_function()

    Perceptron(inputs=inputs)

if __name__ == '__main__':
    main()