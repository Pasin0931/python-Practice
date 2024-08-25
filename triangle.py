l1 = int(input("Please input your first triangle length: "))
l2 = int(input("Please input your second triangle length: "))
l3 = int(input("Please input your third triangle length: "))


if(l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2 or l1 <= 0 or l2 <= 0 or l3 <= 0):
    print("Invalid Triangle")
elif(l1 == l2 == l3):
    print("Equilateral Triangle")
elif(l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1):
    print("Isosceles Triangle")
elif(l1 != l2 != l3):
    print("Scalene Triangle")