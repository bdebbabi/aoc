#2020/12/15 09:05:54
from itertools import combinations
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from tqdm import tqdm
parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f
def part1():
    print('Part 1:\n')
    input = '0,13,1,8,6,15'
    input = input.split(',')
    numbers = [int(i) for i in input]
    for _ in range(len(numbers), 2020):
        last_number = numbers[-1] 
        indexes = np.where(np.array(numbers)==last_number)[0]
        if len(indexes) > 1:
            numbers.append(indexes[-1] - indexes[-2])
        else:
            numbers.append(0)
    ret(int(numbers[-1]))

def part2():
    print('Part 2:\n')
    input = '0,13,1,8,6,15'
    # input = '2,1,3'
    input = input.split(',')
    numbers = {int(number): [i] for i,number in enumerate(input)}
    last_number = int(input[-1])
    for turn in tqdm(range(len(numbers), 30000000)):
        indexes = numbers[last_number]
        if len(indexes)>1:
            last_number = indexes[-1] - indexes[-2]  
            try:
                numbers[last_number].append(turn)
            except:
                numbers[last_number] = [turn]

        else:
            last_number = 0
            try:
                numbers[0].append(turn)
            except:
                numbers[0] = [turn]
    ret(last_number)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()