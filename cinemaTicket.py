vipAc = str(input("Are you a VIP(Awnser Yes or No)? : "))
age = int(input("How old are you: "))
row = str(input("What row do you want to sit: "))
discontRow = ["a","b","c","d"]
undiscountRow = ["e","f","g","h"]

if(vipAc.lower() == "yes"):
    if(55 <= age < 65):
        print("You have recieved special seat with 20% discount.")
    if(age >= 65):
        print("You have recieved special seat with 30% discount.")
else:
    # if(row.lower() == "a" or row.lower() == "b" or row.lower() == "c" or row.lower() == "d"):
    if(row.lower() in discontRow):
        print("You have recieved a normal seat with no discount.")
    elif(row.lower() in undiscountRow):
        print("You have recieved a normal seat with 10% discount.")
    else:
        print("The row doesn't exist.")