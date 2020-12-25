#2020/12/06 10:46:02
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
    content = next(read(ret_type='str'))
    content = content.split('\n\n')
    n = 0
    for c in content:
        c = c.replace('\n', '')
        n+=len(set(c))
    ret(n)

def part2():
    print('Part 2:\n')
    content = next(read(ret_type='str'))
    content = content.split('\n\n')
    n = 0
    for c in content:
        q = len(c.split('\n'))
        c = c.replace('\n','')
        for a in set(c):
            if c.count(a) == q:
                n += 1
    ret(n)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()