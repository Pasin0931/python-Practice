count = 0
countSP = 1
countFL = 1

inputNum = int(input("Please input the number of pyramid row: "))
while count != inputNum:
    print("|",end="")
    print((int(inputNum) - countSP) * " ",end="")
    print("*" * countFL,end="")
    print((int(inputNum) - countSP) * " ",end="")
    print("|")
    countSP+=1
    countFL+=2
    count+=1