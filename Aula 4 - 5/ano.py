#!/usr/bin/env python3

import sys

a = int(sys.argv[1])

if (a%4 == 0 and a%100 != 0) or (a%400 == 0):
 print(f'{a} é um ano bissexto')
else:
 print(f'{a} não é um ano bissexto')


