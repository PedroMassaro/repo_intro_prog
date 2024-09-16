#!/usr/bin/env python3

seq = input('give a sequence:')


seq01 = seq.replace('A','b')
seq02 = seq01.replace('T','A')
seq03 = seq02.replace('b','T')

seq04 = seq03.replace('C','h')
seq05 = seq04.replace('G','C')
seq06 = seq05.replace('h','G')

seq07 = seq06[ : :-1]

print(seq07)
