#word of the day = 'file'
#1
for i in range(100, 1, -2):
    print(i)

#2
def get_words(s):
    return s.split('-')

print(get_words('CS-120-Summer-2018-U-of-A'))

#3
def sum_column(grid, offset):
    if offset >= len(grid): return 'Error: Offset larger then grid'
    else: return sum([i[offset] for i in grid])

print(sum_column([[11, 22, 33, 44, 55],[66, 77, 88, 99, 11],[22, 33, 44, 55, 66],[77, 88, 99, 11, 22],[33, 44, 55, 66, 77]], 2))

#4
def print_some_words(filename,n):
    _=[]
    poem = [line for line in open('poem.txt')]
    for line in poem:
        for word in line.split():
            word = word.strip(',.;:?')
            if len(word) >= n:
                _.append(word)
    print('\n'.join(_))

print_some_words('poem.txt', 6)

#5
def sum_diag_UL_LR(grid, offset):
    if abs(offset) >= len(grid):
        return 'Error: Offset larger then grid'
    else:
        _, x, y = [], 0, 0
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
    return _
print(sum_diag_UL_LR([[11, 22, 33, 44, 55],[66, 77, 88, 99, 11],[22, 33, 44, 55, 66],[77, 88, 99, 11, 22],[33, 44, 55, 66, 77]], -1))