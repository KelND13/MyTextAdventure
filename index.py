from time import *
from random import *

import os,sys
global PK

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

#This is what i'll use to print the game title"
def title(): 
    print ("Politicai")
#and this is what i'll use to print the logo
def logo():
    print ("Learn")


def north():
    print ("Press n then enter to move north")
def south():
    print ("Press s then enter to move south")
def east():
    print ("Press e then enter to move east")
def west():
    print ("Press w then enter to move west")


def startup():
    global votee
    global HP
    global PK
    votee = input("Hello courageous voter! What is your name? ")
    HP = 100
    PK = 0

def voter():
    global friendname
    global response

    friendnames = ["Megyn Kelly", "Bernie Sanders", "Bill Clinton"]
    responses = ["I'm with HER!", "Where are the emails?!", "Make America Great Again!", "That man is a racist, misogynistic bigot!"]
    shuffle(friendnames)
    friendname = friendnames[0]
    print ("\n["+friendname+":] Hi, my name is "+friendname+", Would you like to talk to me?")
    shuffle (responses)
    print ("Press y to talk or n to ignore: ")
    if input() == "y":
        print ("["+friendname+":] " +responses[0])
    else:
        print("["+friendname+":] Bye!")

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
    print ("Now your political knowledge is " + str(PK) + "/5. Nice job!")

def question():
    print ("A helpful villager suddenly appears!")
    print ("They ask if you want to learn more about energy, student debt, gun reform, immigration, or the economy.")
    thequestion = input("Which one? ")
    if thequestion == "energy":
        print("\n")
        print("[Villager:] Trump wants to make the US energy independent, but hasn't release many specifics. Clinton wants to increase renewable energy sources and decrease greenhouse gas emissions. Read more here: http://bit.ly/2cwi8ws")
    elif thequestion == "student debt":
        print("\n")
        print("[Villager:] Trump has yet to deliver any specific student loan policy. Clinton wants to cut interest rates on loans, make income based repayment easier to get, and make community college free")
    elif thequestion == "gun reform":
        print("\n")
        print("[Villager:] Trump is vehemently pro gun. Clinton wants comprehensive background checks and to close loopholes in gun laws")
    elif thequestion == "immigration":
        print("\n")
        print("[Villager:] Trump wants to build a wall to protect US borders and deport the 11 million people living in the US illegally. Clinton will defend Obama's executive action and introduce comprehensive immigration reform with a path to full citizenship")
    elif thequestion == "economy":
        print("\n")
        print("[Villager:] Trump wants to cut business taxes,renegotiate NAFTA and make it easier to manufacture. Clinton wants to raise wages, cut middle class taxes")
    else:
        print("\n")
        print("[Villager:] Sorry, I don't know anything about that. Enter the word energy, student debt, gun reform, immigration, or economy. Which one? ")

def map():
    print ("You went " + str(moveone) + " last time")
def maptwo():
    print ("You've already been " + str(movefour) + " and " + str(moveone))

def mapthree():
    print ("You've already been " + str(movesix) + " and " + str(movefour) + " and " + str(moveone))

def notebook():
    print ("You've traveled " + str(moveeight) + " , " + str(movesix) + " , " + str(movefour) + " , " + str(moveone))

clear_screen()
title()
logo()
startup()


print ("Welcome to the land of Politicai, " + votee)
sleep(2)
print("\n")
print ("Your quest is to collect as much information about the presidential candidates as possible")
sleep(2)

print ("\nYour health is" + " " + str(HP))
print ("Your political knowledge is" + " " + str(PK) + " out of 5")
print ("\n")
sleep(2)
print ("Ready to start your quest? Press y then enter to start your quest. Or press n to abandon your quest.")

print("\n")

if input() == "y":
    print ("You are in your room. You see a notebook next to your bed.")
    print ("Would you like to take the notebook? y or n?")
    if input() == "y":
        inventory = []
        inventory.append("notebook")
        print ("You are now carrying your" + " " + inventory[0])
    else:
        print ("Yikes, how will you remember all the political knowledge you pick up without your notebook? Good luck!")
