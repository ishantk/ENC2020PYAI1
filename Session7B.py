"""
    Value Vs Reference
    Reference -> Passing a Multi Value Container eg: list
"""

def square_of_numbers(numbers):
    print("numbers is:", numbers, hex(id(numbers)))

    for i in range(0, len(numbers)):
        numbers[i] = numbers[i]*numbers[i]          # we are modifying content inside the list and not the list itself

    print("numbers now is:", numbers, hex(id(numbers)))


def main():
    nums = [10, 20, 10, 40, 50]
    print("nums is:", nums, hex(id(nums)))
    print("nums[0] is:", nums[0], hex(id(nums[0])))
    square_of_numbers(nums)
    print("nums now is:", nums, hex(id(nums)))      # content in nums will also be modified here


# we must execute main, if we have created it
if __name__ == '__main__':
    main()