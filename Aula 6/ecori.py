#!/usr/bin/env python3

seq = input('Give me a sequence:')

start = seq.find('AATT')

stop = start + 4

print(f'EcoRI startPos:{start}  endPos:{stop}')
