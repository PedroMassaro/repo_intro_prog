#!/usr/bin/env python3

seq = input('give a sequence')

a = seq.count('a') + seq.count('A')
t = seq.count('t') + seq.count('T')
c = seq.count('c') + seq.count('C')
g = seq.count('g') + seq.count('G')

print(f'número de A.s {a}, T.s {t}, C.s {c} e G.s {g}')
