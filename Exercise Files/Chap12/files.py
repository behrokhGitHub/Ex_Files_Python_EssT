#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
            
    openfile = open('lines.txt', 'rt')
    outfile = open('lines_copy.txt', 'wt')
    
    for line in openfile:
        
        print(line.rstrip(), file=outfile)
        print('.', end='',flush=True)
        
    outfile.close()
    print('\ndone')
        
if __name__ == '__main__': main()
