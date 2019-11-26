#knots and crosses

#import the random function from library for play vs computer
import random

#import the time function from library
#to improve the user experience
import time

LU="-"
MU="-"
RU="-"

LM="-"
MM="-"
RM="-"

LL="-"
ML="-"
RL="-"

#create a variable to store whether the game has been won or is a draw
#a 1 is a player has won and 2 is a draw
win=0

#create a variable to store the difficulty the user has selected
#set as 0 initially
#1 == easy
#2 == medium
difficulty=0

#function to print all game states on the screen
def displayBoard():
    print(" ")
    print(LU + " " + MU + " " + RU)
    print(LM + " " + MM + " " + RM)
    print(LL + " " + ML + " " + RL)
    print(" ")

#function to play two player game
def playGameTwo():

    #display the initial game board with empty states
    displayBoard()

    #set up a conditional loop until a player wins or all states are filled
    while (win!=1 or win!=2):
        
        #check if player has won
        if(win==1 or win==2):
                print("Game over")
                time.sleep(5)
                break
        else:

            #get player 1 move
            move1=input("Player 1 move: ")
            setMovePlayer1(move1)
            displayBoard()
            pass

        #check if player has won
        if(win==1 or win==2):
                print("Game over")
                time.sleep(5)
                break
        else:

            #get player 2 move
            move2=input("Player 2 move: ")
            setMovePlayer2(move2)
            displayBoard()
            pass

#function to play a game against computer
def playGameCPU():

    #create an array with all possibe game moves
    moves=["LU","LM","LL","MU","MM","ML","RU","RM","RL"]

    #display the initial game board with empty states
    displayBoard()

    #set up a conditional loop until either a player has won or all states are filled
    while (win!=1 or win!=2):

        #check to see if player has won
        if(win==1 or win==2):
            print("Game over")
            time.sleep(5)
            break
        else:

            #get player 1 move
            move1=input("Player 1 move: ")
            setMovePlayer1(move1)
            displayBoard()
            pass

        #check to see if CPU has won
        if(win==1 or win==2):
            print("Game over")
            time.sleep(5)
            break
        else:

            #get CPU move

            #options for the difficulty the user selected
            if(difficulty==1):
                move2=random.choice(moves)
            elif(difficulty==2):

                #create a new array of only valid moves
                validmoves=[]
                
                #manually check whether a move is present
                if(LU=="-"):
                    validmoves.append("LU")
                if(MU=="-"):
                    validmoves.append("MU")
                if(RU=="-"):
                    validmoves.append("RU")
                if(LM=="-"):
                    validmoves.append("LM")
                if(MM=="-"):
                    validmoves.append("MM")
                if(RM=="-"):
                    validmoves.append("RM")
                if(LL=="-"):
                    validmoves.append("LL")
                if(ML=="-"):
                    validmoves.append("ML")
                if(RL=="-"):
                    validmoves.append("RL")
                move2=random.choice(validmoves)

            #to start with the CPU goes for the middle piece
            #and tries to make a cross
            #basically ranks all the game states in order desirability
            #uses all 9 moves so a move will definitely be made by the CPU
            elif(difficulty==3):
                if(MM=="-"):
                    move2="MM"
                elif(MU=="-"):
                    move2="MU"
                elif(ML=="-"):
                    move2="ML"
                elif(LM=="-"):
                    move2="LM"
                elif(RM=="-"):
                    move2="RM"
                elif(LL=="-"):
                    move2="LL"
                elif(LU=="-"):
                    move2="LU"
                elif(RU=="-"):
                    move2="RU"
                elif(RL=="-"):
                    move2="RL"

            print("CPU move....")
            setMovePlayer2(move2)
            time.sleep(2)
            displayBoard()
            pass

        

