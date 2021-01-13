#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

p = Decimal('0.1')
q = Decimal('0.1')
r = Decimal('0.1')
s = Decimal('0.3')
t = p+q+r-s
print('p+q-r {}'.format(p+q+r-s))
print(type(t))

x = 'seven'
print('seven {} {}'.format(8, 9))
print('seven {1} {0}'.format(8, 9))
print('seven {:>9} {:>9}'.format(8, 9))
print('seven {:>09} {:>09}'.format(8, 9))
a = 8
b = 9
# using fstring performs the same as .format() 
x = f'seven {9} {9}'
y = f'seven {a} {b}'
print('x is {}'.format(x))
print('y is {}'.format(y))
print(type(x))

