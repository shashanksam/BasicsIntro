import random as r
import re
print("Hi, um how do you want me to address you?")
player_name=""
player_name=input("Your name please:\n  ")

print("Hey! "+player_name+"😁👋 \nThis is a Rock Paper Scissors interactive game\nInstructions: type any of these three hand signs for your turn, I will immediately spawn my move, I promise there's not cheating lol ")
print("\nType either \nRock or rock or stone or just R or r ✊ ")
print("\nPaper or p or P 📄📃")
print("\nScissors or s or S ✂")
print("Rules: you know them already lol")
input()
print("JK, rock beats scissors, paper beats rock, scissors beats paper\n**dont ask me why**🤭")
print("Lets start already.\n__ Just press Quit or Q or no to stop the game __")
score =0
player_score=0
pybot_score=0
moves={ 1:"rock✊✊✊", 2:"paper📄📄📄", 3:"scissors✂✂✂"}
def scored_as(p_move, b_move):
    if(p_move==b_move ): return 0
flag=True

#script to display the player as winner
def player_won():
    won_lines=[
        "Oh! nice move",
        "GOOD!",
        "You beat me!",
        "OOoooh Noice 😯",
    ]

    print(won_lines[r.randint(0,3)])


def player_lost():
    lost_lines=[
        "Sorry, you didn't win 😕🤷‍♀️",
        "Oh! I won",
        "Hmm, rock beats scissors, paper beats rock, scissors beats paper, \n I didn't make the rules lol, the Bot won",
        "Hehe, let's try again?, The bot won"
    ]    

    print(lost_lines[r.randint(0,3)])

def tie():
    tie_lines=[
        "Hmm, we used the same move ugh, again",
        "It's a draw 🥱🥺",
        "Did you copy my move?🤨"
    ]
    print(tie_lines[r.randint(0,2)])
while flag: # stops when user wants
    print("========================\nIts your turn now, so what's your move:🤔\n  ")
    player_move=input(":\n")
    if(player_move.lower()=='q' or player_move.lower()=="stop" or player_move.lower()=="no"):
        print("\n\nOh!, so soon?\nHave a great day😊😄✊📄✂\n")
        break
    moves=[ ["rock","stone", "r"], ["paper","p"] , ["scissors", "s"] ]
    for x in moves:
        for move in moves[x]:
            if(re.search(move,player_move.lower())):
                player_number=x+1
                break
#player move has been taken 
    bot_move=r.randint(1,3)# my bot move is randomly decided
    print("\n\n\n"+player_name+"move\t\t\t\t my move")
    print(moves[player_number]+"    \t\t\t\t "+moves[bot_move])
    #now lets see who won
    won=scored_as(player_number, bot_move)
    if(won==1):player_won()
    elif(won==-1): player_lost()
    else: tie()

