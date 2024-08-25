oneBuck = 0
fiveBuck = 0
twentyBuck = 0
fiftyBuck = 0

cash = int(input("Please input your cash = "))
while (cash != 0):
    if(cash >= 50):
        cash = cash - 50
        fiftyBuck+=1
    elif((cash <= 50) and (cash >= 20)):
        cash = cash - 20
        twentyBuck+=1
    elif((cash <= 20) and (cash >= 5)):
        cash = cash - 5
        fiveBuck+=1
    elif((cash <=5) and (cash >= 1)):
        cash = cash - 1
        oneBuck+=1
print("1:",oneBuck)
print("5:",fiveBuck)
print("20:",twentyBuck)
print("50",fiftyBuck)     