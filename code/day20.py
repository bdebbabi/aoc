from itertools import permutations, product
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from pprint import pprint
import re
np.set_printoptions(threshold=200000)

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = next(read(ret_type='str'))
    input = input.split('\n\n')
    input = {int(i.split(':')[0][5:]):np.array([[l for l in e] for e in i.split(':')[1][1:].split('\n')]) for i in input}
    
    neighbours = {key: 0 for key in input.keys()}
    corners = [3121, 1889, 1187, 1789]

    for tile_nbr, neighbour_nbr in permutations(list(input.keys()),2):
        tile, neighbour = input[tile_nbr], input[neighbour_nbr]
        for tile_edge, neighbour_edge in product([tile[0,:], tile[-1,:], tile[:,0],tile[:,-1]],
            [neighbour[0,:], neighbour[-1,:], neighbour[:,0],neighbour[:,-1]]):
            if (tile_edge == neighbour_edge).all() or (tile_edge[::-1] == neighbour_edge).all():
                if tile_nbr in corners:
                    print(tile_nbr, neighbour_nbr, tile_edge, neighbour_edge)
                    print(tile, neighbour)
                neighbours[tile_nbr]+=1
    res = 1
    for k,v in neighbours.items():
        if v == 2:
            res *= k

    ret(res)

def part2():
    print('Part 2:\n')
    input = next(read(ret_type='str'))
    input = input.split('\n\n')
    input = {int(i.split(':')[0][5:]):np.array([[l for l in e] for e in i.split(':')[1][1:].split('\n')]) for i in input}
    
    neighbours = {key: [] for key in input.keys()}
    corners = [3121, 1889, 1187, 1789]
    for tile_nbr, neighbour_nbr in permutations(list(input.keys()),2):
        tile, neighbour = input[tile_nbr], input[neighbour_nbr]
        for it, (tile_edge, neighbour_edge) in enumerate(product([tile[0,:], tile[-1,:], tile[:,0],tile[:,-1]],
            [neighbour[0,:], neighbour[-1,:], neighbour[:,0],neighbour[:,-1]])):
            if (tile_edge == neighbour_edge).all():
                neighbours[tile_nbr].append([neighbour_nbr])
            elif (tile_edge[::-1] == neighbour_edge).all():
                neighbours[tile_nbr].append([neighbour_nbr])
    size = int(np.sqrt(len(input))) * 10
    puzzle = np.full((size, size), ' ')
    start =  np.rot90(np.flipud(np.fliplr(input[corners[0]])),3)
    puzzle[0:10, 0:10] = start
    assigned_tiles = []
    assigned_tiles.append(corners[0])
    for it in range(11):
        found = False
        current_tile = puzzle[10*it: 10*(it+1), 0:10]
        it +=1 
        edge = current_tile[-1,:]
        for tile_nbr, tile in input.items():
            if tile_nbr not in assigned_tiles:
                for rotation in [0,1,2,3]:
                    temp_tile = np.rot90(tile, rotation)
                    if (temp_tile[0,:] == edge).all():
                        puzzle[10*it: 10*(it+1), 0:10] = temp_tile
                        found = True
                        break
                    elif (np.fliplr(temp_tile)[0,:]==edge).all():
                        puzzle[10*it: 10*(it+1), 0:10] = np.fliplr(temp_tile)
                        found = True
                        break
                    elif (np.flipud(temp_tile)[0,:]==edge).all():
                        puzzle[10*it: 10*(it+1), 0:10] = np.flipud(temp_tile)
                        found = True
                        break
            if found:
                assigned_tiles.append(tile_nbr)
                break
    for row in range(12):
        for col in range(11):
            found = False
            current_tile = puzzle[10*row: 10*(row+1), 10*col:10*(col+1)]
            col +=1 
            edge = current_tile[:,-1]
            for tile_nbr, tile in input.items():
                if tile_nbr not in assigned_tiles:
                    for rotation in [0,1,2,3]:
                        temp_tile = np.rot90(tile, rotation)
                        if (temp_tile[:,0] == edge).all():
                            puzzle[10*row: 10*(row+1), 10*col:10*(col+1)] = temp_tile
                            found = True
                            break
                        elif (np.fliplr(temp_tile)[:,0]==edge).all():
                            puzzle[10*row: 10*(row+1), 10*col:10*(col+1)] = np.fliplr(temp_tile)
                            found = True
                            break
                        elif (np.flipud(temp_tile)[:,0]==edge).all():
                            puzzle[10*row: 10*(row+1), 10*col:10*(col+1)] = np.flipud(temp_tile)
                            found = True
                            break
                    if found:
                        assigned_tiles.append(tile_nbr)
                        break
    pad = list(range(0,121,10))
    pad += [i-1 for i in pad]
    pad.remove(-1)
    pad.remove(120)
    puzzle = np.delete(puzzle, pad, 0)
    puzzle = np.delete(puzzle, pad, 1)
    temp_puzzle = puzzle
    max_matches = 0
    for rotation in [0,1,2,3]:
        puzzle = np.rot90(temp_puzzle, rotation)
        for puzz in [puzzle, np.fliplr(puzzle), np.flipud(puzzle)]:
            puzz = '\n'.join(''.join(x for x in y) for y in puzz)
            count_hash = puzz.count('#')
            puzz = puzz.split('\n')
            matches = 0
            for it, line in enumerate(puzz):
                for pos, c in enumerate(line):
                    if c == '#' and 18 < pos+1 < len(line) and it <= len(puzz)-2:
                        if re.match('#....##....##....###.+', puzz[it+1][pos-18:]):
                            if re.match('.#..#..#..#..#..#....+', puzz[it+2][pos-18:]):
                                matches +=1
            max_matches = max(matches, max_matches)
    ret(count_hash - max_matches*15)

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()