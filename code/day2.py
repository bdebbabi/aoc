#2020/12/02 08:18:57
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
    n = 0
    for line in read(2):
        line = line.split(' ')
        min, max = line[0].split('-')
        letter = line[1][0]
        password = line[2]
        if int(min) <= password.count(letter)<= int(max):
            n+=1
    ret(n)

def part2():
    print('Part 2:\n')
    n = 0
    for line in read(2):
        line = line.split(' ')
        f, s = line[0].split('-')
        f = int(f) -1
        s = int(s) - 1
        letter = line[1][0]
        password = line[2]
        if (password[f]==letter) ^ (password[s]==letter):    
            n+=1
    ret(n)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()