#!/usr/bin/env python3

# Solicita ao usuário que insira o nome do arquivo multi-FASTA
fasta_file = input("Digite o caminho do arquivo multi-FASTA: ")

# Nome dos arquivos de saída
codons_output_file = 'Python_08.codons-6frames.nt'
translation_output_file = 'Python_08.translated_aa.txt'

# Dicionário para armazenar os códons e traduções
output_lines = []
translation_lines = []

# Tabela de tradução
tabela_de_traducao = {
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'AAT': 'N', 'AAC': 'N',
    'GAT': 'D', 'GAC': 'D',
    'TGT': 'C', 'TGC': 'C',
    'CAA': 'Q', 'CAG': 'Q',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'CAT': 'H', 'CAC': 'H',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'AAA': 'K', 'AAG': 'K',
    'ATG': 'M',
    'TTT': 'F', 'TTC': 'F',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'TGG': 'W',
    'TAT': 'Y', 'TAC': 'Y',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TAA': '*', 'TGA': '*', 'TAG': '*'
}

# Função para obter o complemento reverso de uma sequência
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

# Função para traduzir a sequência em aminoácidos
def translate_sequence(sequence):
    protein = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if codon in tabela_de_traducao:
            protein.append(tabela_de_traducao[codon])
        else:
            protein.append('X')  # Representa um codon não reconhecido
    return ''.join(protein)

try:
    with open(fasta_file, 'r') as file:
        gene_name = None
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Se já há uma sequência, processa antes de começar a próxima
                if gene_name and sequence:
                    # Gera códons para os três primeiros quadros de leitura
                    for frame in range(3):
                        frame_sequence = sequence[frame:]
                        codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                        output_lines.append(f"{gene_name}-frame-{frame + 1}-codons\n" + ' '.join(codons))
                        # Traduz os códons em aminoácidos
                        translated = translate_sequence(frame_sequence)
                        translation_lines.append(f"{gene_name}-frame-{frame + 1}-translation\n" + translated)

                    # Obtém o complemento reverso e gera códons para os três quadros de leitura
                    rev_comp_sequence = reverse_complement(sequence)
                    for frame in range(3):
                        frame_sequence = rev_comp_sequence[frame:]
                        codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                        output_lines.append(f"{gene_name}-frame-{frame + 4}-codons\n" + ' '.join(codons))
                        # Traduz os códons em aminoácidos
                        translated = translate_sequence(frame_sequence)
                        translation_lines.append(f"{gene_name}-frame-{frame + 4}-translation\n" + translated)

                # Atualiza o nome do gene e reinicia a sequência
                gene_name = line[1:]  # Remove o '>' do nome
                sequence = ''
            else:
                # Verifica se a linha contém apenas caracteres válidos
                if any(base not in "ATCG" for base in line):
                    print(f"Erro: A sequência contém caracteres inválidos: {line}")
                    continue  # Ignora linhas inválidas
                # Concatena as linhas da sequência
                sequence += line

        # Processa a última sequência
        if gene_name and sequence:
            for frame in range(3):
                frame_sequence = sequence[frame:]
                codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                output_lines.append(f"{gene_name}-frame-{frame + 1}-codons\n" + ' '.join(codons))
                translated = translate_sequence(frame_sequence)
                translation_lines.append(f"{gene_name}-frame-{frame + 1}-translation\n" + translated)

            rev_comp_sequence = reverse_complement(sequence)
            for frame in range(3):
                frame_sequence = rev_comp_sequence[frame:]
                codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                output_lines.append(f"{gene_name}-frame-{frame + 4}-codons\n" + ' '.join(codons))
                translated = translate_sequence(frame_sequence)
                translation_lines.append(f"{gene_name}-frame-{frame + 4}-translation\n" + translated)

    # Escreve a saída dos códons no arquivo
    with open(codons_output_file, 'w') as codons_file:
        codons_file.write('\n'.join(output_lines))

    # Escreve a saída da tradução no arquivo
    with open(translation_output_file, 'w') as translation_file:
        translation_file.write('\n'.join(translation_lines))

    print(f"Saída dos códons gravada em '{codons_output_file}'.")
    print(f"Saída da tradução gravada em '{translation_output_file}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{fasta_file}' não foi encontrado.")
