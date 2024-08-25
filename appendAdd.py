# inputN = int(input("Please input your number: "))
# temp1 = []
# temp2 = []
# count = 0
# sumAll = 0
# num = 1
# while(count < inputN):
#     temp1.append(int(input("Number: ")))
#     count+=1
# print(temp1)
# count = 0
# while(count < inputN):
#     if(temp1[count] % 2 == 0):
#         temp2.append(temp1[count] * 3)
#         count+=1
#     else:
#         temp2.append(temp1[count] * 2)
#         count+=1
# print(temp2)
# count = 0
# while(count < inputN):
#     sumAll = temp2[count] + sumAll
#     count+=1
# print("sum =",sumAll)

inputN = int(input("Please input yor number: "))
temp1 = []
temp2 = []
count = 0
sum = 0
while(count < inputN):
    # append temp1
    temp1.append(int(input("Number: ")))
    if(temp1[count] % 2 == 0):
        # append temp2
        temp2.append(temp1[count] * 3)
        sum = sum + temp2[count]
    else:
        # append temp2
        temp2.append(temp1[count] * 2)
        sum = sum + temp2[count]
    count+=1
print(temp1)
print(temp2)
print(sum)