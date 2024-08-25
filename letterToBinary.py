lastInput = []
count = 0
countPlus = 0
while True:
    inputTxT = str(input("Please input your words ---> "))
    if len(inputTxT) == 1:
        lastInput.append(inputTxT)
        count+=1
    elif inputTxT == "":
        break
    elif len(inputTxT) > 1:
        print("Error ---> You must input only 1 letter!")
while countPlus != count:
    print(lastInput[countPlus], end="")
    countPlus+=1
countPlus = countPlus * 0
print(" ")
bi_list = []
while countPlus != count:
    tmp = ord(lastInput[countPlus])
    bit = 1
    bi = 0
    while tmp > 0:
        # print(tmp % 2, end="")
        bi = ((tmp % 2) * bit) + bi
        bit = bit * 10
        tmp = tmp // 2
    countPlus+=1
    bi_list.append(bi)
print(bi_list)
print(lastInput)