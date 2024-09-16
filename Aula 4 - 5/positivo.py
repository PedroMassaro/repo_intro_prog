#!/usr/bin/env python3

import sys

#a = int(sys.argv[1])
a = input('give a number')
a = int(a)

#if a >= 0:
 #print('Positivo')
#else:
 #print('Negativo')

if a > 0:
 print('Positivo')
 if a < 50:
  print('menor que 50')
  if (a%2 == 0):
   print('é um número par menor que 50')
 else:
  if (a > 50) and (a%3 == 0):
   print('é um número maior que 50 divisível por 3')
else:
 print('negativo')
