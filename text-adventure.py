from time import *
from random import *

import os,sys
global PK

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#This is what i'll use to print the game title"
def title(): 
    print ("TRUMP'S AMERICA")
#and this is what i'll use to print the logo
sleep(3)
def logo():
    print ("                       || `-._.-.\n"
    "                              ||_    .'\n"
    "                              || `-.'\n"
    "         +                    ||                    +\n"
    "         |                    ||                    |\n"
    "        / \               _,,.||.__                / \/\n"
    "       /___\           ,-'         `-.            /___\/\n"
    " ______|===|_________,'               `.__________|===|______\n"
    "/      |===|        /                   \         |===|      \/\n"
   "/___________________/                     \____________________\/\n"
   "|  +-----+ +-----+  |`-._              _.-'|  +-----+ +-----+  |\n"
   "|  ||_|_|| ||_|_||  | |. `'----------'' .| |  ||_|_|| ||_|_||  |\n"
   "|  ||_|_|| ||_|_||  | |:  | ||    :| |  :| |  ||_|_|| ||_|_||  |\n"
"---| %%---%%+ +%%%--+  | |:__| ||____:| |__:| |  +-%%%-+ %%---%%% |---\n"
   "|%%%%_%%%%_%%%%%____| |/  | || -  :| |  \| |___%%%%%_%%%%_%%%%%|\n"
     "`|   %|   `|'   |`.`-._ | |'    `| |__.-'.'|  %|'   `|   %|\n"
    "                 |`.`-._``---....---''_.-'.'|\n"
    "                  `. `-._``---....---''_.-' .'\n"
    "                    `.   ``---....---''   .'\n"
    "                     `.                .'\n"
    "                        `.            .'\n"
    "                          `.        .'\n"
    "                           ().    .()\n"
"/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_||:    :||_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\\n"
"||=||=||=||=||=||=||=||=||=||=||:    :||=||=||=||=||=||=||=||=||=||=||\n"
"\n"
"\n")


def north():
    print ("Press n then enter to move north")
def south():
    print ("Press s then enter to move south")
def east():
    print ("Press e then enter to move east")
def west():
    print ("Press w then enter to move west")


def startup():
    global adventurer
    global HP
    global PK
    adventurer = raw_input("Hello! What is your name? ")
    print ("Hi, " + adventurer + ". Welcome to Trump's America.")
    HP = 100
    PK = 0

def voter():
    global team_member
    global response

    team_members = ["Megyn Kelly", "Melania Trump", "Bill Clinton"]
    responses = ["I'm with HER!", "Where are the emails?!", "Make America Great Again!", "That man is a racist, misogynistic bigot!"]
    shuffle(team_members)
    team_member = team_members[0]
    print ("\n["+team_member+":] Hi, my name is "+team_member+", Would you like to talk to me?")
    shuffle (responses)
    print ("Press y to talk or n to ignore: ")
    if raw_input() == "y":
        print ("["+team_member+":] " +responses[0])
    else:
        print("["+team_member+":] Bye!")

def trump():
    global trumpname
    trumpname = "Donald Trump"
    print ("\nYou see what looks like an orange peel off in the distance. It's "+trumpname+" , and he's coming straight toward you")

def clinton():
    global clintonname
    clintonname = "Hillary Clinton"
    print ("\nA pantsuit clad woman appears. It's "+clintonname+" , and she's coming straight toward you")

def pkpoint():
    global PK
    PK += 1
    print ("Now your political knowledge is " + str(PK) + "/10. Nice job!")

def question():
    print ("A White House aid appears!")
    sleep(2)
    print("\n")
    print ("They ask if you want to learn about the secretary of state, chief of staff, chief strategist, attorney general, or TK.")
    print("\n")
    sleep(3)
    thequestion = raw_input("Which one? ")
    if thequestion == "secretary of state":
        print("\n")
        print("[White House aid:] Trump wants to make the US energy independent, but hasn't release many specifics. Clinton wants to increase renewable energy sources and decrease greenhouse gas emissions. Read more here: http://bit.ly/2cwi8ws")
    elif thequestion == "chief of staff":
        print("\n")
        print("[White House aid:] Trump has yet to deliver any specific student loan policy. Clinton wants to cut interest rates on loans, make income based repayment easier to get, and make community college free")
    elif thequestion == "chief strategist":
        print("\n")
        print("[White House aid:] Trump is vehemently pro gun. Clinton wants comprehensive background checks and to close loopholes in gun laws")
    elif thequestion == "attorney general":
        print("\n")
        print("[White House aid:] Trump wants to build a wall to protect US borders and deport the 11 million people living in the US illegally. Clinton will defend Obama's executive action and introduce comprehensive immigration reform with a path to full citizenship")
    elif thequestion == "TK":
        print("\n")
        print("[White House aid:] Trump wants to cut business taxes,renegotiate NAFTA and make it easier to manufacture. Clinton wants to raise wages, cut middle class taxes")
    else:
        print("\n")
        print("[White House aid:] Sorry, I don't know anything about that. Enter secretary of state, chief of staff, chief strategist, attorney general, or TK")

def map():
    print ("You went " + str(moveone) + " last time")

def maptwo():
    print ("You've already been " + str(movefour) + " and " + str(moveone))

def mapthree():
    print ("You've already been " + str(movesix) + " and " + str(movefour) + " and " + str(moveone))

def notebook():
    print ("You've traveled " + str(moveeight) + " , " + str(movesix) + " , " + str(movefour) + " , " + str(moveone))

