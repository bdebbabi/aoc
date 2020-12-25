#2020/12/09 08:15:10
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
    input = list(read(ret_type='int'))
    base  = input[0:25]
    for i in input[25:]:
        sums = [sum(a) for (a) in combinations(base, 2)]
        if i not in sums:
            ret(i)
        base.pop(0)
        base.append(i)


def part2():
    print('Part 2:\n')
    def chunks(lst, n):
        for i in range(0, len(lst)):
            if i+n <= len(lst):
                yield lst[i:i + n]

    input = list(read(ret_type='int'))
    length = 2
    while True and length != len(input):
        for c in chunks(input, length):
            if sum(c) == 776203571 and len(c)==length:
                ret(max(c)+min(c))
            
        length += 1

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()