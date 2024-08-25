import math
radius1 = int(input("First circle radius: "))
radius2 = int(input("Second circle radius: "))
area1 = math.pi * radius1 * radius1
area2 = math.pi * radius2 * radius2
if(area1 > area2):
    print("First circle is bigger")
elif(area1 == area2):
    print("First and second radius is equally")
else:
    print("Second circle is bigger")