def setMovePlayer1(x):
    #set global variables to set move states
    global LU,MU,RU
    global LM,MM,RM
    global LL,ML,RL

    global win
    
    #check what move the user entered
    if (x=="LU" and LU=="-"):
        LU="X";
    elif (x=="MU" and MU=="-"):
        MU="X";
    elif (x=="RU" and RU=="-"):
        RU="X";
    elif (x=="LM" and LM=="-"):
        LM="X";
    elif (x=="MM" and MM=="-"):
        MM="X";
    elif (x=="RM" and RM=="-"):
        RM="X";
    elif (x=="LL" and LL=="-"):
        LL="X";
    elif (x=="ML" and ML=="-"):
        ML="X";
    elif (x=="RL" and RL=="-"):
        RL="X";
    else:
        print("Invalid move")

    #check for win states after the move has been made
    #to see if player 1 has won
    if(LU=="X" and MU=="X" and RU=="X"):
        print("Player 1 wins!")
        win=1
    if(LM=="X" and MM=="X" and RM=="X"):
        print("Player 1 wins!")
        win=1
    if(LL=="X" and ML=="X" and RL=="X"):
        print("Player 1 wins!")
        win=1
    if(LU=="X" and LM=="X" and LL=="X"):
        print("Player 1 wins!")
        win=1
    if(MU=="X" and MM=="X" and ML=="X"):
        print("Player 1 wins!")
        win=1
    if(RU=="X" and RM=="X" and RL=="X"):
        print("Player 1 wins!")
        win=1
    if(LU=="X" and MM=="X" and RL=="X"):
        print("Player 1 wins!")
        win=1
    if(RU=="X" and MM=="X" and LL=="X"):
        print("Player 1 wins!")
        win=1

    #check if there are no moves left
    if(LU!="-" and MU!="-" and RU!="-" and LM!="-" and MM!="-" and RM!="-" and LL!="-" and ML!="-" and RL!="-" and win!=1):
        print("No more moves left - draw")
        win=2
        

def setMovePlayer2(x):
    #set global variables to set move states
    global LU,MU,RU
    global LM,MM,RM
    global LL,ML,RL

    global win
    
    #check what move the user entered
    if (x=="LU" and LU=="-"):
        LU="O";
    elif (x=="MU" and MU=="-"):
        MU="O";
    elif (x=="RU" and RU=="-"):
        RU="O";
    elif (x=="LM" and LM=="-"):
        LM="O";
    elif (x=="MM" and MM=="-"):
        MM="O";
    elif (x=="RM" and RM=="-"):
        RM="O";
    elif (x=="LL" and LL=="-"):
        LL="O";
    elif (x=="ML" and ML=="-"):
        ML="O";
    elif (x=="RL" and RL=="-"):
        RL="O";
    else:
        print("Invalid move")

    #check for win states after the move has been made
    #to see if player 2 has won
    if(LU=="O" and MU=="O" and RU=="O"):
        print("Player 2 wins!")
        win=1
    if(LM=="O" and MM=="O" and RM=="O"):
        print("Player 2 wins!")
        win=1
    if(LL=="O" and ML=="O" and RL=="O"):
        print("Player 2 wins!")
        win=1
    if(LU=="O" and LM=="O" and LL=="O"):
        print("Player 2 wins!")
        win=1
    if(MU=="O" and MM=="O" and ML=="O"):
        print("Player 2 wins!")
        win=1
    if(RU=="O" and RM=="O" and RL=="O"):
        print("Player 2 wins!")
        win=1
    if(LU=="O" and MM=="O" and RL=="O"):
        print("Player 2 wins!")
        win=1
    if(RU=="O" and MM=="O" and LL=="O"):
        print("Player 1 wins!")
        win=1

    #check if there are no moves left
    if(LU!="-" and MU!="-" and RU!="-" and LM!="-" and MM!="-" and RM!="-" and LL!="-" and ML!="-" and RL!="-" and win!=1):
        print("No more moves left - draw")
        win=2

#main program - needs to come after functions
print("Welcome to the knots and crosses python game")
print("Created by Steven Breakey")
print(" ")
print("Press 1 for single player mode (easy)")
print("Press 2 for single player mode (medium)")
print("Press 3 for single player mode (hard)")
print("Press 4 for two player mode")
print(" ")
mode=int(input("Please enter your selection: "))

#Easy mode is random moves - invalid moves are accepted
if(mode==1):
    difficulty=1
    print(" ")
    print("Single player mode (easy)")
    time.sleep(1)
    playGameCPU()

#Medium mode is random moves - invalid moves are not accepted
elif(mode==2):
    difficulty=2
    print(" ")
    print("Single player mode (medium)")
    time.sleep(1)
    playGameCPU()

#Hard mode is attempting to stop you from winning
#using a strategy
elif(mode==3):
    difficulty=3
    print(" ")
    print("Single player mode (hard)")
    time.sleep(1)
    playGameCPU()

#two player mode
elif(mode==4):
    print(" ")
    print("Two player mode")
    time.sleep(1)
    playGameTwo()
