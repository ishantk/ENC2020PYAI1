"""
    XOR

    A   B   Y
    0   0   0
    0   1   1
    1   0   1
    1   1   0

    Every Logical operation is done with the help of 3 gates
    AND OR and NOT :)

    A XOR B
    (A OR B) AND (NOT (A AND B))

    0 XOR 0
    -------
    (0 OR 0) AND (NOT (0 AND 0))
    0   AND (NOT (0) )
    0 AND 1
    0

    0 XOR 1
    -------
    (0 OR 1) AND (NOT (0 AND 1))
    1   AND (NOT(0))
    1 AND 1
    1

    1 XOR 0
    -------
    (1 OR 0) AND (NOT (1 AND 0))
    1   AND (NOT(0))
    1 AND 1
    1

    1 XOR 1
    -------
    (1 OR 1) AND (NOT (1 AND 1))
    1   AND (NOT(1))
    1 AND 0
    0


"""

import numpy as np

class ANDPerceptron:

    def __init__(self):
        print("AND Perceptron Created")

        # Assuming Weights for AND Operation (Hit & Trial)
        self.weights = np.array([0.6, 0.6])

        # Assuming Threshold for Activation Function
        self.theta = 1


    def summation_function(self):
        self.sum = np.dot(self.input, self.weights)


    def activation_function(self):
        if self.sum > self.theta:
            return 1
        else:
            return 0

    def execute(self, input):
        self.input = input
        print("Working on Input", self.input)
        self.summation_function()
        return self.activation_function()


class ORPerceptron:

    def __init__(self):
        print("OR Perceptron Created")

        # Assuming Weights for OR Operation (Hit & Trial)
        self.weights = np.array([1.1, 1.1])

        # Assuming Threshold for Activation Function
        self.theta = 1

    def summation_function(self):
        self.sum = np.dot(self.input, self.weights)


    def activation_function(self):
        if self.sum > self.theta:
            return 1
        else:
            return 0

    def execute(self, input):
        self.input = input
        print("Working on Input", self.input)
        self.summation_function()
        return self.activation_function()


class NOTPerceptron:

    def __init__(self):
        print("NOT Perceptron Created")

        # Assuming Weights for NOT Operation (Hit & Trial)
        self.weight = -1

        # Assuming Threshold for Activation Function
        self.theta = -0.5

    def summation_function(self):
        self.sum = self.input * self.weight

    def activation_function(self):
        if self.sum > self.theta:
            return 1
        else:
            return 0

    def execute(self, input):
        self.input = input
        print("Working on Input", self.input)
        self.summation_function()
        return self.activation_function()


def main():
                    #  A  B
    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    #  A XOR B
    #  (A OR B) AND (NOT (A AND B))

    and_perceptron = ANDPerceptron()
    or_perceptron = ORPerceptron()
    not_perceptron = NOTPerceptron()

    print()
    print("A OR B")

    # A OR B
    output_or1 = or_perceptron.execute(input=input1)
    output_or2 = or_perceptron.execute(input=input2)
    output_or3 = or_perceptron.execute(input=input3)
    output_or4 = or_perceptron.execute(input=input4)

    print(output_or1, output_or2, output_or3, output_or4)

    print()
    print("A AND B")

    # A AND B
    output_and1 = and_perceptron.execute(input=input1)
    output_and2 = and_perceptron.execute(input=input2)
    output_and3 = and_perceptron.execute(input=input3)
    output_and4 = and_perceptron.execute(input=input4)

    print(output_and1, output_and2, output_and3, output_and4)

    print()
    print("NOT (A AND B)")

    # NOT (A AND B)
    output_not1 = not_perceptron.execute(input=output_and1)
    output_not2 = not_perceptron.execute(input=output_and2)
    output_not3 = not_perceptron.execute(input=output_and3)
    output_not4 = not_perceptron.execute(input=output_and4)

    print(output_not1, output_not2, output_not3, output_not4)

    print()
    print("(A OR B) AND (NOT (A AND B))")

    final_output1 = and_perceptron.execute(input=np.array([output_or1, output_not1]))
    final_output2 = and_perceptron.execute(input=np.array([output_or2, output_not2]))
    final_output3 = and_perceptron.execute(input=np.array([output_or3, output_not3]))
    final_output4 = and_perceptron.execute(input=np.array([output_or4, output_not4]))

    print(final_output1, final_output2, final_output3, final_output4)

if __name__ == '__main__':
    main()