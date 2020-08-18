import random

otp = random.randrange(10000)
print("1. OTP is:", otp)

otp = random.randrange(200000, 400000)
print("2. OTP is:", otp)

otp = random.randrange(2000, 4000, 10)
print("3. OTP is:", otp)

# we cannot have step here
otp = random.randint(1000, 9000)
print("4. OTP is:", otp)

# Assignment: Create a function which generates random number
#             you must write your own algo
# def get_otp(from, to, step):
#     pass