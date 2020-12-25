#2020/12/03 09:05:53
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
    lines = list(read())
    n = 0
    row = 0
    col = 0
    width = len(lines[0])

    while row < len(lines):
        if lines[row][col] == '#':
            n +=1     
        row += 1
        col = (col+3)%width
    
    ret(n)

def part2():
    print('Part 2:\n')

    lines = list(read())
    res = 1
    width = len(lines[0])

    paths = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    for r, c in paths:
        n = 0
        row = 0
        col = 0
        while row < len(lines):
            if lines[row][col] == '#':
                n +=1     
            row = row + r
            col = (col+c)%width
        res = res * n

    ret(res)
    
if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()