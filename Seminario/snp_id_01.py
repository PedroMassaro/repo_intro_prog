#!/usr/bin/env python3

import sys

# Definindo a exceção personalizada NotATCG
class NotATCG(Exception):
    pass

try:
    file01 = sys.argv[1]
    print("Usuário forneceu o nome do arquivo da primeira sequência como: ", file01)

    file02 = sys.argv[2]
    print("Usuário forneceu o nome do arquivo da segunda sequência como: ", file02)

    # Validação das sequências
    # Verificar se o arquivo tem a extensão correta
    if not (file01.endswith('.fasta') or file01.endswith('.fa') or file01.endswith('.nt') or file02.endswith('.fasta') or file02.endswith('.fa') or file02.endswith('.nt')):
        raise ValueError("Os arquivos devem ter uma das seguintes extensões '.fasta', '.fa' ou '.nt'.")

    # Lendo o primeiro arquivo e salvando o ID e a sequência
    name01 = ""
    seq01 = ""
    with open(file01, "r") as FASTA01:
        for line in FASTA01:
            line = line.rstrip()
            if line.startswith('>'):
                name01 = line
            else:
                # Transformando toda a sequência para letra maiúscula e acumulando como uma string
                seq01 += line.upper()

    # Lendo o segundo arquivo e salvando o ID e a sequência
    name02 = ""
    seq02 = ""
    with open(file02, "r") as FASTA02:
        for line in FASTA02:
            line = line.rstrip()
            if line.startswith('>'):
                name02 = line
            else:
                # Transformando toda a sequência para letra maiúscula e acumulando como uma string
                seq02 += line.upper()

    # Verificando se não há outros caracteres dentro das sequências
    if not set(seq01).issubset(set("ATCG")) or not set(seq02).issubset(set("ATCG")):
        raise NotATCG("Erro: Outros desses caracteres, além desse conjunto A, T, C, G, foram encontrados nesta sequência. Verifique sua sequência!")

    # Comparação das sequências para identificação de SNPs
    print("Comparando sequências...")
    snps = []
    for i in range(min(len(seq01), len(seq02))):
        if seq01[i] != seq02[i]:
            snps.append((i, seq01[i], seq02[i]))

    # Armazenamento e exibição dos SNPs
    if snps:
        print("SNPs identificados:")
        for pos, base1, base2 in snps:
            print(f"SNP identificado na posição {pos}: {base1} -> {base2}")
    else:
        print("Nenhum SNP identificado.")
    # Exibição da contagem de SNPs
    print(f"Total de {len(snps)} SNPs identificados.")

except ValueError:
    print("O arquivo deve ter uma das seguintes extensões '.fasta', '.fa' ou '.nt'.")
# Se uma entrada não é fornecida
except IndexError:
    print("Error: Please provide a file name")
# Se o arquivo não pode ser aberto
except IOError:
    print("Error: Can't find file:", file01)
# Presença de outros caracteres, além de ATCG
except NotATCG:
    print("Erro: Outros desses caracteres, além desse conjunto A, T, C, G, foram encontrados nesta sequência. Verifique sua sequência!")
else:
    print("Your file was uploaded correctly")
