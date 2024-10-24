#!/usr/bin/env python3

import re

# Abrir o arquivo para leitura
with open('Python_07_ApoI.fasta', 'r') as file:
    fasta = file.read()

for found in re.finditer(r"(.?AATT.?)"  , fasta):
  loc     = found.group(1)
  loc_start = found.start(1) + 1   # é necessário converter da notação 0 para 1
  loc_end   = found.end(1)

  print(loc , loc_start, loc_end, sep="\t" )

