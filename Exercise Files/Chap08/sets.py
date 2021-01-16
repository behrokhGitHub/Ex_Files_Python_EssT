#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print('members that are in set a, but not in set b', a - b)
    print('members that are in set a, or in set b, or in both', a | b)
    
    d = set(['hel', '3', '4', '1.0', 'gav'])
    e = set(['hel', '3', 4, 1.0, 'gav'])
    print('members that are in set d, but not in set e', d - e)
    print('members that are in set d, or in set e, or in both', d | e)
    print('members that are in set d, or in set e, but not in both', d ^ e)
    
    print(a ^ b)
    c = set()
    c.add("hello")
    c.add(2)
    print(c)
    print_set(a)
    print_set(b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
