import pandas as pd
import random
import numpy as np
import statistics

#This assumes Ace is high
DECK = [2,3,4,5,6,7,8,9,10,11,12,13,14]

def colorGuess():
    return 'black'

def upDownGuess(num):
    if num < statistics.median(DECK):
        return 'up'
    elif num > statistics.median(DECK):
        return 'down'
    else:
        choices = ['up', 'down']
        return choices[random.randrange(0,2)]
    
def inOutGuess(num1,num2):
    inside = abs(num1-num2)
    outside = max(DECK) - inside
    if inside > outside:
        return 'in'
    elif inside < outside:
        return 'out'
    else:
        choices = ['in','out']
        return choices[random.randrange(0,2)]

def suiteGuess():
    suites = ['diamonds', 'spades', 'clubs', 'hearts']
    return suites[random.randrange(0, 4)]


