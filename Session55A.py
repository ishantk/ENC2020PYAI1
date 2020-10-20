"""
    Activation Functions
    1. Linear Transform
        f(x) = x
    2. Binary Step
        f(x) = 1 if x > theta
             = 0 if x < theta
    3. ReLU
        f(x) = x if x > 0
             = 0 if x < 0
    4. Sigmoid
    5. Tanh
    6. Softmax

"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(inputs):
    outputs = []

    for x in inputs:
        result = 1 / (1 + np.exp(-x))
        outputs.append(result)

    return outputs

def hyperbolic_tangent(inputs):
    outputs = np.tanh(inputs)
    return outputs

def softmax(inputs):
    outputs = np.exp(inputs) / sum(np.exp(inputs))
    return outputs


def main():
    inputs = list(range(0, 21))

    print("Sigmoid Inputs:", inputs)
    outputs = sigmoid(inputs)
    print("Sigmoid Outputs:", outputs)

    plt.plot(inputs, outputs)
    plt.xlabel("Inputs")
    plt.ylabel("Outputs")
    plt.show()


    print()

    print("Hyperbolic Tangent Inputs:", inputs)
    outputs = hyperbolic_tangent(inputs)
    print("Hyperbolic Tangent Outputs:", outputs)

    print()

    print("Softmax Inputs:", inputs)
    outputs = softmax(inputs)
    print("Softmax Outputs:", outputs)


if __name__ == '__main__':
    main()