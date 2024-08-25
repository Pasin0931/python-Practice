count1 = 1
l = 1
r = 1

i = int(input("Input i ---> "))
while count1 <= i:
    # l = 1
    # r = 1
    while r <= i:
        print(l, "x", r, "=", l * r)
        r+=1
    r = 1
    l += 1
    count1+=1