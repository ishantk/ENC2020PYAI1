# List of Lists
# RGB Color Reference https://www.w3schools.com/colors/colors_rgb.asp
pixel1 = [120, 0, 190]
pixel2 = [235, 12, 230]
pixel3 = [197, 50, 0]
pixel4 = [190, 99, 111]
pixel5 = [175, 150, 213]
pixel6 = [35, 110, 109]
pixel7 = [99, 121, 88]
pixel8 = [120, 200, 220]
pixel9 = [210, 110, 90]

# List of List of Lists :) -> 3-D Data Structure
image = [
    # 0         1       2
    [pixel1, pixel2, pixel3],   # 0
    [pixel4, pixel5, pixel6],   # 1
    [pixel7, pixel8, pixel9]    # 2
]

print(len(image))       # 1. 3
print(len(image[0]))    # 2. 3
print(len(image[0][0])) # 3. 3
print(image[0][1])      # 4. [235, 12, 230]


print("IMAGE")
for pixels in image:
    for pixel in pixels:
        print(pixel, end="\t")
    print()


"""
    Assignment:
    
    Image:
    p1  p2  p3
    p4  p5  p6
    p7  p8  p9
    
    # Take this input from User
    1. Rotate the Image 90 degrees clockwise
    
    Resultant Image:
    p7  p4  p1
    p8  p5  p2
    p9  p6  p3
    
    2. Rotate the Image 90 degrees anti-clockwise
    3. Rotate the Image 180 degrees clockwise
    4. Rotate the Image 180 degrees anti-clockwise
    5. GrayScale the Image
        pixel -> [120, 50, 90] -> 120 + 50 + 90 // 3 => 260//3 -> 86
        pixel -> [86, 86, 86]

"""