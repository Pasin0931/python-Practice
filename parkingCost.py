hour = int(input("Horurs = "))
minute = int(input("Minute = "))

newMinute = hour * 60
trueMinute = hour * 60
lastMinute = newMinute + minute

if(trueMinute >= 15):
    lastMinute = lastMinute - 15
    if(trueMinute > 16 and trueMinute < 120):
        cost = 10
        print("Your cost is ",cost)
    else:
        if(trueMinute >= 120):
            lastMinute = lastMinute - 120
            lastHours = lastMinute // 60
            hrCost = lastHours * 10
            lastCost = 20 + hrCost
            print("Your cost is ",lastCost)
else:
    print("Free")