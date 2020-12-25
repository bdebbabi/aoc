#2020/12/16 08:20:28
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
    rules = {}
    tickets = []
    for nbr, line in enumerate(read()):
        if nbr <20:
            line = line.split(':')
            intervals = line[1].split(' or ')
            intreval1 = [int(value) for value in intervals[0].split('-')]
            intreval2 = [int(value) for value in intervals[1].split('-')]
            rules[line[0]]=[intreval1, intreval2]
        elif nbr==22:
            my_ticket = [int(value) for value in line.split(',')]
        elif nbr >=25:
            ticket = [int(value) for value in line.split(',')]
            tickets.append(ticket)
    errors = []
    for ticket in tickets:
        for value in ticket:
            found = False
            for rule in list(rules.values()):
                for interval in rule:
                    if value in list(range(interval[0], interval[1]+1)):
                        found = True
                        break
                if found:
                    break
            if not found:
                errors.append(value)
    ret(sum(errors))

def part2():
    print('Part 2:\n')
    rules = {}
    tickets = []
    for nbr, line in enumerate(read()):
        if nbr <20:
            line = line.split(':')
            intervals = line[1].split(' or ')
            intreval1 = [int(value) for value in intervals[0].split('-')]
            intreval2 = [int(value) for value in intervals[1].split('-')]
            rules[line[0]]=[intreval1, intreval2]
        elif nbr==22:
            my_ticket = [int(value) for value in line.split(',')]
        elif nbr >=25:
            ticket = [int(value) for value in line.split(',')]
            tickets.append(ticket)
    errors = []
    new_tickets = []
    for ticket in tickets:
        new_ticket = []
        for value in ticket:
            found = False
            for rule in list(rules.values()):
                for interval in rule:
                    if value in list(range(interval[0], interval[1]+1)):
                        new_ticket.append(value)
                        found = True
                        break
                if found:
                    break
        if len(new_ticket) == 20:
            new_tickets.append(new_ticket)
    new_tickets = np.array(new_tickets)
    rules_pos = {}
    for key, rule in rules.items():
        matched = []
        for i in range(len(new_tickets[0])):
            count = 0
            for value in new_tickets[:,i]:
                if value in list(range(rule[0][0], rule[0][1]+1)) or value in list(range(rule[1][0], rule[1][1]+1)):
                    count +=1
            if count == len(new_tickets):
                matched.append(i)
        rules_pos[key]=matched
    
    matches = []
    res = 1
    for p in sorted(rules_pos, key=lambda l: len(rules_pos[l])):
        for pos in rules_pos[p]:
            if pos not in matches:
                if p.startswith('departure'):
                    res *= my_ticket[pos]
                matches.append(pos)
                break 
    ret(res)
    

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()