count1 = 0
count2 = 0
count3 = 0
temp1 = []
temp2 = []
# add input
while count1 < 5:
    inputNum = int(input("Please input your num ---> "))
    if(inputNum %2 ==0):
        temp1.append(inputNum)
    count1+=1
    print(temp1)
count1 = count1 * 0
print("Even number is ---> ", end="")
# check even number
# output
while count3 < len(temp1):
    if(count3 < len(temp1)-1):
        print(temp1[count3], end = ",")
    else:
        print(temp1[count3], end="")
    count3+=1