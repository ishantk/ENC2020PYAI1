"""
    Perceptron as Logical NOT

"""

class Perceptron:

    def __init__(self):
        print("Perceptron Created")

        # Assuming Weights for NOT Operation (Hit & Trial)
        self.weight = -1

        # Assuming Threshold for Activation Function
        self.theta = -0.5

    def pass_input(self, input):
        self.input = input

    def summation_function(self):
        self.sum = self.input * self.weight

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

    input1 = 0
    input2 = 1

    perceptron = Perceptron()
    print()

    perceptron.pass_input(input1)
    perceptron.execute()

    print()

    perceptron.pass_input(input2)
    perceptron.execute()



if __name__ == '__main__':
    main()