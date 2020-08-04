# Recursion : Function Executing itself again and again :)
#             We need it majorly to solve problem with Dynamic Programming
def get_max_num(data, length):

    if length == 1:     # in case data has 1 element only
        return data[0]  # return the same :)
    else:
        num = get_max_num(data, length-1)

    if num > data[length-1]:
        return num
    else:
        return data[length-1]



def main():
   # data = [10, 20, 30]
   data = [10, 20, 90, 70, 30, 60]
   max_num = get_max_num(data, len(data))
   print("Max Number is:", max_num) # 90


"""
    types of recursion:
    
    1. Direct Recursion
    # same function executes itself again and agian
    def f1():
        f1()
        
    2. Indirect Recursion
    # one function executes other and other executes this one
    def f2():
        f3()
        
    def f3():
        f2() 
        
        
    3. Tail Recursion
    # last statement is execution of function   
    def f4():
        .
        ..
        ...
        .
        ..
        f4()            

"""

# data = [10, 20, 90, 70, 30, 60]
# Draw Function Execution Stack for above data :)

# Assignment:
# Print binary representation of a number with recursion :)
# 12 -> 1 1 0 0
# 9  -> 1 0 0 1
# Draw Function Execution Stack as well

if __name__ == '__main__':
    main()