tmp = []
count = 0
countPlus = 0
while True:
    inputABC = int(input("Please input your number ---> "))
    if inputABC != 0:
        if inputABC in tmp:
            countPlus+=1
        tmp.append(inputABC)
        count+=1
    else:
        break
print(countPlus)