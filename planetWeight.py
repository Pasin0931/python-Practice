earthWeight = float(input("Please input your weight on Earth in kilo: "))
print("Available Planets ---> 1.Mercury 2.Venus 3.Earth 4.Mars 5.Jupiter 6.Saturn 7.Uranus 8.Neptune")
while(True):
    input1 = int(input("Please input number: "))
    if(input1 == 1):
        mercuryWeight = earthWeight * 0.38
        print("Your weight on Mercury is ",mercuryWeight,"kg")
    elif(input1 == 2):
        venusWeight = earthWeight * 0.91
        print("Your weight on Venus is ",venusWeight,"kg")
    elif(input1 == 3):
        print("Your weight on Earth is ",earthWeight,"kg")
    elif(input1 == 4):
        marsWeight = earthWeight * 0.38
        print("Your weight on Mars is ",marsWeight,"kg")
    elif(input1 == 5):
        jupiterWeight = earthWeight * 2.34
        print("Your weight on Jupiter is ",jupiterWeight,"kg")
    elif(input1 == 6):
        saturnWeight = earthWeight * 1.06
        print("Your weight on Saturn is ",saturnWeight,"kg")
    elif(input1 == 7):
        uranusWeight = earthWeight * 0.92
        print("Your weight on Uranus is ",uranusWeight,"kg")
    elif(input1 == 8):
        neptuneWieght = earthWeight * 1.19
        print("Your weight on Neptune is ",neptuneWieght,"kg")
    else:
        print("ERROR")
    contiOrNot = str(input("Do you which to calculate for your weight on other planets? Insert Yes or No: "))
    if(contiOrNot.lower() == "yes"):
        print("")
    else:
        print("")
        print("Program Ended!")
        break