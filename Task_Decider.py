""" Don't know what to decide? use this to make up your mind"""
import random as r

decisions=[]

print("""Enter your tasks:
""")

while True:
    try:
        todo="\n"
        todo=input()
    except EOFError as e:
        todo=""
        if(len(decisions)==0): continue
        else :break
    if(todo!="\n" and todo!=""): decisions.append(todo)
    else: break

if(len(decisions)):print("Your choices are:")
for choice in decisions:
    print(" ",choice)

try:
    print("\nwhy dont you-",decisions[r.randint(0,len(decisions)-1)])
except ValueError:
    print("You dont have anything to do?\nReally?\nLets try again.")
    
    
""" try these inputs as an example, just copy and paste them in the input box
drink water
text hello to a friend
learn python
turn off the lights
eat something healthy
help @shashanksam by improving the program

"""
