count = 1
var = 0
sumVar = 0
inputN = int(input("Please input N: "))

while(count <= inputN):
    if(count % 2 == 0):
        var = count * 3
        sumVar = var + sumVar
        count+=1
    else:
        var = count * 2
        sumVar = var + sumVar
        count+=1
print(sumVar)

# count = 1
# sumVar = 0
# inputN = int(input("Please input N: "))
# while(count <= inputN):
#     # even number
#     if(count % 2 == 0):
#         sumVar = sumVar + (count * 3)
#     # odd number
#     elif(count % 2 == 1):
#         sumVar = sumVar + (count * 2)
#     count+=1
# print(sumVar)