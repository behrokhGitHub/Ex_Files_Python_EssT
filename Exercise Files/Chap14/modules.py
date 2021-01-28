#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    
    p = sys.platform
    print(p)
    
    o = os.name
    print(o)
    
    path = os.getenv('PATH')
    print(path)
    
    cwd = os.getcwd()
    print(cwd)
    
    ran = list(range(25))
    print(ran)
    random.shuffle(ran)
    print(ran)

if __name__ == '__main__': main()
