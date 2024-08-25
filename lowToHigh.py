temp1 = []
i = 0

while True:
    inputNum = int(input("Please input your number ---> "))
    if inputNum == -1:
        break
    if(i == 0):
        temp1.append(inputNum)
        i+=1
    else:
        if(inputNum >= temp1[i-1]):
            temp1.append(inputNum)
            i+=1
    # temp1.append(inputNum)
    
print(temp1)
# 
# print(temp1)
# count2 = 0
# #1< 4
# while count2 < i:
#     if(count2 != 0):
#         # count2 = 1
#         if(temp1[count2] >= temp1[count2-1]):
#             temp2.append(temp1[count2])
#     elif(count2 ==0):    
#         temp2.append(temp1[count2])
#     count2+=1
# print(temp2)