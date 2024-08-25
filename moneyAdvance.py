cash = int(input("Please input your cash = "))
fiftyBuck = cash // 50
cash = cash % 50
twentyBuck = cash // 20
cash = cash % 20
fiveBuck = cash // 5
cash = cash % 5
oneBuck = cash // 1
cash = cash % 1


print("1:",oneBuck)
print("5:",fiveBuck)
print("20:",twentyBuck)
print("50",fiftyBuck)    