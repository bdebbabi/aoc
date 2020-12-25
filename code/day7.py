#2020/12/07 09:43:49
from itertools import combinations
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
def first(sentence):
    s = sentence.split()
    return s[0] + ' ' + s[1]

def contents(sentence):
    s = sentence.split(',')
    first = s[0].split()
    container = first[0] + ' ' + first[1]
    if "no other bags" in s[0]:
        return {container:{}}

    contents = {}
    contents.update({first[5]+ ' '+ first[6]:int(first[4])})
    for content in s[1:]:
        content = content.strip().split()
        contents.update({content[1]+ ' '+ content[2]:int(content[0])})
    return {container:contents}

def part1():
    print('Part 1:\n')
    content = next(read(ret_type='str'))
    content = content.replace('\n','')
    content = content.split('.')
    n = 0
    bags = []
    my_bag = 'shiny gold'
    for sent in content:
        if my_bag in sent and first(sent) != my_bag:
            bags.append(first(sent))
            n += 1
    second_bags = []
  
    l = len(set(bags))
    old_l = 0
    while old_l!=l:
        old_l=l
        for sent in content:
            for bag in bags:
                if bag in sent and first(sent) != bag:
                    bags.append(first(sent))
                    second_bags.append(first(sent))
                    n += 1
        l = len(set(bags))
        
    ret(l)

         

def part2():
    print('Part 2:\n')

    content = next(read(ret_type='str'))
    content = content.replace('\n','')
    content = content.split('.')
    bags = {}

    for sent in content[:-1]:
        bags.update(contents(sent))

    def rec(bag):
        return 1 + sum(rec(k)*v for k,v in bags[bag].items())
    
    ret(rec('shiny gold')-1)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()