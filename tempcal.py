temp = []
sum = 0
countNum = 0
countEnd = 0

while True:
    inputa = float(input("Enter your temperature ---> "))
    if inputa == -1:
        break
    sum = sum + inputa
    temp.append(inputa)
    countNum+=1

maxTemp = temp[0]
minTemp = temp[0]

while countEnd != countNum:
    if temp[countEnd] > maxTemp:
        maxTemp = temp[countEnd]
    if temp[countEnd] < minTemp:
        minTemp = temp[countEnd]
    countEnd+=1

print(" ")
print(" ")
    
print("Maximum temperature ---> ",maxTemp)
print("Minimal temperature ---> ",minTemp)
print("Sum ---> ", sum)
print("Number of reading ---> ", countNum)