else:
    print ("You sit at home and decide you're better off not voting at all.")
    print ("GAME OVER")
    ys.exit(0)

sleep(2)
print ("\n")

print ("You see a village straight ahead to the north, a forest to the east, a lake to the west, and a valley behind you to the south")

print("\n")
sleep(3)

north()
south()
east()
west()

print("\n")
sleep(3)

move = input("Which direction would you like to go? ")


if move == 'n':
    print ("\nYou move north down the dirt road toward the village")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.") 
elif move == 'e':
    print ("\nYou walk east toward the forest")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
elif move == 'w':
    print ("\nYou walk west toward the lake")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")
elif move == 's':
    print ("\nYou carefully hike down into the valley")
    print ("\n")
    sleep(2)
    print ("Someone blocks your path.")

voter()

print("\n")
sleep(2)

moveone = input("You nod politely and decide to keep moving. Which way? ")


if moveone == "n":
    print ("You are in a village") 
elif moveone == "e":
    print ("You are in a forest")
elif moveone == "w":
    print ("You are by a lake")
else :
    print ("You are in a valley")

sleep(1)
print ("You log your position in the notebook")
print ("\n")
question()

print ("\n")
print ("You logged the info in your notebook")

print ("\n")
sleep(3)

pkpoint()

print ("\n")
sleep(2)

print ("You're ready to keep exploring")
print ("\n")
map()
print ("\n")
movetwo = input("Which way now? ")


if movetwo == moveone:
    print ("You already found all the knowledge that way! Choose a new direction or you might get lost...")
elif movetwo == "e":
    print ("You are heading toward the forest")
elif movetwo == "w":
    print ("You are heading toward the lake")
else:
    print ("You are heading back to the valley")

print ("\n")
sleep(3)

print ("Someone is comning!")
sleep(3)

voter()

movethree = input("Now which way now? ")

if movethree == moveone:
    print ("You already found all the knowledge in that direction! Choose a new direction ")
elif movethree != moveone:
    print ("You're back at the house")

movefour = input("Now which way? ")

if movefour == "n":
    print ("You are in a village") 
elif movefour == "e":
    print ("You are in a forest")
elif movefour == "w":
    print ("You are by a lake")
else:
    print ("You are in a valley")

question()

print("\n")
sleep(4)
pkpoint()

print("\n")

print("Ready to keep moving?")
maptwo()

movefive = input("Which way now? ")

if movefive == movefour or moveone:
    print ("You already found all the knowledge in that direction! Choose a new direction ")
elif movethree != movefour or moveone:
    print ("You're back at the house")

movesix = input("Which way? ")

if movesix == "n":
    print ("You are in a village") 
elif movesix == "e":
    print ("You are in a forest")
elif movesix == "w":
    print ("You are by a lake")
elif movesix == "s":
    print ("You are in a valley")
else:
    print ("Pick a new direction!")

question()

print("\n")
sleep(4)
pkpoint()

print("\n")

moveseven = input("Ready to keep moving? Which way? ")

if moveseven == movefour or moveone or movesix:
    print ("You already found all the knowledge in that direction! Choose a new direction ")
elif movethree != movefour or moveone or movesix:
    print ("You're back at the house")

print ("\n")
print ("Someone is comning!")
sleep(3)
voter()

print("\n")
mapthree()
print("\n")
moveeight = input("Which way now? ")
    
if moveeight == "n":
    print ("You are in a village") 
elif moveeight == "e":
    print ("You are in a forest")
elif moveeight == "w":
    print ("You are by a lake")
elif moveeight == "s":
    print ("You are in a valley")
else:
    print ("Pick a new direction!")


question()

print("\n")
sleep(4)
pkpoint()

print("\n")      

print("Wow you've almost completed your quest!")
print ("\n")
notes = input("Want to review your notebook? ")

if notes = "y" or "yes":
    notebook()
else:
    break

print ("This game is a work in progress, so you can't win it yet - sorry! :( Thanks for sticking with it this far! Visit kellydickerson.me to leave feedback")
