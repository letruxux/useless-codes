import random, time, os

move = ""
pcscore = 0
score = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def ask():
        global move
        move = input("Make a move! S-cissors, P-aper or R-ock.\n")
        if move == "S" or move == "P" or move == "R" or move == "s" or move == "p" or move == "r":
            if move == "S" or move == "s":
                move = "✂️"
            elif move == "P" or move == "p":
                move = "🧻"
            elif move == "R" or move == "r":
                move = "🪨"
            print("\nYou selected "+move+".")
        else:
            ask()
def game():
        global pcscore
        global score
        time.sleep(2)
        cls()
        ask()
        time.sleep(.2)
        ranchoice = random.choice(["✂️","🧻","🪨"])
        print("Computer selected"+ranchoice+".\n")
        
        fail = "You lost..."
        win = "You won!"

        def currentscore():
            global pcscore
            global score
            pcscore = pcscore + 1 - 1
            score = score + 1 - 1
            return "Current score: "+str(score)+"/"+str(pcscore)

        if ranchoice==move:
            print("It's a tie!")

        elif ranchoice=="✂️" and move=="🪨":
            score = score + 1
            score = score
            print(win)
            print(currentscore())
        
        elif ranchoice=="✂️" and move=="🧻":
            pcscore = pcscore + 1
            pcscore = pcscore
            print(fail)
            print(currentscore())

        elif ranchoice=="🪨" and move=="✂️":
            pcscore = pcscore + 1
            pcscore = pcscore
            print(fail)
            print(currentscore())
        
        elif ranchoice=="🪨" and move=="🧻":
            score = score + 1
            print(win)
            print(currentscore())

        elif ranchoice=="🧻" and move=="🪨":
            pcscore = pcscore + 1
            print(fail)
            print(currentscore())

        elif ranchoice=="🧻" and move=="✂️":
            score = score + 1
            print(win)
            print(currentscore())

        else:
            print("idk how but you did an impossible move")
        print("")
        game()

game()

