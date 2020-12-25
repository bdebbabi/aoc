#2020/12/08 11:48:37
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
    input = next(read(ret_type='str'))
    commands = [[l[0:3], int(l[3:])]for l in input.split('\n')]
    path = [0]*len(commands)
    pos = 0
    acc = 0
    while 2 not in set(path):
        last_acc = acc
        action, nbr = commands[pos]
        path[pos] += 1
        if action=="acc":
            acc += nbr
            pos += 1
        elif action=='jmp':
            pos += nbr
        elif action=='nop':
            pos += 1

    
    ret(last_acc)

def part2():
    print('Part 2:\n')
    input = next(read(ret_type='str'))
    commands = [[l[0:3], int(l[3:])]for l in input.split('\n')]
    def run(commands):
        acc = 0
        pos = 0 
        path = [0]*len(commands)
        while 2 not in set(path):
            last_acc = acc
            action, nbr = commands[pos]
            path[pos] += 1
            if action=="acc":
                acc += nbr
                pos += 1
            elif action=='jmp':
                pos += nbr
            elif action=='nop':
                pos += 1
            if pos+1>=len(commands):
                ret(last_acc)
                break

    for i, command in enumerate(commands):
        com = commands.copy()
        if command[0] == "nop":
            com[i] = ["jmp", command[1]]
            run(com)
        elif command[0] == "jmp":
            com[i] = ["nop", command[1]]
            run(com)
        else:
            pass    

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()