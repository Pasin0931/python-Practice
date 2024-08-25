# temp = []
# sum = 0
# count = 0
# while True:
#     inputNum = int(input("Enter a number (0 to end): "))
#     if inputNum == 0:
#         break
#     temp.append(inputNum)
#     sum = sum + temp[count]
#     count+=1
# print("List of all numbers --->",temp)
# print("Sum: ",sum)

# --------------------------------------------------------

temp = []
sum = 0
count1 = 0
count2 = 0
while True:
    inputNum = int(input("Enter a number (0 to end): "))
    if inputNum == 0:
        break
    temp.append(inputNum)
    count1+=1
print("List of all numbers --->",temp)
print("Calculating sum...")
while count2 != count1:
    sum = temp[count2] + sum
    print(sum)
    count2+=1