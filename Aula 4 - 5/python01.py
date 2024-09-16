#!/usr/bin/env python3

#print("Meu nome: Sofia")
#print("Minha cor favorita: Verde")

#atividade = "Cordar"
#print("Minha atividade favorita:" , atividade)

#ani = "Galinha"
#print("Meu animal favorito:" , ani)

import sys

if len(sys.argv) != 5:
    print("Uso: python script.py <nome> <cor_favorita> <atividade_favorita> <animal_favorito>")
    sys.exit(1)

nome = sys.argv[1]
cor_favorita = sys.argv[2]
atividade_favorita = sys.argv[3]
animal_favorito = sys.argv[4]

print("Nome:", nome + ",", "Cor favorita:", cor_favorita + ",", "Atividade favorita:", atividade_favorita + ",", "Animal favorito:", animal_favorito)
#print("Nome:", nome, ",", "Cor favorita:", cor_favorita, ",", "Atividade favorita:", atividade_favorita, ",", "Animal favorito:", animal_favorito)
