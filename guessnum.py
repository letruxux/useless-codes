import random,os

maxg = input("Max guess?\n")
maxg = int(maxg)

anwser = random.randint(1,maxg)

guess = input("Guess the number between 1 and "+str(maxg)+".\n")
while True:
    if int(guess) == anwser:
        print("You guessed it!")
        os.system('pause' if os.name=='nt' else 'read')
    else:
        guess = input("Wrong, guess the number between 1 and "+str(maxg)+".\n")