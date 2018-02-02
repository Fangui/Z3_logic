#!/usr/bin/env python

# Inspire (a lot) from the Picoctf 2013 Harder Serial

# Damn, you lost THE motivation sentence to survive the LSE !!
# All you remember is some constraint (people use that to remember stuff)
# When you have the serial (the actual interresting part), for even MORE FUN, you can be translate it to a sentence (no space, easy translation), if you think you found it, come to me for reward <3

# Exercice from https://github.com/Zorrette/SMT-FUN

import sys
from z3 import *


def check_serial(serial):
  if (not set(serial).issubset(set(map(str,range(10))))):
    print ("only numbers allowed")
    return False
  if len(serial) != 18:
    return False
  if int(serial[15]) + int(serial[4]) != 14:
    return False
  if int(serial[1]) * int(serial[17]) != 0:
    return False
  if int(serial[15]) / int(serial[6]) != 9:
    return False
  if int(serial[17]) - int(serial[0]) != -2:
    return False
  if int(serial[5]) - int(serial[17]) != 9:
    return False
  if int(serial[15]) - int(serial[1]) != 3:
    return False
  if int(serial[1]) * int(serial[10]) != 48:
    return False
  if int(serial[8]) + int(serial[13]) != 7:
    return False
  if int(serial[0]) * int(serial[8]) != 4:
    return False
  if int(serial[4]) * int(serial[11]) != 25:
    return False
  if int(serial[8]) + int(serial[9]) != 2:
    return False
  if int(serial[12]) - int(serial[13]) != -3:
    return False
  if int(serial[9]) % int(serial[16]) != 0:
    return False
  if int(serial[14]) * int(serial[16]) != 2:
    return False
  if int(serial[7]) - int(serial[4]) != 4:
    return False
  if int(serial[6]) + int(serial[0]) != 3:
    return False
  if int(serial[2]) - int(serial[16]) != -1:
    return False
  if int(serial[4]) - int(serial[6]) != 4:
    return False
  if int(serial[5]) * int(serial[11]) != 45:
    return False
  if int(serial[10]) % int(serial[15]) != 8:
    return False
  if int(serial[11]) / int(serial[3]) != 1:
    return False
  if int(serial[13]) - int(serial[14]) != 4:
    return False
  if int(serial[16]) + int(serial[17]) != 2:
    return False
  return True


s = Solver()

c0 = Int('c0')
c1 = Int('c1')
c2 = Int('c2')
c3 = Int('c3')
c4 = Int('c4')
c5 = Int('c5')
c6 = Int('c6')
c7 = Int('c7')
c8 = Int('c8')
c9 = Int('c9')
c10 = Int('c10')
c11 = Int('c11')
c12 = Int('c12')
c13 = Int('c13')
c14 = Int('c14')
c15 = Int('c15')
c16 = Int('c16')
c17 = Int('c17')

s = Solver()
s.add(c15 + c4 == 14)
s.add(c1 * c17 == 0)
s.add(c15 / c6 == 9)
s.add(c17 - c0 == -2)
s.add(c5 - c17 == 9)
s.add(c15 - c1 == 3)
s.add(c1 * c10 == 48)
s.add(c8 + c13 == 7)
s.add(c0 * c8 == 4)
s.add(c4 * c11 == 25)
s.add(c8 + c9 == 2)
s.add(c12 - c13 == -3)
s.add(c9 % c16 == 0)
s.add(c14 * c16 == 2)
s.add(c7 - c4 == 4)
s.add(c6 + c0 == 3)
s.add(c2 - c16 == 1)
s.add(c4 - c6 == 4)
s.add(c5 * c11 == 45)
s.add(c10 % c15 == 8)
s.add(c11 / c3 == 1)
s.add(c13 - c14 == 4)
s.add(c16 + c17 == 2)

print (s.check())
print (s.model())
