import random


def play():
    print("HANGMAN GAME")
    print("Instruction (The number of blanks represent the word length)")
    words = ["kogip","ooo"]
    ran = random.randint(0, len(words) - 1)
    word = words[ran]
    blank = ""
    correctLetters = []
    playerLive = 5
    count = 0
    done = False
    for i in word:
        blank += "-"
        correctLetters.append("-")
    print(blank)
    letter = input("Guess a letter: ")
    while True:
        filledBlanks = ""
        if letter in word:
            print("Right")
            for pox in range(len(word)):
                curr = word[pox]
                if letter == curr:
                    correctLetters[pox] = letter
            for c in correctLetters:
                filledBlanks += c
            print(filledBlanks)
            if playerLive == 0:
                print(f"Game Over! You Loose, answer was {word}")
                break
            if "-" not in filledBlanks:
                print("Game Over! You Won")
                break
            letter = input("Guess a letter: ")
        else:
            print("Wrong")
            playerLive -= 1
            if playerLive == 0:
                print(f"Game Over! You Loose, answer was {word}")
                break
            letter = input("Guess a letter: ")
