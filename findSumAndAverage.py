number = []
count1 = 0
sum = 0

while True:
    inputa = int(input("Please input your number ---> "))
    if(inputa == -1):
        break
    else:
        number.append(inputa)
while count1 != len(number):
    sum = sum + number[count1]
    count1+=1
print("Sum ---> ",sum)
print("Average ---> ", sum // count1)