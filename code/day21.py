from itertools import combinations, product
from utils import read, ret
#import scipy.spatial.distance
#https://docs.scipy.org/doc/scipy/reference/spatial.distance.html
import pandas as pd
import numpy as np 
import argparse
from pprint import pprint
from scipy.optimize import linear_sum_assignment
parser = argparse.ArgumentParser()
parser.add_argument('--f', type=int, help='Function to run', default=1)
FLAGS = parser.parse_args()

func = FLAGS.f
pd.set_option('display.max_rows', None)
def part1():
    print('Part 1:\n')
    input = next(read(ret_type='str'))
    input = input.split('\n')
    food = []
    all_ingredients = []
    all_allergens = []
    for line in input:
        ingredients, allergens = line.split('(')
        ingredients = ingredients[:-1].split(' ')
        all_ingredients += ingredients
        allergens = [allergen.strip() for allergen in allergens[9:-1].split(',')]
        all_allergens += allergens
        food.append([ingredients, allergens])
    all_allergens_set = set(all_allergens)
    all_ingredients_set = set(all_ingredients)
    food_data = np.full((len(all_ingredients_set), len(all_allergens_set)),0)
    food_df = pd.DataFrame(food_data, all_ingredients_set, all_allergens_set)
    for (ingredients, allergens) in food:
        for ingredient, allergen in product(ingredients, allergens):
            food_df[allergen][ingredient] += 1

    row_ind, col_ind = linear_sum_assignment(food_df, maximize=True)
    assigned_ingredients = []
    print(food_df)
    for row, col in zip(row_ind, col_ind):
        assigned_ingredients.append(food_df.index[row]) 
        print(food_df.index[row], food_df.columns[col], food_df.iloc[row][col])

    remaining_ingredients = [ingredient for ingredient in all_ingredients if ingredient not in assigned_ingredients]
    ret(len(remaining_ingredients))

def part2():
    print('Part 2:\n')
    input = next(read(ret_type='str'))
    input = input.split('\n')
    food = []
    all_ingredients = []
    all_allergens = []
    for line in input:
        ingredients, allergens = line.split('(')
        ingredients = ingredients[:-1].split(' ')
        all_ingredients += ingredients
        allergens = [allergen.strip() for allergen in allergens[9:-1].split(',')]
        all_allergens += allergens
        food.append([ingredients, allergens])
    all_allergens_set = set(all_allergens)
    all_ingredients_set = set(all_ingredients)
    food_data = np.full((len(all_ingredients_set), len(all_allergens_set)),0)
    food_df = pd.DataFrame(food_data, all_ingredients_set, all_allergens_set)
    for (ingredients, allergens) in food:
        for ingredient, allergen in product(ingredients, allergens):
            food_df[allergen][ingredient] += 1

    row_ind, col_ind = linear_sum_assignment(food_df, maximize=True)
    assigned_ingredients = []
    for row, col in zip(row_ind, col_ind):
        assigned_ingredients.append([food_df.columns[col], food_df.index[row]]) 
    s = ''
    for allergen, ingredient in sorted(assigned_ingredients):
        s += ingredient +','

    ret(s[:-1])

if __name__ == "__main__":
    if func == 1:
        part1()
    else:
        part2()