from itertools import combinations
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = next(read(ret_type='str')).split('\n')
    p1_deck = [int(card) for card in input[1:26]][::-1]
    p2_deck = [int(card) for card in input[28:]][::-1]
    while p1_deck and p2_deck:
        p1_card, p2_card = p1_deck.pop(), p2_deck.pop()
        if p1_card > p2_card:
            p1_deck = [p2_card, p1_card] + p1_deck
        else:
            p2_deck = [p1_card, p2_card] + p2_deck
    total = 0
    for it, card in enumerate(p1_deck):
        total += (it+1) * card

    ret(total)

def part2():
    print('Part 2:\n')
    input = next(read(ret_type='str')).split('\n')
    p1_deck = [int(card) for card in input[1:26]][::-1]
    p2_deck = [int(card) for card in input[28:]][::-1]
    def rec(p1_deck, p2_deck, game):
        round = 1
        temp_game = game
        p1_decks, p2_decks = [], []
        while p1_deck and p2_deck:
            # print(f'-- Round {round} (Game {game}) --')
            round += 1
            # print("p1_deck: ", p1_deck[::-1])
            # print("p2_deck: ", p2_deck[::-1])
            if p1_deck in p1_decks or p2_deck in p2_decks:
                return 'p1', p1_deck, p2_deck

            p1_decks.append(p1_deck.copy())
            p2_decks.append(p2_deck.copy())

            p1_card, p2_card = p1_deck.pop(), p2_deck.pop()
            # print("p1_card: ", p1_card)
            # print("p2_card: ", p2_card)
            if len(p1_deck)>=p1_card and len(p2_deck)>=p2_card:
                temp_game += 1 
                round_result, _, _ = rec(p1_deck[len(p1_deck)-p1_card:],
                                         p2_deck[len(p2_deck)-p2_card:], 
                                         temp_game)
            else:
                round_result = 'p1' if p1_card > p2_card else 'p2'
            if round_result == 'p1':
                # print(f'player 1 wins round {round} of game {game}!\n')
                p1_deck = [p2_card, p1_card] + p1_deck
            else:
                # print(f'player 2 wins round {round} of game {game}!\n')
                p2_deck = [p1_card, p2_card] + p2_deck
        
        if p1_deck:
            return 'p1', p1_deck, p2_deck
        else:
            return 'p2', p1_deck, p2_deck

    result, p1_deck, p2_deck = rec(p1_deck, p2_deck, 1)
    winner_deck = p1_deck if result=='p1' else p2_deck 
    total = 0
    print(winner_deck)
    for it, card in enumerate(winner_deck):
        total += (it+1) * card

    ret(total)
if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()