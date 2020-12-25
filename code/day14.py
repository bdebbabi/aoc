#2020/12/14 19:43:19
from itertools import  product
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = []
    max_add = 0
    for line in read():
        res = re.match(r"^mask = (\w*)$|^mem\[(\d*)\] = (\d*)$", line.strip()).groups()
        if res[0]:
            mask = res[0]
        if res[1]:
            max_add = max(max_add, int(res[1]))
            input.append([mask, int(res[1]), int(res[2])])
    result = [0]*(max_add+1)
    for mask, add, val in input:
        res = ''
        val = format(val,f'#0{len(mask)+2}b')[2:]
        for m,v in zip(mask,val):
            if m == 'X':
                res+=v 
            else:
                res+=m
        result[add] = int(res,2)
    
    ret(sum(result))

def part2():
    print('Part 2:\n')
    input = []
    max_add = 0
    for line in read():
        res = re.match(r"^mask = (\w*)$|^mem\[(\d*)\] = (\d*)$", line.strip()).groups()
        if res[0]:
            mask = res[0]
        if res[1]:
            max_add = max(max_add, int(res[1]))
            input.append([mask, int(res[1]), int(res[2])])
    result={}
    for mask, add, val in input:
        res = ''
        add = format(add,f'#0{len(mask)+2}b')[2:]
        for m,v in zip(mask,add):
            if m == 'X':
                res+='X' 
            elif m == '0':
                res+=v
            else:
                res+=m
        for p in product('01', repeat = res.count('X')):
            temp = ''
            c = 0
            for a in res:
                if a == 'X':
                    temp+=p[c]
                    c+=1
                else:
                    temp+=a
            result[int(temp,2)] = val
    
    ret(sum(list(result.values())))


if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()