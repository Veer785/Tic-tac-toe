import random

while True:
    ccount = 0  # It is used to store the score of the game
    ucount = 0
    l = ['rock', 'scissor', 'paper']

    op = int(input('''
Game Start............    
1. Yes
2. No | Exit
'''))
    if op == 1:
        for a in range(1, 6):
            userinput = int(input('''
1. rock
2. scissor
3. paper            
            '''))
            uchoice = ""
            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"
            cchoice = random.choice(l)
            print("computer value ", cchoice)
            print("user value", uchoice)

            if cchoice == uchoice:
                print("game draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "paper" and cchoice == "rock") or (uchoice == "scissor" and cchoice == "paper"):
                print("you win")
                ucount += 1
            else:
                print("computer win")
                ccount += 1
            print()

    if ccount == ucount:
        print("Final game draw")
    elif ccount > ucount:
        print("Final computer wins this game")
    else:
        print("Final you are the winner")

    print("Your score:", ucount)
    print("Computer score:", ccount)

    op = int(input('Do you want to play again?\n1. Yes\n2. No | Exit\n'))
    if op != 1:
        break