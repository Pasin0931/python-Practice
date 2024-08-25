sum = 0
temp1 = []
countSum = 0
count = 0
input1 = 0
while(True):
    input1 = int(input("Please input your letter and type quit to leave: "))
    if(input1 == -1):
        break
    temp1.append(input1)
    sum = temp1[count] + sum
    countSum+=1
    count+=1
sum = sum / countSum
print(temp1)
print(sum)