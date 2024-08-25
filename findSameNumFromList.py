temp1 = []
temp2 = []
count1 = 0
count2 = 0
countExtra = 0

while True:
    inputNum = int(input("Please input your number ---> "))
    if inputNum == -1:
        break
    if inputNum > 100:
        print("Out of range!!")
    else:
        temp1.append(inputNum)
        count1+=1
while count2 != len(temp1):
    if temp1[count2] in temp2:
        countExtra+=1
        count2+=1
    else:
        temp2.append(temp1[count2])
        count2+=1
print("Same num ---> ", countExtra)



    # if len(temp1) == 2:
    #     while count1 != count2:
    #         if temp1[count1] == temp1[countToLast]:
    #             temp2.append(temp1[count1])
    #             break
    #         else:
    #             count1+=1
    #             count2+=1
    #             countToLast+=1
    # else:
    #     print()