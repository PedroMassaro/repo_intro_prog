#!/usr/bin/env python3

# Solicita ao usuário que insira o nome do arquivo multi-FASTA
fasta_file = input("Digite o caminho do arquivo multi-FASTA: ")

# Nome do arquivo de saída
output_file = 'Python_08.codons-6frames.nt'

# Lista para armazenar as saídas dos códons
output_lines = []

# Função para obter o complemento reverso de uma sequência
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

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

                    # Obtém o complemento reverso e gera códons para os três quadros de leitura
                    rev_comp_sequence = reverse_complement(sequence)
                    for frame in range(3):
                        frame_sequence = rev_comp_sequence[frame:]
                        codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                        output_lines.append(f"{gene_name}-frame-{frame + 4}-codons\n" + ' '.join(codons))

                # Atualiza o nome do gene e reinicia a sequência
                gene_name = line[1:]  # Remove o '>' do nome
                sequence = ''
            else:
                # Concatena as linhas da sequência
                sequence += line

        # Processa a última sequência
        if gene_name and sequence:
            for frame in range(3):
                frame_sequence = sequence[frame:]
                codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                output_lines.append(f"{gene_name}-frame-{frame + 1}-codons\n" + ' '.join(codons))

            rev_comp_sequence = reverse_complement(sequence)
            for frame in range(3):
                frame_sequence = rev_comp_sequence[frame:]
                codons = [frame_sequence[i:i + 3] for i in range(0, len(frame_sequence), 3)]
                output_lines.append(f"{gene_name}-frame-{frame + 4}-codons\n" + ' '.join(codons))

    # Escreve a saída no arquivo
    with open(output_file, 'w') as out_file:
        out_file.write('\n'.join(output_lines))

    print(f"Saída gravada em '{output_file}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{fasta_file}' não foi encontrado.")
