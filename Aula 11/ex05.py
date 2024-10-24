import re

# Abrir o arquivo FASTA para leitura
with open('Python_07.fasta', 'r') as file:
    fasta_content = file.readlines()

i = 0
for line in fasta_content:
    i += 1
    match = re.match(r'^>(\S+)\s*(.*)', line)

    if match:
        seq_name = match.group(1)  #sem espaços
        desc = match.group(2)  #Descrição da sequência
        print(f"Sequência: {seq_name}, Descrição: {desc}")


i = 0
for line in fasta_content:
    i += 1
    match = re.match(r'^>(\S+)\s*(.*)', line)

    if match:
        seq_name = match.group(1)  #sem espaços
        desc = match.group(2)  #Descrição da sequência
        print(f"Sequência: {seq_name}, Descrição: {desc}")
