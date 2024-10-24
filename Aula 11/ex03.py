import re

# Abrir o arquivo FASTA para leitura
with open('Python_07.fasta', 'r') as file:
    fasta_content = file.readlines()

i = 0
for line in fasta_content:
    i += 1  # Incrementa o contador de linhas
    match = re.match(r'^>(\S+)\s*(.*)', line)

    #Verificar se o match não é None
    if match:
        print(f"Linha = {i}, Cabeçalho = {match.group(0)}")
