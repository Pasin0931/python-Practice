# input :
# (-1 to end the program): 
# 5
# 8
# 12
# 4
# -1
# ouptut:
# avg: 7.25
# sum = 0
# i = 0
# inputn = 0
# while True:
#     inputn = int(input("Input number ---> "))
#     if inputn == -1:
#         break
#     else:
#         sum = inputn + sum
#         i+=1
# print("Average ---> ", sum / i)



# input :
# (-1 to end the program): 
# 5
# 8
# 12
# 4
# -1
# ouptut:
# max: 12


# inputnum = int(input("Input number ---> "))
# max = inputnum
# while True:
#     if inputnum == -1:
#         break
#     elif max < inputnum:
#         max = inputnum
#     else:
#         pass
#     inputnum = int(input("Input number ---> "))
# print("Maximun number ---> ",max)



# input :
# (-1 to end the program): 
# 5
# 8
# 12
# 4
# -1
# ouptut:
# max: 12
# min: 4


inputNum = int(input("Input: "))
max = inputNum
min = inputNum
while True:
    if inputNum == -1:
        break
    elif inputNum < min:
        min = inputNum
    elif inputNum > max:
        max = inputNum
    inputNum = int(input("Input: "))
if  min == -1 or max == -1:
    print("-")
else:
    print("Maximum: ", max)
    print("Minimum: ", min)