#!/usr/bin/env python3

# Solicita o nome do arquivo multi-FASTA
fasta_file = input("Digite o caminho do arquivo multi-FASTA: ")

# Arquivos de saída
codons_output_file = 'Python_08.codons-6frames.nt'
translation_output_file = 'Python_08.translated_aa.txt'
longest_peptide_output_file = 'Python_08.translated-longest_aa.txt'

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
    try:
        return ''.join(complement[base] for base in reversed(sequence) if base in complement)
    except KeyError:
        print("Erro: Caracteres inválidos na sequência.")
        return ''

# Função para traduzir uma sequência em aminoácidos
def translate_sequence(sequence):
    protein = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]
        if codon in tabela_de_traducao:
            protein.append(tabela_de_traducao[codon])
        else:
            protein.append('X')
    return ''.join(protein)

# Função para encontrar o peptídeo mais longo de uma sequência traduzida
def find_longest_peptide(protein_seq):
    peptides = protein_seq.split('*')
    longest_peptide = ""
    for pep in peptides:
        if 'M' in pep:
            pep = pep[pep.index('M'):]  # Obtém o trecho de M até antes de '*'
            if len(pep) > len(longest_peptide):
                longest_peptide = pep
    return longest_peptide

try:
    with open(fasta_file, 'r') as file:
        gene_name = None
        sequence = ''
        codons_output = []
        translation_output = []
        longest_peptide_output = []

        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Processa a sequência anterior
                if gene_name and sequence:
                    longest_peptide = ""
                    for i in range(3):
                        # Quadro direto
                        frame_seq = sequence[i:]
                        frame_codons = [frame_seq[j:j + 3] for j in range(0, len(frame_seq), 3)]
                        codons_output.append(f"{gene_name}-frame-{i+1}-codons\n" + ' '.join(frame_codons))
                        frame_translation = translate_sequence(frame_seq)
                        translation_output.append(f"{gene_name}-frame-{i+1}-translation\n" + frame_translation)
                        peptide = find_longest_peptide(frame_translation)
                        if len(peptide) > len(longest_peptide):
                            longest_peptide = peptide

                        # Complemento reverso
                        rev_frame_seq = reverse_complement(sequence)[i:]
                        rev_frame_codons = [rev_frame_seq[j:j + 3] for j in range(0, len(rev_frame_seq), 3)]
                        codons_output.append(f"{gene_name}-frame-{i+4}-codons\n" + ' '.join(rev_frame_codons))
                        rev_frame_translation = translate_sequence(rev_frame_seq)
                        translation_output.append(f"{gene_name}-frame-{i+4}-translation\n" + rev_frame_translation)
                        peptide = find_longest_peptide(rev_frame_translation)
                        if len(peptide) > len(longest_peptide):
                            longest_peptide = peptide

                    longest_peptide_output.append(f">{gene_name}-longest-peptide\n{longest_peptide}")

                # Atualiza o gene e reseta a sequência
                gene_name = line[1:]
                sequence = ''
            else:
                sequence += line

        # Processa a última sequência
        if gene_name and sequence:
            longest_peptide = ""
            for i in range(3):
                # Quadro direto
                frame_seq = sequence[i:]
                frame_codons = [frame_seq[j:j + 3] for j in range(0, len(frame_seq), 3)]
                codons_output.append(f"{gene_name}-frame-{i+1}-codons\n" + ' '.join(frame_codons))
                frame_translation = translate_sequence(frame_seq)
                translation_output.append(f"{gene_name}-frame-{i+1}-translation\n" + frame_translation)
                peptide = find_longest_peptide(frame_translation)
                if len(peptide) > len(longest_peptide):
                    longest_peptide = peptide

                # Complemento reverso
                rev_frame_seq = reverse_complement(sequence)[i:]
                rev_frame_codons = [rev_frame_seq[j:j + 3] for j in range(0, len(rev_frame_seq), 3)]
                codons_output.append(f"{gene_name}-frame-{i+4}-codons\n" + ' '.join(rev_frame_codons))
                rev_frame_translation = translate_sequence(rev_frame_seq)
                translation_output.append(f"{gene_name}-frame-{i+4}-translation\n" + rev_frame_translation)
                peptide = find_longest_peptide(rev_frame_translation)
                if len(peptide) > len(longest_peptide):
                    longest_peptide = peptide

            longest_peptide_output.append(f">{gene_name}-longest-peptide\n{longest_peptide}")

    # Salva as saídas
    with open(codons_output_file, 'w') as f:
        f.write('\n'.join(codons_output))
    with open(translation_output_file, 'w') as f:
        f.write('\n'.join(translation_output))
    with open(longest_peptide_output_file, 'w') as f:
        f.write('\n'.join(longest_peptide_output))

    print(f"Saídas salvas em '{codons_output_file}', '{translation_output_file}', e '{longest_peptide_output_file}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{fasta_file}' não foi encontrado.")
