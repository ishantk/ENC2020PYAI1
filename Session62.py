from Session62A import DataSetHelper
from Session62B import ANN



def main():
    file_name = "seeds.csv"
    helper = DataSetHelper()
    X, Y, num_of_classes = helper.preapre_data_set(file=file_name, target="y", normalize=True)

    print("INPUT X")
    print(X)

    print()

    print("OUTPUT Y")
    print(Y)

    print()

    print("NUM OF CLASSES")
    print(num_of_classes)

    ann = ANN()
    # ann.fit()
    # ann.predict()

if __name__ == '__main__':
    main()