#!/usr/bin/env python3

# Simulação do processo descrito no fluxograma

def entrada_sequencias():
    # Entrada das sequências de DNA
    return input("Insira a sequência de DNA: ").upper()

def validar_sequencia(sequencia):
    # Valida a sequência para garantir que só contenha A, T, C, G
    bases_validas = set("ATCG")
    if set(sequencia).issubset(bases_validas):
        return True
    else:
        return False

def comparar_sequencias(seq1, seq2):
    # Compara duas sequências de DNA e retorna as posições dos SNPs (diferenças)
    snps = [(i, seq1[i], seq2[i]) for i in range(min(len(seq1), len(seq2))) if seq1[i] != seq2[i]]
    return snps

def exibir_erro():
    print("Erro: Sequência inválida. Tente novamente.")

def identificar_snps(sequencia1, sequencia2):
    print("Comparando sequências...")
    snps = comparar_sequencias(sequencia1, sequencia2)
    return snps

def armazenar_snps(snps):
    # Armazena as posições e SNPs identificados
    for pos, base1, base2 in snps:
        print(f"SNP identificado na posição {pos}: {base1} -> {base2}")
    return snps

def contar_exibir_resultados(snps):
    # Conta e exibe o número total de SNPs identificados
    print(f"Total de {len(snps)} SNPs identificados.")
    
def salvar_exportar_resultados(snps):
    # Exportar os SNPs para um arquivo (simulação)
    with open("resultados_snps.txt", "w") as f:
        for pos, base1, base2 in snps:
            f.write(f"SNP na posição {pos}: {base1} -> {base2}\n")
    print("Resultados salvos em 'resultados_snps.txt'.")

def fluxo_comparacao():
    # Função principal que simula o fluxo
    while True:
        # Entrada e validação das sequências
        sequencia1 = entrada_sequencias()
        if not validar_sequencia(sequencia1):
            exibir_erro()
            continue

        sequencia2 = entrada_sequencias()
        if not validar_sequencia(sequencia2):
            exibir_erro()
            continue

        # Identificação de SNPs
        snps = identificar_snps(sequencia1, sequencia2)

        # Armazenar e exibir resultados
        armazenar_snps(snps)
        contar_exibir_resultados(snps)

        # Pergunta se quer salvar/exportar
        salvar = input("Deseja salvar/exportar os resultados? (s/n): ").lower()
        if salvar == 's':
            salvar_exportar_resultados(snps)

        # Verificar se deseja comparar novas sequências ou finalizar
        continuar = input("Deseja comparar novas sequências? (s/n): ").lower()
        if continuar != 's':
            break

    print("Processo finalizado.")

# Executa o fluxo de comparação
fluxo_comparacao()
