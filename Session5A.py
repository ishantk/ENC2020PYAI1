"""

    Sorting: Bubble Sort :)
    Input : 60, 12, 24, 18, 80 | Not Sorted
    Output: 12, 18, 24, 60, 80 | Sorted in Asc

    i:0
    0th : 60, 12, 24, 18, 80 | Consider all the elements [size 5]
    j:0 to 4

    0th Iteration
    0.0: [60, 12], 24, 18, 80 | Swap 60 and 12
         [12, 60], 24, 18, 80

    0.1: 12, [60, 24], 18, 80 | Swap 60 and 24
         12, [24, 60], 18, 80

    0.2: 12, 24, [60, 18], 80 | Swap 60 and 18
         12, 24, [18, 60], 80

    0.3: 12, 24, 18, [60, 80] | Swap Nothing

    0.4: 12, 24, 18, 60, [80] | 80 in the end cannot be compared to anyone else :)

    Here, the last element will become the largest number automatically
    As we are pushing the largest number in the end

    i:1 consider 1 less element [Size: 4]

    1.1  12, 24, 18, 60,
         .....

    1:2 3 elements
     so on and so forth :)

   Reference Visualization : https://visualgo.net/bn/sorting

"""

data = [60, 12, 24, 18, 80]
print("DATA BEFORE:")
print(data)

n = len(data) # 5

for i in range(0, n): # (0, 5)| i: 0, 1, 2, 3, 4
    # i: 0 | n: 5 | j: (0, 4) -> j: 0, 1, 2, 3
    # i: 1 | n: 5 | j: (0, 3) -> j: 0, 1, 2
    # i: 2 | n: 5 | j: (0, 2) -> j: 0, 1
    # i: 3 | n: 5 | j: (0, 1) -> j: 0
    # i: 4 | n: 5 | j: (0, 0) -> Not execute
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            # swap the elements
            data[j], data[j+1] = data[j+1], data[j]

print("DATA NOW:")
print(data)
