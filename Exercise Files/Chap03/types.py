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

x = 0x0a
y = 0x01
z = x >> y

print (f'(hex)  x is {x:02x}, y is  {y:02x}, z is {z:02x}')
print (f'(bin)  x is {x:08b}, y is  {y:08b}, z is {z:08b}')

x = 5
y = 3
z = x / y

print (f'result is {z}')