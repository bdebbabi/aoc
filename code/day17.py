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
    input = next(read(17, ret_type='str'))
    input = [list(i) for i in input.split('\n')]
    input = np.array(input) 
    h,w = input.shape
    H = h+2*6
    W = w+2*6
    Z = 13
    cube = np.full((Z,H,W), '.')
    cube[6,6:6+h, 6:6+w] = input
    temp_cube = np.full((Z,H,W), '.')
    for it in range(6):
        temp_cube = cube.copy()
        for i, j, z in product(range(H), range(W), range(Z)):
            neighbours = []
            for l in range(max(0,z-1), min(z+2,Z)):
                temp_neighbours = temp_cube[l, max(i-1,0):min(i+2,H),
                                max(j-1,0):min(j+2,W)]
                neighbours += list(temp_neighbours.reshape(-1,))
                
            neighbours.remove(temp_cube[z,i,j])
            
            if temp_cube[z,i,j] == "#" and 2 <= neighbours.count("#")<=3 :
                cube[z,i,j] = "#"
            elif temp_cube[z,i,j] == "." and neighbours.count("#")==3:
                cube[z,i,j] = "#"
            else:
                cube[z,i,j] = "."

    ret(int(np.sum(cube=="#")))

def part2():
    print('Part 2:\n')
    input = next(read(17, ret_type='str'))
    input = [list(i) for i in input.split('\n')]
    input = np.array(input) 
    h,w = input.shape
    H = h+2*6
    W = w+2*6
    Z = 13
    M = 13
    cube = np.full((M,Z,H,W), '.')
    cube[6,6,6:6+h, 6:6+w] = input
    temp_cube = np.full((M,Z,H,W), '.')
    for it in range(6):
        temp_cube = cube.copy()
        for i, j, z, m in product(range(H), range(W), range(Z), range(M)):
            neighbours = []
            for l, q in product(range(max(0,z-1), min(z+2,Z)), range(max(0,m-1), min(m+2,M))):
                temp_neighbours = temp_cube[q, l, max(i-1,0):min(i+2,H),
                                max(j-1,0):min(j+2,W)]
                neighbours += list(temp_neighbours.reshape(-1,))
                
            neighbours.remove(temp_cube[m,z,i,j])
            
            if temp_cube[m,z,i,j] == "#" and 2 <= neighbours.count("#")<=3 :
                cube[m,z,i,j] = "#"
            elif temp_cube[m,z,i,j] == "." and neighbours.count("#")==3:
                cube[m,z,i,j] = "#"
            else:
                cube[m,z,i,j] = "."

    ret(int(np.sum(cube=="#")))

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()