from itertools import combinations
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from collections import deque
from tqdm import tqdm
parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = 398254716
    cups = [int(n) for n in str(input)]
    current_cup_idx = 0
    for it in range(100):
        print(f'-- move {it+1} --')
        picked_cups = []
        print(f"cups: {cups}")
        print(f'current index label: {cups[current_cup_idx]}')

        for cup_idx in range(current_cup_idx+1, current_cup_idx+4):
            picked_cups.append(cups[cup_idx%9])
            cups[cup_idx%9] = 0

        print(f"pick up: {picked_cups}")
        
        dest_label = cups[current_cup_idx] - 1
        while dest_label in picked_cups or dest_label <= 0:
            dest_label -= 1
            if dest_label <= 0:
                dest_label = 9
                while dest_label in picked_cups:
                    dest_label-=1
        dest_idx = cups.index(dest_label)
        
        print(f'destination: {cups[dest_idx]}\n')
        cups = cups[:dest_idx+1] + picked_cups + cups[dest_idx+1:]
        if current_cup_idx > dest_idx:
            cups = deque(cups)
            cups.rotate(-3)
            cups = list(cups)
        cups = [cup for cup in cups if cup!=0]
        current_cup_idx = (current_cup_idx+1)%9 
    split_idx = cups.index(1)
    res = cups[split_idx+1:] + cups[:split_idx]
    s = ''
    for r in res:
        s+= str(r)
    ret(s)

def part2():
    print('Part 2:\n')
    N = 10000000
    size = 1000000 
    input = 398254716
    input = [int(n) for n in str(input)]
    for cup in range(10, 1000001):
        input.append(cup)
    cups = [0]*(size+1)
    for it, cup in enumerate(input):
        if it+1 == len(input):
            cups[cup] = input[0]
        else:
            cups[cup] = input[it+1]
    current_cup = input[0]
    for it in tqdm(range(N)):
        # print(f'-- move {it+1} --')
        # print(f"cups: {cups}")
        # print(f'current index label: {current_cup}')
        picked_cups = []
        next_cup = cups[current_cup]
        for _ in range(3):
            picked_cups.append(next_cup)
            next_cup = cups[next_cup]
        # print(f"pick up: {picked_cups}")

        dest_label = current_cup - 1
        while dest_label in picked_cups or dest_label <= 0:
            dest_label -= 1
            if dest_label <= 0:
                dest_label = size
                while dest_label in picked_cups:
                    dest_label-=1
        # print(f'destination: {dest_label}\n')
        cups[current_cup] = cups[picked_cups[2]]
        cups[picked_cups[2]] = cups[dest_label]
        cups[dest_label] = picked_cups[0]
        current_cup = cups[current_cup]
    ret(cups[1]*cups[cups[1]])


if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()