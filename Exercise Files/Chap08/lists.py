#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    
    # range in list
    print(game[1:3])
    
    # range in list with steps
    print(game[1:5:2])
    
    # finding the index of an item 
    i = game.index('Scissors')
    print(game[i])
    
    # append an item to a list
    game.append('Computers')
    game.insert(0, 'Paper')
    
    # remove an item form a list
    game.remove('Paper')
    
    # remove from end of the list
    game.pop()
    
    # pop() also return the removed item
    x = game.pop()
    print(x)
    
    # pop() also remove an item at particular index
    y = game.pop(0)
    print(y)
    
    # remove an item using del
    del game[2]
    
    game.append('Lizard')
    game.append('Spock')
    print_list(game)
    
    # or remove by a slice
    del game[1:3]
    
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
