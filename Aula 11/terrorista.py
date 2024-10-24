#!/usr/bin/env python3

import re

#Abrir o arquivo para leitura
with open('texto_t.txt', 'r') as file:
    text = file.read()

for found in re.finditer(r"(\b(tic[- ]tac|bomba|carro[- ]bomba|explosivo)\b)"  , text):
  nob     = found.group(1)
  nob_start = found.start(1) + 1   # é necessário converter da notação 0 para 1
  nob_end   = found.end(1)

if nob_start != 0:
  print("Ameaça:")
  print(nob , nob_start, nob_end, sep="\t" )



