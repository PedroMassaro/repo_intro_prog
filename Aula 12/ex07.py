import sys

# Tabela de tradução de códons para aminoácidos
tabela_de_traducao = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

# Função para obter o complemento reverso de uma sequência
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, '') for base in reversed(sequence))

# Função para encontrar o peptídeo mais longo em uma sequência de aminoácidos
def longest_peptide(protein_sequence):
    longest_pep = ''
    current_pep = ''
    for aa in protein_sequence:
        if aa == 'M':  # Start a new peptide
            current_pep = 'M'
        elif aa == '*' and current_pep:  # End of current peptide
            if len(current_pep) > len(longest_pep):
                longest_pep = current_pep
            current_pep = ''
        elif current_pep:
            current_pep += aa
    return longest_pep if longest_pep else current_pep

# Função para ler o arquivo FASTA e armazenar as sequências
def read_fasta(file):
    sequences = {}
    with open(file, 'r') as f:
        seq_id = None
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_id:
                    sequences[seq_id] = seq
                seq_id = line[1:]
                seq = ''
            else:
                seq += line
        if seq_id:
            sequences[seq_id] = seq
    return sequences

# Função para traduzir uma sequência de DNA em uma sequência de aminoácidos
def translate(dna_sequence):
    protein = []
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        amino_acid = tabela_de_traducao.get(codon, '')
        if amino_acid:
            protein.append(amino_acid)
    return ''.join(protein)

# Processamento principal
sequences = read_fasta('Python_08.fasta')

with open('Python_08.codons-6frames.nt', 'w') as codons_file, \
     open('Python_08.translated.aa', 'w') as translated_file, \
     open('Python_08.translated-longest.aa', 'w') as longest_pep_file, \
     open('Python_08.orf-longest.nt', 'w') as orf_longest_file:

    for seq_id, sequence in sequences.items():
        # Gerar os seis quadros de leitura (3 no sentido normal e 3 no complemento reverso)
        frames = [sequence[i:] for i in range(3)] + [reverse_complement(sequence)[i:] for i in range(3)]
        
        longest_peptide_seq = ''
        longest_codons_seq = ''
        
        for frame_index, frame_seq in enumerate(frames, start=1):
            # Gerar códons
            codons = [frame_seq[i:i+3] for i in range(0, len(frame_seq) - 2, 3)]
            codons_file.write(f'>{seq_id}-frame-{frame_index}-codons\n{" ".join(codons)}\n')

            # Traduzir para aminoácidos
            protein_seq = translate("".join(codons))
            translated_file.write(f'>{seq_id}-frame-{frame_index}-translated\n{protein_seq}\n')

            # Encontrar o peptídeo mais longo
            current_longest_peptide = longest_peptide(protein_seq)
            if len(current_longest_peptide) > len(longest_peptide_seq):
                longest_peptide_seq = current_longest_peptide
                longest_codons_seq = "".join(codons)

        # Escrever o peptídeo mais longo para a sequência
        longest_pep_file.write(f'>{seq_id}-longest-peptide\n{longest_peptide_seq}\n')
        orf_longest_file.write(f'>{seq_id}-longest-orfs\n{longest_codons_seq}\n')
