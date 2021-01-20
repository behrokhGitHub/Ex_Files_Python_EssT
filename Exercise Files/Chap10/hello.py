#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    
    print('Hello, World. upper()'.upper())
    print('Hello, World. lower()'.lower())
    print('Hello, World. capitalize()'.capitalize())
    print('Hello, World. lower()'.lower())
    print('Hello, World. title()'.title())
    print('Hello, World.'.swapcase())
    print('Hello, World. upper()'.upper())
    print('Hello, World.'.casefold()) # works like lower() but in more aggresive way 
    
    # concatinate two strings
    s1 = 'hello world.'
    s2 = 'this is a python class.'
    print(s1 + ' ' + s2)
    
    # formatting strings in python
    # insert comma for a 1000 seperation
    x = 4 * 749 * 1000
    print('the result is {:,}'.format(x).replace(',', '.'))
    print(f'the result is {:,}'.format(x))
    
    
    
class MyString(str):
    def __str__(self):
        return self[::-1]
    
s = MyString('hello world.')
print(s)
        

if __name__ == '__main__': main()






































