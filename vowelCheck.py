input1 = str(input("Please input your letter: "))
vowel1 = ["a","e","i","o","u"]
vowel2 = ["A","E","I","O","U"]
if((input1 in vowel1) or (input1 in vowel2)):
    print(input1,(" is a vowel!"))
else:
    print(input1, (" is NOT a vowel!"))

# check
# print(vowel1)
# print(input1)
# print(input1 in vowel1)
# print(type(vowel1))