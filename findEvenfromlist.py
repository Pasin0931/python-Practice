temp = [10, 2, 5, 2, 5, 3, 7, 8, 11]
temp2 = []
count = 0
countEven = 0

while count != len(temp):
    if temp[count] % 2 == 0:
        countEven+=1
        temp2.append(temp[count])
    count+=1

print("Even number ---> ", countEven)
print("Even number is ---> ", temp2)