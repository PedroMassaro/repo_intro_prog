#!/usr/bin/env python3
from collections import defaultdict

# Solicita ao usuário que insira o nome do arquivo multi-FASTA
fasta_file = input("Digite o caminho do arquivo multi-FASTA: ")

# Dicionário para armazenar a composição de nucleotídeos
seqs = defaultdict(lambda: {'A': 0, 'T': 0, 'G': 0, 'C': 0})

try:
    with open(fasta_file, 'r') as file:
        gene_name = None
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                #Identifica o nome da sequência
                gene_name = line[1:]
            elif gene_name:
                #Conta os nucleotídeos da sequência
                for nucleotide in line:
                    if nucleotide in seqs[gene_name]:
                        seqs[gene_name][nucleotide] += 1

    # Imprime a composição de nucleotídeos no formato especificado
    for gene, counts in seqs.items():
        print(f"{gene}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{fasta_file}' não foi encontrado.")
