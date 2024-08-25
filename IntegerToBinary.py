# input1 = int(input("Input number: "))
# clone1 = input1
# while(clone1 != 0):
#     input1 = input1 % 2
#     print(input1,end="")
#     input1 = clone1 // 2
#     clone1 = input1
# print()

input1 = int(input("Input number: "))
rem = 0
inc = 1
bin = 0
while input1 != 0:
    rem = input1 % 2
    input1 = input1 // 2
    bin = bin + (rem * inc)
    inc = inc * 10
print(bin)