def healthhit():
    global HP
    HP -= 20
    print ("Uh oh, the secret service has spotted you! Run!")
    sleep(2)
    print ("Too late. They tackled you and escorted you back to the front door. Your health is now " + str(HP) + "/100")


clear_screen()
title()
logo()
startup()

sleep(2)
print("\n")
print ("Your quest (if you choose to accept it) is to collect as much information about the president's inner circle as possible.")
sleep(2)

print ("\nYour health is" + " " + str(HP))
sleep(2)
print("\n")
print ("Your political knowledge is" + " " + str(PK) + " out of 10")
print ("\n")
sleep(2)
print ("Ready to start your quest?")
print("\n")
sleep(2)
print ("Press y then enter to start your quest.")
sleep(1)
print ("Or press n to abandon your quest and move to Canada.")

print("\n")

if raw_input() == "y":
    print ("You are outside the White House. Suddenly, Bernie Sanders appears.")
    print("\n")
    sleep(3)
    print ("[Bernie Sanders]: It's dangerous to go alone. Take this.")
    sleep(3)
    print("\n")
    nb = raw_input("Add mystery object to your inventory? y or n? ")
    if nb == "y":
        inventory = []
        inventory.append("notebook")
        print("\n")
        print ("You are now carrying a" + " " + inventory[0] + ".")
    else:
        print("\n")
        print ("Yikes, how will you remember everything without a notebook? I hope you don't lose your way.")
else:
    print ("You start packing a suitcase for Canada.")
    print ("GAME OVER")
    sys.exit(0)

sleep(2)
print ("\n")
print ("You walk inside the White House and see a staircase straight ahead to the north, a door to the east, and a hallway to the west.")

print("\n")
sleep(3)
print("\n")
sleep(3)

move = raw_input("Which direction would you like to go? ")

north()
east()
west()

print("\n")

if move == 'n':
    print ("\nYou move north up the staircase.")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
    print ("\n")
    sleep(2) 
elif move == 'e':
    print ("\nYou walk east and open the door.")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
    print ("\n")
    sleep(2)
elif move == 'w':
    print ("\nYou walk west down the hallway.")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
    print ("\n")
    sleep(2)
elif move == 's':
    print ("\nYou head back to the entrance.")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
    print ("\n")
    sleep(2)

voter()

print("\n")
sleep(2)

moveone = raw_input("You nod politely and hurry on your way. Which way now? ")


if moveone == "n":
    print ("You are in the oval office.") 
elif moveone == "e":
    print ("You are in the kitchen.")
elif moveone == "w":
    print ("You are in the Rose room.")
else :
    print ("You are back at the main entrance.")

sleep(1)
print ("You log your position in the notebook.")
print ("\n")
question()

sleep(4)
print ("\n")
print ("You logged the info in your notebook.")

print ("\n")
sleep(3)

pkpoint()

print ("\n")
sleep(2)

print ("Ready to keep exploring?")
print ("\n")
map()
print ("\n")
movetwo = raw_input("Which direction now? ")


if movetwo == moveone:
    print ("You already found all the answers that way! Choose a new direction or you might get lost...")
elif movetwo == "e":
    print ("You are heading toward the kitchen.")
elif movetwo == "w":
    print ("You are heading toward the Rose room.")
else:
    print ("You are heading back to the entrance.")

print ("\n")
sleep(3)

print ("Someone is comning!")
sleep(3)

voter()
print ("\n")
movethree = raw_input("Now which way? ")
print ("\n")
if movethree == moveone:
    healthhit()
elif movethree != moveone:
    print ("You're back at the main entrance")
print ("\n")
movefour = raw_input("Now which way? ")
print ("\n")
if movefour == "n":
    print ("You are in the oval office.") 
elif movefour == "e":
    print ("You are in the kitchen.")
elif movefour == "w":
    print ("You are in the Rose room.")
else:
    print ("You are back at the main entrance.")

question()

print("\n")
sleep(4)
pkpoint()

print("\n")

print("Ready to keep moving?")
maptwo()
print ("\n")
movefive = raw_input("Which way now? ")
print ("\n")
if movefive == movefour or moveone:
    healthhit()
elif movethree != movefour or moveone:
    print ("You're back at the main entrance.")
print ("\n")
movesix = raw_input("Which way? ")
print ("\n")
if movesix == "n":
    print ("You are in the oval office.") 
elif movesix == "e":
    print ("You are in the kitchen.")
elif movesix == "w":
    print ("You are in the Rose room.")
elif movesix == "s":
    print ("You are in a valley.")
else:
    print ("Pick a new direction!")
print ("\n")
question()

print("\n")
sleep(4)
pkpoint()

print("\n")

moveseven = raw_input("Ready to keep moving? Which way? ")

if moveseven == movefour or moveone or movesix:
    healthhit()
elif movethree != movefour or moveone or movesix:
    print ("You're back at the main entrance.")

print ("\n")
print ("Someone is comning!")
sleep(3)
voter()

print("\n")
mapthree()
print("\n")
moveeight = raw_input("Which way now? ")
    
if moveeight == "n":
    print ("You are in the oval office.") 
elif moveeight == "e":
    print ("You are in the kitchen.")
elif moveeight == "w":
    print ("You are in the Rose room.")
elif moveeight == "s":
    print ("You are back at the main entrance.")
else:
    healthhit()


question()

print("\n")
sleep(4)
pkpoint()

print("\n")      

print("Wow you've almost completed your quest!")
print ("\n")
notes = raw_input("Want to review your notebook? ")

if notes == "y" or "yes":
    notebook()
else:
    print ("fine")

print("bye!")