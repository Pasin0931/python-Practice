# target = 72
# count = 0
# while(True):
#     randomNum = float(input("Please input your number = "))
#     if(randomNum == target):
#         print("Your guess is correct.")
#         count+=1
#         break
#     elif(randomNum > target):
#         if(randomNum > 100):
#             print("Your guess is out of range!")
#         else:
#             print("Your guess is too high.")
#         count+=1
#     elif(randomNum < target):
#         if(randomNum < 0):
#             print("Your guess is out of range!")
#         else:
#             print("Your guess is too low.")
#         count+=1
# print("You have done",count,"attemps!")

target = 72
count = 0
while(True):
    randomNum = float(input("Please input your number = "))
    if (randomNum < 0 or randomNum > 100):
        print("Your guess is out of range!")
    elif(randomNum > target):
        print("Your guess is too high.")
        count+=1
    elif(randomNum < target):
        print("Your guess is too low.")
        count+=1
    else:
        print("Your guess is correct.")
        count+=1
        break
print("You have done",count,"attemps!")