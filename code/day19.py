from itertools import combinations
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from pprint import pprint
import re
parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    def rec(rule_nbr, t):
        rule = rules[rule_nbr]
        if '"' in rule:
            res = rule.replace('"','')
        else: 
            res = ''
            t+=1
            for r in rule.split(' '):
                if r == '|':
                    res += '|'
                else:
                    res += rec(int(r), t)
        res = f'({res})'
        return res

    input =  list(read())
    rules  = {int(line.split(':')[0]): line.split(':')[1].strip() for line in input[0:136]}
    messages = input[137:]
    rule0 = rec(0, 1)
    n = 0
    for message in messages:
        if re.match(rule0, message) and re.match(rule0, message).group(0) == message:
            n+=1
    ret(n)

def part2():
    print('Part 2:\n')
    def rec(rule_nbr, t):
        rule = rules[rule_nbr]
        if '"' in rule:
            res = rule.replace('"','')
        else: 
            res = ''
            t+=1
            for r in rule.split(' '):
                if r == '|':
                    res += '|'
                else:
                    res += rec(int(r), t)
        res = f'({res})'
        return res

    input =  list(read())
    rules  = {int(line.split(':')[0]): line.split(':')[1].strip() for line in input[0:136]}
    messages = input[137:]
    rules[8]='42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42'
    rules[11]='42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31'
    rule0 = rec(0, 1)
    n = 0
    for message in messages:
        if re.match(rule0, message) and re.match(rule0, message).group(0) == message:
            n+=1
    ret(n)
if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()