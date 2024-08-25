highest = 0
lowest = 0
count = 0
countScore = 0
sum = 0
temp = []

abov = 0
belo = 0

while True:
    inputa = int(input("Input a score ---> "))
    if inputa == -1:
        break
    sum = sum + inputa
    temp.append(inputa)
    lowest = temp[0]
    highest = temp[0]
    if temp[count] > highest:
        highest = temp[count]
    if temp[count] < lowest:
        lowest = temp[count]
    count+=1

average = sum / count

# while count != len(temp):
#     average = temp[count] + average
print("\n\n\n")
print("Highest score ---> ", highest)
print("Lowest score ---> ", lowest)
print("Average score ---> ", average)
print("Number of scores ---> ", count)

count*=0

while count != len(temp):
    if temp[count] > average:
        abov+=1
    elif temp[count] < average:
        belo+=1
    count+=1

print("Number of score above average ---> ", abov)
print("Number of score below average ---> ", belo)