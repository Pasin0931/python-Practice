vowel = ["a","e","i","o","u"]
count = 0
countVowel = 0

inputLetter = str(input("Please input your word: "))
while count < len(inputLetter):
    if inputLetter[count].lower() in vowel:
        print("",end="")
        countVowel+=1
        count+=1
    else:
        print(inputLetter[count],end="")
        count+=1
print("\n"+str(countVowel))

vowel = ["a","e","i","o","u"]
# str_cutting = []
str_cutting = ""
count = 0
countVowel = 0

# ---------------------------------------------------------------

# vowel = ["a","e","i","o","u"]
# # str_cutting = []
# str_cutting = ""
# count = 0
# countVowel = 0

# inputLetter = str(input("Please input your word: "))
# # "hello"
# # inputLetter[0] = "h"
# while count < len(inputLetter):
#     if inputLetter[count].lower() in vowel:
#         # str_cutting+=inputLetter[count]
#         # str_cutting.append(inputLetter[count])
#         countVowel+=1
#     else:
#         # "" + "h"
#         str_cutting+=inputLetter[count]
#         # str_cutting = str_cutting + inputLetter
#         # str_cutting.append(inputLetter[count])
#     count+=1
# print(countVowel)
# print(str_cutting)
# # i = 0
# # while i < len(str_cutting):
# #     print(str_cutting[i],end="")
# #     i+=1
# # print()
# # print(str_cutting)

# # print("\n"+str(countVowel))