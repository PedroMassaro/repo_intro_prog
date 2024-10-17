#!/usr/bin/env python3


#10 - Crie um conjunto usando as duas sintaxes diferentes para criar um conjunto, myset = set() e myset2 = {}. Qual é a diferença? Importa como você cria o conjunto?
#Criando conjuntos com duas sintaxes diferentes
mySet = set('ATGTGGG') #Isso criará um conjunto onde cada caractere individualmente será tratado como um elemento do conjunto
mySet2 = {'ATGCCT'} #Essa criará um conjunto, no entanto com um único elemento que é a string inteira

print('Exercício 10 - Criando um conjunto a partir de duas sintaxes diferentes:')
print(f'{mySet} - set() cria um conjunto onde cada caractere individualmente será tratado como um elemento do conjunto')
print(f'{mySet2} - {{}} cria um conjunto, no entanto com um único elemento que é a string inteira. Logo, importa como se cria o conjunto')

#11 - Escreva um script para encontrar a interseção, diferença, união e diferença simétrica entre esses dois conjuntos
#Definindo os conjuntos
set_A = set([3, 14, 15, 9, 26, 5, 35, 9])
set_B = set([60, 22, 14, 0, 9])

# Calculando a interseção (elementos presentes em ambos os conjuntos)
inter = set_A & set_B

# Calculando a diferença (elementos em A que não estão em B)
diff_A_B = set_A - set_B

# Calculando a união (todos os elementos de A e B)
union = set_A | set_B

# Calculando a diferença simétrica (elementos que estão em A ou B, mas não em ambos)
sym_diff = set_A ^ set_B

# Exibindo os resultados
print(f'\nExercício 11 - Operações com conjuntos:\nInterseção: {inter}\nDiferença (A - B): {diff_A_B}\nUnião: {union}\nDiferença Simétrica: {sym_diff}')
