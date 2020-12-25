#2020/12/04 07:11:03
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

 
def get_passports():
    passports = []
    passport = {}
    inputs = list(read())
    for line in inputs:
        line = line.rstrip().split( )
        if not line:
            passports.append(passport)
            passport = {}
        else:
            for item in line:
                k, v = item.split(':')
                passport[k]=v  
    passports.append(passport)

    return passports

def part1():
    print('Part 1:\n')
    valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    n=0
    passports = get_passports()
    for p in passports:
        items =list(p.keys())
        if 'cid' in items:
            items.remove('cid')
        if set(items)==set(valid):
            n+=1  
    ret(n)

def part2():
    print('Part 2:\n')
    
    valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    n=0
    passports = get_passports()
    
    for p in passports:
        items = list(p.keys())
        fields = 0 
        if 'cid' in items:
            items.remove('cid')
        if set(items)==set(valid):
            fields+=1
            if 1920<=int(p['byr'])<=2002: fields+=1
            if 2010<=int(p['iyr'])<=2020: fields+=1
            if 2020<=int(p['eyr'])<=2030: fields+=1
            if ('cm' in p['hgt'] and 150<=int(p['hgt'][0:-2])<=193) or ('in' in p['hgt'] and 59<=int(p['hgt'][0:-2])<=76): fields+=1
            if bool(re.match('#[0-9a-f]{6}', p['hcl'])): fields+=1
            if p['ecl'] in eye: fields+=1
            if bool(re.match('^[0-9]{9}$',p['pid'])): fields+=1
            if fields == 8:
                n+=1  
    ret(n)
    
if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()