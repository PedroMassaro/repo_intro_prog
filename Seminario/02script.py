# Entrada e validação das sequências
while True:
    # Entrada das sequências
    sequencia1 = input("Insira a primeira sequência de DNA: ").upper()
    
    # Validação da sequência 1
    if not set(sequencia1).issubset(set("ATCG")):
        print("Erro: Sequência inválida. Tente novamente.")
        continue

    sequencia2 = input("Insira a segunda sequência de DNA: ").upper()

    # Validação da sequência 2
    if not set(sequencia2).issubset(set("ATCG")):
        print("Erro: Sequência inválida. Tente novamente.")
        continue

    # Comparação das sequências para identificação de SNPs
    print("Comparando sequências...")
    snps = []
    for i in range(min(len(sequencia1), len(sequencia2))):
        if sequencia1[i] != sequencia2[i]:
            snps.append((i, sequencia1[i], sequencia2[i]))

    # Armazenamento e exibição dos SNPs
    if snps:
        print("SNPs identificados:")
        for pos, base1, base2 in snps:
            print(f"SNP identificado na posição {pos}: {base1} -> {base2}")
    else:
        print("Nenhum SNP identificado.")
    
    # Exibição da contagem de SNPs
    print(f"Total de {len(snps)} SNPs identificados.")

    # Salvar ou exportar os resultados
    salvar = input("Deseja salvar/exportar os resultados? (s/n): ").lower()
    if salvar == 's':
        with open("resultados_snps.txt", "w") as f:
            for pos, base1, base2 in snps:
                f.write(f"SNP na posição {pos}: {base1} -> {base2}\n")
        print("Resultados salvos em 'resultados_snps.txt'.")

    # Verificar se deseja comparar novas sequências ou finalizar
    continuar = input("Deseja comparar novas sequências? (s/n): ").lower()
    if continuar != 's':
        break

print("Processo finalizado.")
