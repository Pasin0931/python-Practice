import math
while(True):
    print("1. Circumference")
    print("2. Area")
    print("3. Logout")
    input_num = int(input("Choose your option ---> "))
    if(input_num == 1):
        radius = int(input("Please input your radius: "))
        circumference = math.pi * 2 * radius
        print("Your circle circumference is ",circumference)
        print("")
    elif(input_num == 2):
        radius = int(input("Please input your radius: "))
        area = math.pi * radius * radius
        print("Your circle area is ",area)
        print("")
    elif(input_num == 3):
        print("Logout successfully")
        break
    else:
        print("Your option doesn't exist, please try again")
        print("")