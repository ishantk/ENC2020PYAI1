
def get_max_number(*numbers):

    max = numbers[0]

    for number in numbers:
        if number > max:
            max = number

    return max


def main():
    print(get_max_number(10, 20, 50, 70, 90, 30, 40))
    print(max(10, 20, 50, 70, 90, 30, 40))


if __name__ == '__main__':
    main()
