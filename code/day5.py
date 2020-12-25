#2020/12/05 09:16:14
from itertools import combinations
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from math import  floor, ceil

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def get_id(string):
    row = dicho(string[0:7], 128)
    col = dicho(string[7:], 7)
    id = row *8 + col
    return id
    
def dicho(string, max):
    a = 0
    b = max
    for s in string:
        t = (a+b)/2
        if s in['F', 'L']:
            b = floor(t)
        elif s in ['B', 'R']:
            a = ceil(t)
    return a


def part1():
    print('Part 1:\n')
    ids = []
    for line in read():
        ids.append(get_id(line))
    max = np.max(np.array(ids))
    ret(int(max))

def part2():
    print('Part 2:\n')
    ids = []
    for line in read():
        ids.append(get_id(line))
    for id in range(np.min(ids), np.max(ids)):
        if id not in ids:
            ret(int(id))

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()