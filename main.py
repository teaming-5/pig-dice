import random

command = ""
turns = 0
totalScore = 0
turnScoe = 0

while totalScore < 100:
    print("Turn: {} Score: {} in {} turns.".format(turnScore, totalScore, turns))
    command = input("command> ").lower()

    if command == "roll":
        roll = random.randit(1,6)
        if roll == 1:
            print("You rolled a 1!")
            turnScore = 0
            turns += 1
        else:
            turnScore += roll
    elif command == "hold":
        print("You've ended your turn.")
        totalScore += turnScore
        turnScore = 0
        turns += 1
    elif command == "quit":
        print("Bye!")
        break
    else:
        print("What?")
print("FINAL SCORE: {} in {} turns".format(totalScore, turns))

if totalScore >= 100:
    name = input("Winner! Enter your name: ")
