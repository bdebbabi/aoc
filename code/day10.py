#2020/12/10 08:52:04
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
    input = sorted(input)
    battery = 0
    diff1 = 0
    diff3 = 0
    for i in input:
        print(battery, i)
        if i - battery == 1:
            diff1 += 1
        elif i - battery == 3:
            diff3 += 1
        elif (i - battery > 3) or (i - battery <=0):
            print('error')
        else: 
            pass
        battery = i
    diff3 += 1
    ret(diff1*diff3)


def part2():
    print('Part 2:\n')
    input = list(read(ret_type='int'))

    input = sorted(input)

    res = [0]*(input[-1]+1)
    res[0] = 1
    for i in input:
        res[i] = res[i-3] + res[i-2] + res[i-1]
    ret(res[-1])


if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()