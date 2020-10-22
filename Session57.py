"""
    A XOR B
    as ANN

    ANN is combination of
    Input Layer
    Hidden Layer
    Output Layer

"""
import numpy as np

class Perceptron:

    def __init__(self, type):
        self.type = type # 1-> AND, 2-> OR, 3-> NOT

        if self.type == 1:
            self.perceptron = "AND PERCEPTRON"
            self.weights = np.array([0.6, 0.6])
            self.theta = 1

        elif self.type == 2:
            self.perceptron = "OR PERCEPTRON"
            self.weights = np.array([1.1, 1.1])
            self.theta = 1

        elif self.type == 3:
            self.perceptron = "NOT PERCEPTRON"
            self.weights = -1
            self.theta = -0.5
        else:
            print("INVALID TYPE :(")

        print(self.perceptron)

    def summation_function(self):
        if self.type is not 3:
            self.sum = np.dot(self.input, self.weights)
        else:
            self.sum = self.input * self.weights

    def activation_function(self):
        if self.sum > self.theta:
            return 1
        else:
            return 0

    def execute(self, inputs):
        outputs = []

        for input in inputs:
            self.input = input
            self.summation_function()
            outputs.append(self.activation_function())

        return outputs

class ANN:

    def __init__(self, input_layer=[], hidden_layer=[], output_layer=[]):
        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer

    def fit(self, inputs):
        outputs1 = self.input_layer[0].execute(inputs=inputs)
        outputs2 = self.input_layer[1].execute(inputs=inputs)

        # print(outputs1)
        # print(outputs2)

        outputs3 = self.hidden_layer[0].execute(inputs=outputs2)

        # print(outputs3)

        final_inputs = []
        for i in range(len(outputs1)):
            final_inputs.append(np.array([outputs1[i], outputs3[i]]))

        final_outputs = self.output_layer[0].execute(inputs=final_inputs)

        # print(final_outputs)
        return final_outputs



def main():
                    #  A  B
    input1 = np.array([0, 0])
    input2 = np.array([0, 1])
    input3 = np.array([1, 0])
    input4 = np.array([1, 1])

    ann = ANN(
        input_layer=[Perceptron(type=2), Perceptron(type=1)],
        hidden_layer=[Perceptron(type=3)],
        output_layer=[Perceptron(type=1)]
    )

    outputs = ann.fit(inputs=[input1, input2, input3, input4])
    print(outputs)


if __name__ == '__main__':
    main()