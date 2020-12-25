#2020/12/11 17:08:45
from itertools import combinations, product
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
    input = next(read(ret_type='str'))
    input = [list(i) for i in input.split('\n')]
    input = np.array(input) 
    l,w = input.shape
    temp_input = np.full((l,w), '.')
    while (input!=temp_input).any():
        temp_input = input.copy()
        for i, j in product(range(l), range(w)):
            neighbours = temp_input[max(i-1,0):min(i+2,l),
                            max(j-1,0):min(j+2,w)]
            neighbours = list(neighbours.reshape(-1,))
            neighbours.remove(temp_input[i,j])
            if temp_input[i,j] == "L" and neighbours.count("#") == 0:
                input[i,j] = "#"
            elif temp_input[i,j] == "#" and neighbours.count("#")>=4:
                input[i,j] = "L"
    
    ret(int(np.sum(input=="#")))

def part2():
    print('Part 2:\n')
    def directions(i,j,input,l,w):
        yield input[i,j+1:]#right
        yield input[i,:j][::-1]#left
        yield input[i+1:,j]#down
        yield input[:i,j][::-1]#up
        yield [input[id,jd] for id, jd in zip(range(i+1,l), range(j+1,w))]#down right
        yield [input[id,jd] for id, jd in zip(range(i-1,-1,-1), range(j-1,-1,-1))]#up left
        yield [input[id,jd] for id, jd in zip(range(i-1,-1,-1), range(j+1,w))]#up right
        yield [input[id,jd] for id, jd in zip(range(i+1,l), range(j-1,-1,-1))]#down left

    input = next(read(ret_type='str'))
    input = [list(i) for i in input.split('\n')]
    input = np.array(input) 
    l,w = input.shape
    temp_input = np.full((l,w), '.')
    count = 0
    while (input!=temp_input).any():
        count += 1 
        temp_input = input.copy()
        for i, j in product(range(l), range(w)):
            neighbours = []
            for direction in directions(i,j,temp_input,l,w):
                neighbours.append(next((s for s in direction if s in ['L','#']),'.'))
            if temp_input[i,j] == "L" and neighbours.count("#") == 0:
                input[i,j] = "#"
            elif temp_input[i,j] == "#" and neighbours.count("#")>=5:
                input[i,j] = "L"
    ret(int(np.sum(input=="#")))

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()