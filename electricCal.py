unit = int(input("Please input your electrical charge: "))

if(0 <= unit <=150):
    newUnit = 3.5 * unit
    print("You have to pay",newUnit)
elif(150 < unit <= 400):
    newUnit1 = 3.5 * 150
    newUnit2 = 4.5 * (unit - 150)
    newUnit = newUnit1 + newUnit2
    print("You have to pay",newUnit)
elif(unit > 400):
    newUnit1 = 3.5 * 150
    newUnit2 = 4.5 * 250
    newUnit3 = 5.5 * (unit - 400)
    newUnit = newUnit1 + newUnit2 + newUnit3
    print("You have to pay",newUnit)
else:
    print("ERROR")