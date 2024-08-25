age = int(input("Please input your age: "))
if(age < 13):
    if(age < 10):
        print("Little kid should play toys.")
    if(age >= 10 and age <= 12):
        print("Kid should start learning music.")
elif(13 <= age and 19 >= age):
    if(age < 16):
        print("Young teenage should having intrest in sports.")
    if(16 <= age and 19 >= age):
        print("Old teenage should start caring about future career.")
else:
    print("Adult should work for their family.")