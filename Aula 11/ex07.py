#!/usr/bin/env python3

import re

# Abrir o arquivo para leitura
with open('Python_07_ApoI.fasta', 'r') as file:
    fasta = file.read()

#Local para corte
pattern = r'([AG])(AATT[CT])'

#Substituir o padrão na sequência e inserimos o marcador de corte "^"
mod_seq = re.sub(pattern, r'\1^AATT\2', fasta)

#Imprimir a sequência com os locais de corte
print(mod_seq)
