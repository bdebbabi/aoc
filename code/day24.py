from itertools import combinations, product
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
import re 
from tqdm import tqdm 
parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = next(read(ret_type='str')).split('\n')
    directions = []
    for line in input:
        path = []        
        direction = re.findall('(se)|(sw)|(ne)|(nw)|(w)|(e)', line)
        for dir in direction:
            for d in dir:
                if d : path.append(d)
        directions.append(path)

    positions = {}

    for direction in directions:
        pos = 0j+0
        for d in direction:
            if d=='w':
                pos -= 1
            elif d=='e':
                pos += 1
            elif d=='sw':
                pos += 1j-1
            elif d=='se':
                pos += 1j
            elif d=='nw':
                pos += -1j
            elif d =='ne':
                pos += -1j+1
        if pos in positions:
            positions[pos] +=1
        else:
            positions[pos] = 1
    black, white = 0, 0
    for position, nbr in positions.items():
        if nbr>2: print(nbr)
        if nbr%2 == 0:
            white+=1
        elif nbr == 1:
            black+=1
    ret(black)

def part2():
    print('Part 2:\n')
    input = next(read(ret_type='str')).split('\n')
    directions = []
    for line in input:
        path = []        
        direction = re.findall('(se)|(sw)|(ne)|(nw)|(w)|(e)', line)
        for dir in direction:
            for d in dir:
                if d : path.append(d)
        directions.append(path)

    positions = {}

    for direction in directions:
        pos = 0j+0
        for d in direction:
            if d=='w':
                pos -= 1
            elif d=='e':
                pos += 1
            elif d=='sw':
                pos += 1j-1
            elif d=='se':
                pos += 1j
            elif d=='nw':
                pos += -1j
            elif d =='ne':
                pos += -1j+1
        if pos in positions:
            positions[pos] +=1
        else:
            positions[pos] = 1
    
    black = []
    for position, nbr in positions.items():
        if nbr == 1:
            black.append(position)

    positions = list(positions.keys())
    real_max = int(np.abs(max(positions, key=lambda x: np.abs(x.real)).real))
    imag_max = int(np.abs(max(positions, key=lambda x: np.abs(x.imag)).imag))
    tiles = {}
    colors = {}
    limits = [119,120,121,-119,-120,-121]
    # limits = [104,105,-104,-105]
    for i, j  in product(range(-real_max-101, real_max+102), range(-imag_max-101, imag_max+102)):
        tile = complex(i,j)
        tiles[tile] = [complex(i,j-1), 
                        complex(i+1,j-1),
                        complex(i+1,j),
                        complex(i,j+1),
                        complex(i-1,j+1),
                        complex(i-1,j)]
        if i in limits or j in limits:
            colors[complex(i,j-1)] = 'white'
            colors[complex(i+1,j-1)] = 'white'
            colors[complex(i+1,j)] = 'white'
            colors[complex(i,j+1)] = 'white'
            colors[complex(i-1,j+1)] = 'white'
            colors[complex(i-1,j)] = 'white'
        if tile in black:
            colors[tile]='black'
        else:
            colors[tile]='white'
    temp_colors = colors.copy()
    for it in tqdm(range(100)):
        for tile, neighbours in tiles.items():
            black_neigbours = 0
            for neighbour in neighbours:
                if colors[neighbour] == 'black': black_neigbours+=1
            if colors[tile]=="black" and (black_neigbours==0 or black_neigbours>2):
                temp_colors[tile]="white"
            elif colors[tile]=="white" and black_neigbours == 2:
                temp_colors[tile]="black"
        # print(temp_black)
        colors = temp_colors.copy()
        # print(f'Day {it+1}: {res}')
    res= 0
    for k,v in colors.items():
        if v=='black':
            res+=1
    
    
    ret(res)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()