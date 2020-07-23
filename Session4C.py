# ZOMATO -> flat 40%0ff | amount >= 300
#           upto 200

amount = int(input("Enter Amount Value: "))

"""
# Regular if/else
if amount >= 500:
    print("You are eligible to Apply Promo Code")
    print("Apply ZOMATO to get 40% Off")
else:
    print("You are not Eligible to Apply Promo Code")
"""

"""
# Nested if/else
if amount >= 300:
    print("You are eligible to Apply Promo Code")
    print("Apply ZOMATO to get 40% Off")
    promo_code = input("Enter Promo Code")
    if promo_code == "ZOMATO":
        print("ZOMATO Applied")

        discount = 0.40*amount

        if discount > 200:
            discount = 200

        print("Discount For You:", discount)
        amount -= discount

    else:
        print("Invalid Promo Code")
else:
    print("You are not Eligible to Apply Promo Code")

print("Please Pay: \u20b9", amount)
"""
# Assignment: In above program, reduce the number of lines :)
#             Hint, and or operations :)


# ZOMATO -> flat 40%0ff | amount >= 200
#           upto 100

# JUMBO ->  flat 50%0ff | amount >= 500
#           upto 200

# BINGO -> flat 20% 0ff | amount >= 100

#if/else
if amount >=100:
    promo_code = input("Enter Promo Code")

    # Nested ladder of/else
    if promo_code == "ZOMATO":

        discount = 0.40 * amount
        if discount >= 100:
            discount = 100

        print("ZOAMTO Promo Code Discount:", discount)
        amount -= discount

    elif promo_code == "JUMBO":

        discount = 0.50 * amount
        if discount >= 200:
            discount = 200

        print("JUMBO Promo Code Discount:", discount)
        amount -= discount

    elif promo_code == "BINGO":

        discount = 0.20 * amount
        print("BINGO Promo Code Discount:", discount)
        amount -= discount


    else:
        print("Invalid Promo Code")
else:
    print("Not Eligible for Promo Code")

print("Please Pay: \u20b9", amount)

# Assignment: Fix the code to work for correct amounts
#             suggest the user which promo code can give him more discounts in case user has applied promo code for less discounts
#             if user enters promo code which is invalid, suggest home all the promo codes with discount values as per his amount :)
