from imghdr import what
from tkinter import E
from types import new_class
from typing import Text
import time
import random
import os

loop = 1
x = 1
names = []
#iniorder = []
print("how many people are you putting in for IniOrder?")
howmanyinorderSTR = input()
howmanyinorder = int(howmanyinorderSTR)
#print(howmanyinorder)
print("just a reminder, input your characters from highest to lowest Iniative")
print("what is the name of the person you'd like to add to IO")
while (loop == 1):
    name = "default"
    name = input()
    names.append(name)
    x = x + 1
    if(x > howmanyinorder):
        break
print("you now are adding ", names, " to the IO")
    #x = 1
    #while (loop == 1):
    #    print("now ")

    #Now putting out the IO
print("type 'done' when combat is over, and 'next' to move to the next in IO")
c = 0

while (loop == 1):
    buffername = names[c]
    names[c] = "[" + names[c]
#    nametp = names[c]
#    c = c + 1
#    #print(c)
    for q in names:
        print(q)
    names[c] = buffername
    c = c + 1
    if(c > howmanyinorder - 1):
        c = 0
    action = input("any action? ")
    if(action == "done"):
        break
    elif(action == "next"):
        print("continuing")
        continue
    
print("You are now done combat, congrats if you won")
time.sleep(3)
    
