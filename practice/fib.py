#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:44:24 2021

@author: behrokh
"""
def main():
    n = 0
    while fib(n) < 1000:

        print(fib(n))
        n = n+1
    # fibonacci at index n 
    print('fib(n) at index 10 is {}'.format(fib(10)))
    
    print('fib_mem testing: ')
    mem={}
    i = 0
    while i < n:
        print (i, ' ', fib_mem(i, mem))
        i+=1
     

def fib(n):
    
    if n == 0:
        return 0;
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

def fib_mem(n, mem):
    
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        mem[n] = fib(n-1) + fib(n-2)
     
    return mem[n] 

   
    
if __name__ == '__main__': main()