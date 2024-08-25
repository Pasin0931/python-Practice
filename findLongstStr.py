count1 = 0
count2 = 0
i = 0
temp1 = []
str_max = ""

while True:
    input1 = str(input("Please input your text ---> "))
    if input1 == "":
        break
    elif(len(input1) > len(str_max)):
        str_max = input1
print(str_max)
    # temp1.append(input1)
#     i+=1
# j = 0
# max = ""
# num_in = 0
# while j < i-1:
#     if(temp1[num_in] > temp1[j+1]):
#         max = temp1[num_in]
#     else :
#         max = temp1[j+1]
#     j+=1
# print("max", max)
    # if len(temp1[count1 + 1] > temp1[count1]):
    #     print(".")
    # else:
    #     count2+=1
    # count1+=1

# while i > count1:
#     if len(temp1[count1 + 1] > temp1[count1]):
#         print(".")
#     else:
#         count2+=1
#     count1+=1
