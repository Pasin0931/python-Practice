count = 1
numba = 1
inputN = int(input("Please input your number: "))
while(count <= inputN):
    if(numba % 5 == 0):
        print("F")
        count+=1
        numba+=1
    else:
        print(count)
        count+=1
        numba+=1
        