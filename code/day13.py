#2020/12/13 12:09:11
from itertools import count
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
import time
from tqdm import tqdm 

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f

def part1():
    print('Part 1:\n')
    input = list(read())
    timestamp = int(input[0])
    ids = [int(id) for id in input[1].split(',') if id != 'x']
    minutes = []
    for id in ids:
        if timestamp % id == 0:
            ret(0)
            break
        minute = id * ((timestamp//id)+1) - timestamp
        minutes.append(minute)
    print(ids)
    print(minutes)
    ret(min(minutes) * ids[np.argmin(minutes)])

def part2():
    print('Part 2:\n')
    # input = list(read())
    # start_time = time.time()
    # ids = {int(id):t for t, id in enumerate(input[1].split(',')) if id != 'x'}
    # max_id = max(list(ids.keys()))
    # max_id_t = ids[max_id]
    # ids = {id:t-max_id_t for id, t in ids.items()}
    # timestamp = 0
    # step = 1000
    # while True:
    #     if timestamp // step > 1:
    #         print(f"{timestamp} ({len(str(timestamp))})")
    #         step *= 10
    #     timestamp += max_id
    #     count = len(ids)  
    #     for id, t in ids.items():
    #         if (timestamp + t)%id != 0: 
    #             break
    #         count -= 1
    #     if count == 0:
    #         ret(timestamp-max_id_t)
    #         break
    # print("--- %s seconds ---" % (time.time() - start_time))

    #Chinese remainder algo 
    def mul_inv(a, b):
        b0= b
        x0, x1= 0,1
        if b== 1: return 1
        while a>1 :
            q=a// b
            a, b= b, a%b
            x0, x1=x1 -q *x0, x0
        if x1<0 : x1+= b0
        return x1
    
    input = list(read())
    ids = {int(id):t for t, id in enumerate(input[1].split(',')) if id != 'x'}
    N = int(np.prod(list(ids.keys())))
    sum = 0
    for id, t in ids.items():
        p = N//id
        sum += (-t%id) *mul_inv(p, id)*p

    ret(int(sum%N))

    # input = list(read())
    # ids = [[int(id),t] for t, id in enumerate(input[1].split(',')) if id != 'x']
    # step = 1
    # n = ids[0][0]
    # for (id, t) in ids:
    #     n = next(c for c in count(n, step) if (c + t) % id == 0)
    #     step *= id
    # ret(n)
if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()