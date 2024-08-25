# a = [1,2,3,4]
# i = 0
# sumI = 0
# while (i < len(a)):
#     print(a[i])
#     i += 1
#     sumI = i + sumI
# print(sumI)

number = [1,2,3,4]
n = 0
sumN = 0
while(n < 4):
    if(number[n] % 2 == 0):
        sumN = (number[n] * 3) + sumN
        n+=1
    else:
        sumN = (number[n] * 2) + sumN
        n+=1
print(sumN)