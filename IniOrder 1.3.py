from imghdr import what
from operator import truediv
from tkinter import E
from types import new_class
from typing import Text
import time
import random
import os





loop = 1
x = 1
names = []
iniorder = []
hitpoint = []
armourclass = []
#how many are playing?
print("do you want IOC to keep track of your stats like HP and AC? (y/n)")
while True:
    yorn = input()
    if(yorn == 'y'):
        print("alrighty! You can see these stats by typing in 'HP' or 'AC' when prompted if you would like to take any action")
        break
    elif(yorn == 'n'):
        print("Okay IOC will not track your stats")
        break
    else:
        print("that is not a y or an n")
print("how many people are you putting in for IniOrder?")
howmanyinorderSTR = input()
howmanyinorder = int(howmanyinorderSTR)
#gaining stats
print("You will type in the name of the character and their initiative roll")
while (loop == 1):
    name = "default"
    name = input("name  ")
    names.append(name) 
    inirolld = 10
    inirolld = input("roll  ")
    iniroll = int(inirolld)
    iniorder.append(iniroll)
    if(yorn == 'y'):
        hpc = input("put in the characters HP  ")
        hp = int(hpc)
        hitpoint.append(hp)
        acc = input("put in this characters AC  ")
        ac = int(acc)
        armourclass.append(ac)

    x = x + 1
    if(x > howmanyinorder):
        break
#sorting the characters into proper order
order2 = iniorder
order3 = order2
display = [names for (iniorder,names) in sorted(zip(iniorder,names), key=lambda pair: pair[0])]
HPordered = [hitpoint for (order2, hitpoint) in sorted(zip(order2,hitpoint), key=lambda pair: pair[0])]
ACordered = [armourclass for (order3, armourclass) in sorted(zip(order3,armourclass), key=lambda pair: pair[0])]
display.reverse()
HPordered.reverse()
ACordered.reverse()
#print(HPordered)
#print(ACordered)
print("type 'done' when combat is over, other wise hit enter to move to the next in initiative order")
c = 0
#displaying the characters
while (loop == 1):
    buffername = display[c]
    display[c] = "[" + display[c]
    for q in display:
        print(q)
    display[c] = buffername
    action = input("any action? ")
    if(action == "done"):
        break
    elif(action == 'HP' and yorn == 'y'):
        print(display[c], " has an hp of ", HPordered[c])
    elif(action == 'AC' and yorn == 'y'):
        print(display[c], "'s AC is ", ACordered[c])    
    elif(action == 'lower HP' and yorn == 'y'):
        tolower = 0
        text = 'how much would you like to lower ' + display[c] + "'s hp by?  "
        lower = input(text)
        tolower = int(lower)
        HPordered[c] = HPordered[c] - tolower
        print(display[c], " now has an HP of ", HPordered[c])
    elif(action == "raise HP" and yorn == 'y'):
        toraise = 0
        text2 = 'how much would you like to raise ' + display[c] + "'s hp by?  "
        traise = input(text2)
        toraise = int(traise)
        HPordered[c] = HPordered[c] + toraise
        print(display[c], " now has an HP of ", HPordered[c])
    elif(action == ''):
        c = c + 1
        if(c > howmanyinorder - 1):
            c = 0
        continue
    
print("You are now done combat, congrats if you won")
time.sleep(3)