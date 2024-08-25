input1 = int(input("Please input your number: "))
count = 1
value1 = input1
while(count <= 12):
    print(value1,"x",count,"=",end=" ")
    input1 = value1 * count
    print(input1)
    count+=1