import pandas as pd
import random
import numpy as np
import Cards

def getDeck():
    # Ace low for now
    deck = []
    suites = ['diamonds', 'hearts', 'clubs', 'spades']
    for x in range(1, 14):
        for suite in suites:
            deck.append(Cards.card(x, suite))
    random.shuffle(deck)
    return deck

def deck4(deck):
        if len(deck) >= 4:
            play(deck)
        else:
            print('Out of cards')

def play(deck = False):
    win = 0
    lose = 0
    if not deck:
        deck = getDeck()
    print('Color:')
    guess = input()
    first = deck.pop(0)
    if Cards.color(first, guess.lower()):
        print('You have', first.num)
        print('Up or Down: ')
        guess = input()
        second = deck.pop(0)
        if Cards.upDown(first, second, guess.lower()):
            print('You have', first.num,'and', second.num)
            print('In or Out: ')
            guess = input()
            third = deck.pop(0)
            if Cards.inOut(first, second, third, guess.lower()):
                print('You got', third.num)
                print('Suite:')
                guess = input()
                fourth = deck.pop(0)
                if Cards.suite(first, second, third, fourth, guess.lower()):
                    print('Win!')
                    win += 1
                    deck4(deck)
                else:
                    print('You got', fourth.suite)
                    print('Wrong')
                    lose += 1
                    deck4(deck)
            else:
                print('You got', third.num)
                print('Wrong')
                lose += 1
                deck4(deck)
        else:
            print('Wrong, it was', second.num)
            lose += 1
            deck4(deck)
    else:
        print('Wrong, it was:', first.color)
        lose += 1
        deck4(deck)
play()