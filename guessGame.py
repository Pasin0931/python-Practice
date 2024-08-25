import random

# tempWord = []
def randoma():
    # while True:
    #     word = str(input("Type your word ---> ")).lower()
    #     if word == "":
    #         break
    #     tempWord.append(word)
    tempWord = [
        "tom yum goong",
        "pad thai",
        "som tum",
        "tom kha gai",
        "gaeng keow wan",
        "pad krapow moo saap",
        "khao pad",
        "pad see ew",
        "laab",
        "moo ping"]
    #
    # tempWord = [
    #     "sushi",
    #     "ramen",
    #     "tempura",
    #     "sashimi",
    #     "udon",
    #     "yakitori",
    #     "okonomiyaki",
    #     "katsu curry",
    #     "tonkatsu",
    #     "miso soup"]

    # tempWord = [
    #     "coq au vin",
    #     "boeuf bourguignon",
    #     "ratatouille",
    #     "escargot",
    #     "croque monsieur",
    #     "quiche lorraine",
    #     "bouillabaisse",
    #     "cassoulet",
    #     "crème brûlée",
    #     "soufflé"]

    return random.choice(tempWord)

def word_stat(word, guessed_letter):
    display = ""
    for letter in word:
        if letter in guessed_letter:
            display += letter
        # display+=str(guessed_letter)
        else:
            display+=" _ "
    return display

def wordGuessingG():
    boola = True
    secretWord = randoma()
    guessed_letter = []
    attemp = 12
    print(secretWord)
    while True:
        i = str(input("Press _ to continue ---> "))
        if i == "":
            break
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("Guess a word!!")
    print("**--------------------------------------**")
    print("Secret word ---> ", word_stat(secretWord, guessed_letter))

    while attemp > 0:
        if boola == False:
            print("*")
            print("*")
            print("*")
            print("*")
            print("Game ended!")
            break
        guess = str(input("Guess a letter: ")).lower()
        if len(guess) != 1:
            print("You must ut only 1 letters!")
            continue
        if guess in guessed_letter:
            print("You already guess that letter!")
            continue
        guessed_letter.append(guess)
        print(guessed_letter)

        if guess not in secretWord:
            attemp -= 1
            print("*")
            print("No letter", guess, "occur in the word.")
            print("*")
            print("You have", attemp,"attemps left!")
        else:
            occur = secretWord.count(guess)
            print("Letter", guess, "occur", occur, "times!")
        currentStat = word_stat(secretWord, guessed_letter)
        print("Secret word: ", currentStat)

        if " _ " not in currentStat:
            print("*")
            print("Congratulation!! you guess the word correctly!")
            boola = False
    if " _ " in currentStat:
        print("You ran out of attemps! the secret word is ", secretWord)

wordGuessingG()

# randoma()
# print(tempWord)
