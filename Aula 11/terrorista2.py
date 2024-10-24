#!/usr/bin/env python3

import re

#Abrir o arquivo para leitura
with open('texto_t.txt', 'r') as file:
    text = file.read()

print(re.sub(r'\b(tic[- ]tac)\b', 'motor', text))



