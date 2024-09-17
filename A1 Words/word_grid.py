"""
    File: word_grid.py
    Author: Anthony Geile
    Course: CSC 120, Fall 2024
    Purpose: Create a grid from a user input of the grid size and a user input of the random seed, then print the grid
"""
import random

def make_grid(grid_size):
    # Returns a grid thats 'grid_size'x'grid_size' big and fills it with random letters based off the random seed using the chr() function
    _=[]
    for i in range(grid_size):
        _.append([chr(random.randint(97, 122))for r in range(grid_size)])
    return _

def print_grid(grid):
    # Prints the grid 'grid' in rows and columns
    for i in grid:
        print(i)

def init():
    #Creates a global variable 'grid_size', takes an input for the grid_size and the seed for the random library
    global grid_size
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)

def main():
    #Calls init() to get the grid size and random seed, then calls make_grid() to create the grid, then calls print_grid() to print the grid
    init()
    grid = make_grid(grid_size)
    print_grid(grid)

main()