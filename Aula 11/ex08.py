#!/usr/bin/env python3

import re

with open('Python_07_ApoI.fasta', 'r') as file:
    fasta = file.read()

#Local para corte
pattern = r'([AG])(AATT[CT])'

#Substituir o padrão na sequência e inserimos o marcador de corte "^"
mod_seq = re.sub(pattern, r'\1^AATT\2', fasta)

#Dividir a sequência nos locais de corte usando '^'
frag = mod_seq.split('^')

#Remover '\n' de cada fragmento
for i in range(len(frag)):
    frag[i] = frag[i].replace('\n', '')

#Imprimir
print(sorted(frag, key=len, reverse=True))


