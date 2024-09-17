"""
    File: pokemon.py
    Author: Anthony Geile
    Course: CSC 120, Fall 2024
    Purpose: Sort Pokemon by attribute and print the strongest one
"""

def pokeprocessor(pokemon, userinput, pokeindex):  
    """
    Takes the average of the userinput in all the pokemon 
    and outputs a list of the highest average

    Parameters: 2-Level pokemon dictionary, user input, list of pokemon indexes
  
    Returns: Largest average of userinput and its type
    
    """ 
    comp = []
    past = [[0]]
    final = []
    if userinput.upper() in pokeindex:
        for key, value in pokemon.items():
            average = 0
            for info in value:
                average += int(info[pokeindex.index(userinput.upper())-3])
            comp = [float(average/len(value)), key]
            if comp[0] > past[0][0]:
                past = []
                past.append(comp)
            elif comp[0] == past[0][0]:
                past.append(comp)
            comp  = []
        final.extend(sorted(past))
        past = [[0]]
    return final
        

def pokecompiler(pokedata): 
    """
    Compiles all pokemon into a dictonary from the given file

    Parameters: List of all Pokemon data from file
  
    Returns: A 2 level dictonary, ordering the pokemon by type
    
    """ 
    pokemon = {}
    for line in pokedata:
        line = line.split(',')
        if line[2] in pokemon:
            pokemon[line[2]].append(line[3:])
        else:
            pokemon[line[2]] = [line[3:]]
    return pokemon

def init(filename):
    """
    Create a pokeindex file and a pokedata file to use later 
    and orders pokemon catagories

    Parameters: Takes file name 
  
    Returns: The a list that has the indexes of pokemon catagories 
    and a list of the pokemon information from the file
    
    """
    pokeindex = []
    file = open(filename)
    pokedata = file.read().strip().split('\n')
    file.close()
    for catagory in pokedata[0].split(','):
        if catagory == 'Type 1':
            catagory = 'TYPE'
        elif catagory == 'Sp. Atk':
            catagory = 'specialattack'
        elif catagory == 'Sp. Def':
            catagory = 'specialdefense'
        elif catagory == None: 
            break
        pokeindex.append(catagory.upper())
    pokedata.pop(0)
    return pokeindex, pokedata

def main():
    """
    Runs all functions, takes user inputs and prints out pokemon information
    """
    filename = input() 
    pokeindex, pokedata = init(filename)
    while 1:
        userinput = input()
        if userinput == '':
            break
        else:
            pokemon = pokecompiler(pokedata)
            pd = pokeprocessor(pokemon,userinput, pokeindex)
            for info in pd:
                print(f"{info[1]}: {info[0]}")

main()