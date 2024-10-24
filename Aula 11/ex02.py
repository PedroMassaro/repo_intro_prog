#!/usr/bin/env python3

import re

#Abrir o arquivo para leitura
with open('Python_07_nobody.txt', 'r') as file:
    text = file.read()

fav_name = 'Pedro'

#Substituir todas as ocorrências de 'Nobody' pelo nome favorito
new_text = text.replace('Nobody', fav_name)

#Escrever o texto em um arquivo de saída com o nome favorito
output_filename = f'{fav_name}.txt'
with open(output_filename, 'w') as output_file:
    output_file.write(new_text)

print(f"Todas as ocorrências de 'Nobody' foram substituídas por '{fav_name}' e o arquivo foi salvo como {output_filename}.")

