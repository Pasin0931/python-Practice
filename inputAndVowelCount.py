count = 0
countVOW = 0
vowels = ["a","e","i","o","u"]
while(True):
    input1 = str(input("Please input your letter and type quit to leave: "))
    if(input1.lower() == "quit"):
        print("Program Ended")
        print("Vowels: ",countVOW)
        print("Total input: ",count)
        break
    elif(input1.lower() in vowels):
        print(input1,"is a vowel!")
        countVOW+=1
        count+=1
    else:
        print(input1,"is NOT a vowel!")
        count+=1
    