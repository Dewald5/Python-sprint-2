# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:29:52 2020

@author: Dewald
"""
import random
repeat = "Y"
Dice1 = "-----""\n"" |   |""\n"" | o |""\n"" |   |""\n"" -----"
Dice2 = "-----""\n"" |o  |""\n"" |   |""\n"" |  o|""\n"" -----"
Dice3 = "-----""\n"" |o  |""\n"" | o |""\n"" |  o|""\n"" -----"
Dice4 = "-----""\n"" |o o|""\n"" |   |""\n"" |o o|""\n"" -----"
Dice5 = "-----""\n"" |o o|""\n"" | o |""\n"" |o o|""\n"" -----"
Dice6 = "-----""\n"" |o o|""\n"" |o o|""\n"" |o o|""\n"" -----"
while repeat == "Y":
    repeat  = input("Do you want to play (Y/N)""\n")
    Dice = 0 
    x = 0
    if repeat == "Y":
        rolls = input("How many times do you want to roll the dice""\n")
        for x in range(int(rolls)):
            Dice = random.randint(1,6)
            if Dice == 1:
                print("\n",Dice1,"\n")
            elif Dice == 2:
                print("\n",Dice2,"\n")
            elif Dice == 3:
                print("\n",Dice3,"\n")
            elif Dice == 4:
                print("\n",Dice4,"\n")
            elif Dice == 5:
                print("\n",Dice5,"\n")
            elif Dice == 6:
                print("\n",Dice6,"\n")
    else:
        print("Thanks for playing")