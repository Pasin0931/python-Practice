input1 = int(input("Please input your number: "))
input2 = 0
while(input1 > 0):
    input2 = (input1 % 10) + input2
    input1 = input1 // 10
print(input2)

# value1 = (input1 // 1) % 10
# value2 = (input1 // 10) % 10
# value3 = (input1 // 100) % 10
# value4 = (input1 // 1000) % 10

# print(value1)
# print(value2)
# print(value3)
# print(value4)