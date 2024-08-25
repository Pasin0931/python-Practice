listScore = []
countScore = [0,0,0,0,0,0,0,0,0,0,0]
countKid = 1
index = 0
count = 0

while countKid <= 10:
    scoreInput = int(input("Please enter student's score ---> "))
    if scoreInput > 10 or scoreInput < 0:
        print("Score is out of range!")
    else:
        listScore.append(scoreInput)
        countKid+=1
print("Original list ---> ",listScore)

while index < len(listScore):
    indexCountScore = listScore[index]
    countScore[indexCountScore]+=1
    index+=1

print(countScore)

while count <= 10:
    print(count, " ---> ", countScore[count] * "*")
    count+=1