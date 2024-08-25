count = 0
countLast = 0

state = int(input("Input here ---> "))
while countLast <= state:
    num = 1
    while num <= countLast:
        print(num,end="")
        num+=1
    print()
    countLast+=1