#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    
    # creating a dictionary
    dic = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    
    # or
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    
    # iterating through a dictionary
    for k, v in animals.items() : print( f'{k}: {v}')
    
    # .keys() returns the keys of a dictionary
    for k in animals.keys() : print(k)
    
    # .values() returns the values of a dictionary
    for v in animals.values() : print(v)
    
    # dictionary is a mutable data structure
    animals['monkey'] = 'haha'
    
    # serach in a dictionary (.contains() in java)
    print('found!' if 'lion' in animals else 'nope!')
    
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
