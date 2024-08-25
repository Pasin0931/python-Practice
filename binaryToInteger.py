a = 1101
total = 0
count = 1
sum = 0
while a != 0:
    print(a % 10)
    tmp = a % 10
    total = tmp * (count)
    count = count * 2
    print("OOOO",total)
    sum = total + sum
    a = a // 10
print("total: ",sum)