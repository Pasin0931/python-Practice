# inputNum = int(input("Input your number: "))
# countNum = inputNum
# print(inputNum,end="! = ")
# print(inputNum,end=" x ")
# while(inputNum >= 3):
#     inputNum = inputNum - 1
#     countNum = inputNum * countNum
#     print(inputNum,end=" x ")
# print("1 = ",end="")
# print(countNum)

inputNum = int(input("Input your number: "))
countNum = 1
print(inputNum,end="! = ")
while(inputNum >= 1):
    countNum = countNum * inputNum
    if(inputNum == 1):
        print(inputNum,end=" = ")
    else:
        print(inputNum,end=" x ")
    inputNum = inputNum - 1
if(inputNum < 0):
    print("invalid input")
else:
    print(countNum)