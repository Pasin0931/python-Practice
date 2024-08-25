point = int(input("Please input your point: "))
costOfProduct = int(input("Please input your product cost: "))

if(point < 1000000):
    print("You won't recieve any discount")
    print("Your have to pay",costOfProduct)
    print("Your have ",point," points remains.")

if(point >= 1000000 and point < 2000000):
    print("You have recieved 10% discount")
    fis = 10 * costOfProduct
    sec = fis / 100
    last = costOfProduct - sec
    print("Your have to pay",last)
    remainPoi = point - 1000000
    print("Your have ",remainPoi," points remains.")
else:
    if(point >= 2000000 and point < 3000000):
        print("You have recieved 15% discount")
        fis = 15 * costOfProduct
        sec = fis / 100
        last = costOfProduct - sec
        print("Your have to pay",last)
        remainPoi = point - 2000000
        print("Your have ",remainPoi," points remains.")
    else:
        if(point >= 3000000 and point < 6000000):
            print("You have recieved 20% discount")
            fis = 20 * costOfProduct
            sec = fis / 100
            last = costOfProduct - sec
            print("Your have to pay",last)
            remainPoi = point - 3000000
            print("Your have ",remainPoi," points remains.")
        else:
            if(point >= 6000000 and point < 9000000):
                print("You have recieved 30% discount")
                fis = 30 * costOfProduct
                sec = fis / 100
                last = costOfProduct - sec
                print("Your have to pay",last)
                remainPoi = point - 6000000
                print("Your have ",remainPoi," points remains.")
            else:
                if(point >= 9000000):
                    print("You have recieved 40% discount")
                    fis = 40 * costOfProduct
                    sec = fis / 100
                    last = costOfProduct - sec
                    print("Your have to pay",last)
                    remainPoi = point - 9000000
                    print("Your have ",remainPoi," points remains.")