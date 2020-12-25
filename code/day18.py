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
    class T:
        def __init__(self, v):
            self.v = v 
        def __add__(self, other):
            return T(self.v+other.v)
        def __sub__(self, other):
            return T(self.v*other.v)
        def __mul__(self, other):
            return T(self.v*other.v)
    t = 0
    for line in read():
        line = line.replace('*', '-')
        for i in range(10):
            line = line.replace(f'{i}', f'T({i})')
        t+=eval(line).v

    ret(t)

def part2():
    print('Part 2:\n')
    class T:
        def __init__(self, v):
            self.v = v 
        def __add__(self, other):
            return T(self.v+other.v)
        def __sub__(self, other):
            return T(self.v*other.v)
        def __mul__(self, other):
            return T(self.v+other.v)
    t = 0
    for line in read():
        line = line.replace('*', '-')
        line = line.replace('+', '*')

        for i in range(10):
            line = line.replace(f'{i}', f'T({i})')
        t+=eval(line).v

    ret(t)


if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()