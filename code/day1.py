#2020/12/01 13:32:00
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
    for c in combinations(read(1, 'int'),2):
        if sum(c)==2020:
            print(c)
            print(np.product(c))

def part2():
    print('Part 2:\n')
    for c in combinations(read(1, 'int'), 3):
        if sum(c)==2020:
            print(c)
            print(np.product(c))

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()