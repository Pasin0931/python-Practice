import math
area = 0
while(True):
    radius = int(input("Please input your radius: "))
    area = math.pi * radius * radius
    if(area > 150):
        print("Circle area is above 150")
        print("Circle area is",area)
        break
    else:
        print("Circle area isn't above 150")