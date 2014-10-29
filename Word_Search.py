import numpy as np
import random

def gen_start_coords(size):
# Given an input size, enumerates all possible coordinates for a size by size grid.
# Also adds a third value to each coordinate, indicating whether word should be placed
# vertically or horizontally. Returns list of coordinates.
    coords = []
    for a in range(size):
        for b in range(size):
            coords.append([a,b,1])
    for a in range(size):
        for b in range(size):
            coords.append([a,b,0])
    return coords

def Make_Upper(word_list):
# Given a list of words, returns the same list, but with all letter in upper case
    for pointer in range(len(word_list)):
        word_list[pointer] = word_list[pointer].upper()
    return word_list

def initiate_grid(size):
#Return an empty numpy array of size by size and type string
    grid = np.empty((size,size), dtype='string')
    length = range(size)
    for i in length:
        for j in length:
            grid[i][j] = ''
    return grid

def check_grid(grid, x, y, orientation, word):
#Check whether or not a word can be accomodated in a grid, starting at position (x,y) and 
#oriented either horizontally or vertically. Return 0 if word cannot fit, return 1 if word
#can fit. Also checks to see if other words are crossing, and only allows appropriate crossings.
    if orientation == 0:
        for i in range(len(word)):
            if (grid[x][y] != '') and (grid[x][y] != word[i]):
                return 0
            x+=1
        return 1
    if orientation == 1:
        for i in range(len(word)):
            if (grid[x][y] != '') and (grid[x][y] != word[i]):
                return 0
            y+=1
        return 1

def fill_word(word, grid, coords):
    
# Randomly place a word in a grid by randomly selecting start coordinates
# from a list of starting coordinates (coords) and checking 
# whether or noth the word will fit. Returns a grid with the word entered.

    index = random.randint(0, len(coords)-1)
    guess = coords.pop(index) #choose start coordinate
    orientation = guess[2] #find orientation (vertical or horizontal)
    size = len(grid[0])
    if orientation == 0:
        if guess[0] <= (size-len(word)):
            x = guess[0]
            y = guess[1]
            # randomly decide whether to reverse the order of the word
            direction = random.randint(0,1)
            if direction == 1:
                word = word[::-1]
            # check if the word fits from the given starting coordinates
            if check_grid(grid, x, y, orientation, word) == 1:
                for letter in word:
                    grid[x][y] = letter
                    x+=1
                return grid, 1
    if orientation == 1:
        if guess[1] <= (size-len(word)):
            x = guess[0]
            y = guess[1]
            # randomly decide whether to reverse the order of the word
            direction = random.randint(0,1)
            if direction == 1:
                word = word[::-1]
             # check if the word fits from the given starting coordinates
            if check_grid(grid, x, y, orientation, word) == 1:
                for letter in word:
                    grid[x][y] = letter
                    y+=1
                return grid, 1
    return grid, 0

def random_Letter():
#Return a random capital letter

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = random.choice(letters)
    return letter

def fill_remainder(grid):
#Populate all empty entries of grid with random letters
    length = len(grid[0])
    for i in range(length):
        for j in range(length):
            if grid[i][j] == '':
                grid[i][j]=random_Letter()
    return grid

def Populate_Word_Search(word_list, size):
# Creates an empty grid of size by size, and populates it with all words from word_list
# Fills remainder of grid with random letters, and returns the grid.
    grid = initiate_grid(size)
    for word in word_list:
        coords = gen_start_coords(size)
        grid, check = fill_word(word,grid, coords)
        while (check == 0):
            grid, check = fill_word(word, grid, coords)
    grid = fill_remainder(grid)  
    return grid

def Create_Word_Search(word_list, size):
# In case one combination of starting coordinates does not result in a proper grid,
# keeps trying until one is created.
    for word in word_list:
        if len(word) > size:
            print "At least one word in your list is larger than the grid, try again."
            return 
    result = None
    counter = 0
    while (result is None) & (counter < 200):
        try:
            # connect
            result = Populate_Word_Search(word_list, size)
        except:
            counter +=1
            pass
    if counter == 200:
        return "Cannot create word search. Try again"
    #print result
    return result     

def Ask_for_word():
# Ask the user for a list of words to be placed in a grid
    word_list = raw_input("Enter word list, with each word separated by a comma: ")
    word_list = word_list.split(',')
    for element in range(len(word_list)):
        word_list[element] = word_list[element].strip()
    word_list = Make_Upper(word_list)
    return word_list

def Ask_for_grid():
# Ask the user for the size of the grid they want
    size =raw_input("Enter an integer value for your word search grid size: ")
    size = int(size)
    return size

def print_grid(grid):
# print nice version of grid
    for row in grid:
        print "\n"
        for el in row:
            print el,

def main():
    word_list = Ask_for_word()
    size = Ask_for_grid()
    grid = Create_Word_Search(word_list, size)
    print_grid(grid)

if __name__ == "__main__":
    main()