"""
    File: word_search.py
    Author: Anthony Geile
    Course: CSC 120, Fall 2024
    Purpose: Finds all words from a grid using a word bank
"""

def get_word_list():
    #Returns a list of valid words 
    return open('WORDS.txt').read().split()

def read_letters_files():
    #Returns a list of the letters grid
    return open('Letters.txt').read().replace(' ', '').split()

def horizontal_construct(grid, reverse):
    #Constructs the possible horizontal words
    _ = []
    for raw_row in grid:
        #Reverses the row when reverse is True
        row = raw_row[::-1] if reverse == 1 else raw_row
        #Shifts the row as many times as the row is long minus 3 because thats the min length of a word
        for shift_count in range(len(row)-3):
            for build_count in range(3+shift_count, len(row)+shift_count):
                _.append(row[shift_count:build_count])
    return _

def vertical_construct(grid, reverse):
    #Constructs the possible vertical words
    _ = []
    new_grid = []
    #Creates a new grid the transitions the original grid so that the columns become rows and vice versa
    for count in range(len(grid)):
        temp = ''
        for row in grid:
            temp += row[count]
        new_grid.append(temp)

    #Finds all the possible words with the reverse function built in by using the same for loop as the horizontal_construct
    for raw_row in new_grid:
        row = raw_row[::-1] if reverse == 1 else raw_row
        for shift_count in range(len(row)-3):
            for build_count in range(3+shift_count, len(row)+shift_count):
                _.append(row[shift_count:build_count])
    return _

def diagonal_construct(grid, reverse):
    row = []
    for i in range(2):
        #Reverses the horizontal axis of the grid
        if reverse == 1: grid.reverse()
        #Reverses the vertical axis of the grid
        if i == 1:
            new_grid = []
            for i in grid:
                new_grid.append(i[::-1])

        #Finds all possible words along the diagonals
        for i in range((-len(grid)+3), (len(grid)-2)):
            offset, _, x, y = i, [], 0, 0
            if offset < 0:
                y=abs(offset)
                for i in range(len(grid)-y):
                    _.append(grid[x][y])
                    x += 1
                    y += 1
            elif offset > 0:
                x=abs(offset)
                for i in range(len(grid)-x):
                    _.append(grid[x][y])
                    x += 1
                    y += 1
            elif offset == 0:
                for i in range(len(grid)):
                    _.append(grid[x][y])
                    x += 1
                    y += 1
            row.append(''.join(_))
    return row

def create_possible_words(grid):
    #Creates all possible words in the grid (Horizontal, Vertical and Diagonal)
    Final_list = []

    #Runs the Constructs
    for i in range(2):
       Final_list.extend(horizontal_construct(grid,i))
       Final_list.extend(vertical_construct(grid, i))
       Final_list.extend(diagonal_construct(grid, i))

    return Final_list

def compute(word_list, possible_words):
    _ = []
    #Compares possible words to word bank
    for word in possible_words:
        if word in word_list:
            _.append(word)
    return tuple(_)

def main():
    #Runs all functions
    word_list = get_word_list()
    letters_grid = read_letters_files()
    possible_words = create_possible_words(letters_grid)
    found_words = compute(word_list, possible_words)
    return found_words

#print(main())
main()