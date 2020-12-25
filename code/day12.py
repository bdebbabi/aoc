#2020/12/12 09:02:47
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
    def change_direction(angle):
        directions = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W'
        }
        return directions[angle]

    direction = 'E'
    NS = 0
    WE = 0
    angle = {
        'N':0,
        'E':90,
        'S':180,
        'W':270
    }
    for line in read():
        action  = line[0]
        value = int(line[1:])
        current_angle = angle[direction]
        if action == 'N' or (action == 'F' and direction == 'N'):
            NS += value
        elif action == 'S' or (action == 'F' and direction == 'S'):
            NS += -value
        elif action == 'E' or (action == 'F' and direction == 'E'):
            WE += value
        elif action == 'W' or (action == 'F' and direction == 'W'):
            WE += -value
        elif action == 'R':
            current_angle = (current_angle + value)% 360
            direction = change_direction(current_angle)
        elif action == 'L':
            current_angle = (current_angle - value + 360)% 360
            direction = change_direction(current_angle)
        
    ret(abs(NS)+abs(WE))

def part2():
    print('Part 2:\n')
    waypointNS = 1
    waypointWE = 10
    shipNS = 0
    shipWE = 0
    for line in read():
        action  = line[0]
        value = int(line[1:])    
        if action == 'N':
            waypointNS += value
        elif action == 'S':
            waypointNS += -value
        elif action == 'E':
            waypointWE += value
        elif action == 'W':
            waypointWE += -value
        elif action == 'F':
            shipNS += waypointNS*value
            shipWE += waypointWE*value
        elif action == 'R':
            if value == 90:
                waypointNS, waypointWE = -waypointWE, waypointNS
            elif value == 180:
                waypointNS, waypointWE = -waypointNS, -waypointWE
            elif value == 270:
                waypointNS, waypointWE = waypointWE, -waypointNS
        elif action == 'L':
            if value == 90:
                waypointNS, waypointWE = waypointWE, -waypointNS
            elif value == 180:
                waypointNS, waypointWE = -waypointNS, -waypointWE
            elif value == 270:
                waypointNS, waypointWE = -waypointWE, waypointNS
        
    ret(abs(shipNS)+abs(shipWE))


if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()