####Rock Paper Scissors game
import random as r
import re
print("Hi, um how do you want me to address you?")
player_name=""
player_name=input("Your name please:\n ")

print("\nHey! "+player_name+"  👋 \nThis is a Rock Paper Scissors interactive game\nInstructions: type any of these three hand signs for your turn, I will immediately spawn my move,\n ")
print("Type:\nRock or rock or stone or R or r ✊ ")
print("Paper or p or P  📃")
print("Scissors or s or S ✂")
print("Rules: you know them already lol")
input()
print("jk, rock beats scissors, paper beats rock, scissors beats paper\n**dont ask me why**  🤭")
print("Lets start already.\n\nJust press Quit or Q or no to stop the game.")
score =0
player_score=0
pybot_score=0
movestandard={ 1:"ROCK ", 2:"PAPER 📄", 3:"SCISSORS ✂"}
def scored_as(p, b):
    if(p==b ): return 0
    elif(p==1 and b==3):return 1 #player rock, bot scis WON
    elif(b==1 and p==3):return -1 # player sci, bot rock LOST
    elif(p==2 and b==3):return -1 #p paper, bot sci LOST
    elif(b==2 and p==3):return 1 #player sci, bot paper WON
    elif(p==1 and b==2):return -1 #player rock, bot paper Lost
    elif(b==1 and p==2):return 1 #player paper, bot rock WON
#rules to win completed
flag=True

#script to display the player as winner
def player_won():
    won_lines=[
        " Oh! nice move",
        " GOOD!",
        " You beat me!",
        " OOoooh Noice 😯",
    ]

    print(won_lines[r.randint(0,3)])


def player_lost():
    lost_lines=[
        " Sorry, you didn't win 😕🤷‍♀️",
        " Oh! I won",
        " Hmm, rock beats scissors, paper beats rock, scissors beats paper, \n I didn't make the rules lol, the Bot won",
        " Hehe, let's try again?, The bot won"
    ]    

    print(lost_lines[r.randint(0,3)])

def tie():
    tie_lines=[
        " Hmm, we used the same move ugh, again",
        " It's a draw 🥱🥺",
        " Did you copy my move?🤨"
    ]
    print(tie_lines[r.randint(0,2)])
while flag: # stops when user wants
    print("================\n\nIts your turn now, so what's your move:   🤔\n  ")
    player_move=input(":\t")
    if(player_move.lower()=='q' or player_move.lower()=="stop" or player_move.lower()=="no"):
        print("\nOh!, so soon?\nHave a great day    😊😄✊📄✂\n")
        break
    moves=[ ["rock","stone", "r"], ["paper","p"] , ["scissors", "s"] ]
    for x in range(len( moves)):
        for move in moves[x]:
            if(re.search(move,player_move.lower())):
                player_number=x+1
                break
#player move has been taken 
    bot_move=r.randint(1,3)# my bot move is randomly decided
    print("\n\tYour move\t\t\t my move")
    print(" \t"+ movestandard[player_number]+ "    \t\t\t "+movestandard[bot_move]+ "\n\n" )
    won=int(0)
    won = scored_as(player_number, bot_move)
    if(won==1):
        player_won()
        player_score+=1
    elif(won==-1): 
        player_lost()
        pybot_score+=1
    else: tie()
    print("_________________________________________________________")
    print(" Score : "+player_name+" = "+str(player_score)+" and bot = " +str(pybot_score))
    print("_________________________________________________________")
    print("Do you wanna play again? yes / no")
    game_continue=input(":")
    if(game_continue.lower()=="no"):
        flag=False
        print("Thanks for playing ;p")
    else: flag=True


