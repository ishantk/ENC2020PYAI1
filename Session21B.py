# User-Defined Exception
# We can create our own Exception classes, but in Python, any Exception class must be Child of Exception
class WithdrawError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.min_balance = 2000
        self.attempts = 0

    def withdraw(self, amount):

        self.balance -= amount

        if self.balance <= self.min_balance:
            self.balance += amount
            print("Withdraw: [Failed]  | Balance is Low: \u20b9", self.balance)
            self.attempts += 1
        else:
            print("Withdraw: [Success] | New Balance is: \u20b9", self.balance)

        if self.attempts == 3:
            # We as developers can crash the program
            # error = IndexError("Illegal Attempts [{}]".format(self.attempts))

            error = WithdrawError("Illegal Attempts [{}]".format(self.attempts))
            raise error

def main():
    print("Banking Started")

    john = BankAccount()
    print(john.__dict__)

    try:
        # Consider, John is trying to perform transaction which is 5000 times
        # Challenge: John is trying to occupy Bank's Resources
        for i in range(5000):
            john.withdraw(3000)
    except Exception as error:
        print("Something Went Wrong", error)
        print("Please Try Again Later")

    print("Banking Finished")


if __name__ == '__main__':
    main()

# PS: Application must Terminate Normally and hence we should surround the code in try except WHENEVER we raise the Exception
