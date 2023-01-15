#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:08:40 2021
Updated on Sun Jan 15 2023

This applications take a user input of dice rolls and dipslays on a bar graph the 
frequency of rolls for each number
@author: terrydennison
"""
import matplotlib.pyplot as plt
import numpy as np

#User input of the number of times to roll the dice
val = int(input('Please enter value: '))

#Function that takes user input and calculates dices rolls
def func():

    num_of_updates = val
    
    #List to dispaly x lables of dice faes
    diceNum = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
    
    #counter
    k = 0
    
    #Conditional statement to check if k == user entry value
    #If not k will increment by 1
    while k != num_of_updates:

        roller = np.random.randint(1, 7, 1)

        for i in roller:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        rollFreq = [dic[i] for i in sorted(dic.keys())]

        k += 1
    
    #Displays the statistcal values above the bars face value
    for i in range(len(rollFreq)):
        plt.text(
            i, rollFreq[i], f'{(rollFreq[i]/num_of_updates)*100:.1f}%\n', color='k', ha='center')
    for i in range(len(rollFreq)):
        plt.text(i, rollFreq[i], f'{rollFreq[i]}\n\n', color='k', ha='center')
    plt.xlabel("Dice Number")
    plt.ylabel('Frequencies')

    plt.bar(diceNum, rollFreq, color=['r', 'g', 'k', 'y', 'c', 'b'])
    plt.ylim(1, (250))
    plt.title(str(num_of_updates) + ' Dice Rolls')
    plt.show()


dic = {}

func()
