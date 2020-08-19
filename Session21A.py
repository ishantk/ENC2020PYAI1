"""
    Exception Handling
    Python is Interpreted i.e. whenever we run our program line by line code is executed
    So, we dont have anything as Compile Time Error
    Any Error which will occur is known as Runtime Error -> EXCEPTIONS

    Unfortunately, App Stopped Working
    Our App had a run time error and OS Closed it forcefully

"""

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('Welcome to Cashback Rewards')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

cashbacks = [100, 120, 50, 90, 70, 200, 230, 110, 40, 10]

lucky_number = int(input("Enter your Lucky Number: "))
try:
    print("Thank You For Your Participation. You Won a CashBack of \u20b9", cashbacks[lucky_number])

    additional_cashback = cashbacks[lucky_number]//lucky_number
    print("You have Won an Additional Cashback of \u20b9", additional_cashback)

# except Exception as error:
except: # without knowing the error :(
    print("Something Went Wrong")

# which will be executed at any cost i.e. in case crash occurs, before the crash finally gets executed and otherwise also wit will be executed
finally:
    print("This is Important")

"""
except IndexError as error:
    print("Something Went Wrong With Index:", error)

except ZeroDivisionError as error:
    print("Something Went Wrong With Division:", error)
"""

print("Hope You use your Cashback Soon")

# PS: whenever we get an error, program will not execute further. i.e. it will CRASH or we can say it stopped abnormally
#     whenever we get an error in the try block, control will directly jump into except block and hence statements below erroneous statement in try will not be executed

"""
    Exception Hierarchy in Python
    class Exception: # This is a built in class :)
        pass

    class IndexError(Exception):
        pass
        
    class ZeroDivisionError(Exception):
        pass   
        
    In Python, all the Exceptions are the children of Exception Class      

    Nested try except
    
    try:
        try:
            pass
        except:
            pass
        finally:
            pass
    except:
        try:
            pass
        except:
            pass
        finally:
            pass 
    finally:                     
        try:
            pass
        except:
            pass
        finally:
            pass 
"""