#!/usr/bin/env python3

seq = input('give a sequence:')

at = seq.count('A') + seq.count('T')

gc = len(seq) - at

print('Conteúdo de AT', at, 'e de GC', gc)
