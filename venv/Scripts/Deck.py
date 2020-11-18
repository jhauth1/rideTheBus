import pandas as pd
import random
import numpy as np
import Cards
from statistics import mean
import naiveAI as AI

def getDeck():
    # Ace low for now
    deck = []
    suites = ['diamonds', 'hearts', 'clubs', 'spades']
    for x in range(2, 15):
        for y, suite in enumerate(suites):
            card = Cards.card(x, suite)
            deck.append(card)
    random.shuffle(deck)
    return deck

def deck4(deck):
        if len(deck) >= 4:
             return play(deck)
        else:
            return 0

def play(deck = False):
    score = 0
    if not deck:
        deck = getDeck()
    guess = AI.colorGuess()
    first = deck.pop(0)
    if Cards.color(first, guess):
        guess = AI.upDownGuess(first.num)
        second = deck.pop(0)
        if Cards.upDown(first, second, guess):
            guess = AI.inOutGuess(first.num, second.num)
            third = deck.pop(0)
            if Cards.inOut(first, second, third, guess):
                guess = AI.suiteGuess()
                fourth = deck.pop(0)
                # Placeholder in case I want to keep this if
                if Cards.suite(first, second, third, fourth, guess):
                    score += 0
                else:
                    score -= 1
                    score += deck4(deck)
            else:
                score -= 1
                score += deck4(deck)
        else:
            score -= 1
            score += deck4(deck)
    else:
        score -= 1
        score += deck4(deck)
    return score