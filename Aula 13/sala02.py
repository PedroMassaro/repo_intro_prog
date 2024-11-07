#!/usr/bin/env python3

import sys

file = ''
try:
   file = sys.argv[1]
   print("User provided file name:", file)

   #Verificar se o arquivo tem a extensão correta
   if not (file.endswith('.fasta') or file.endswith('.fa') or file.endswith('.nt')):
      raise ValueError("O arquivo deve ter uma das seguintes extensões '.fasta', '.fa' ou '.nt'.")

   seq = []
   FASTA = open(file, "r")
   for line in FASTA:
     line = line.rstrip()
     if not line.startswith('>'):
       seq += line

  dic = {}

  with open(file, 'r') as seq:
    for line in seq:
     line = line.rstrip()
     if line.startswith('>'):
      id = line.split(' ')[0]
      id = id[1:]
      if id not in dic.keys():
       dic[id] = ''
     else:
      dic[id] += line.upper()

  count_nt = {}
  for id in dic:
    nts = set(dic[id])
    if id not in count_nt:
      count_nt[id] = {}
    for nt in nts:
      conta = dic[id].count(nt)
      count_nt[id][nt] = conta


  print(count_nt)


   if not any(char in seq for char in 'ARGCN'):
      raise NotARGCN("Error: None of those characters A, R, G, C ou N were found in this sequence.")

#Se uma entrada não é fornercida
except IndexError:
    print("Error: Please provide a file name")
#Se o arquivo não pode ser aberto
except IOError:
    print("Error: Can't find file:", file)
#Se um nenhum character ARGCN é encontrado na  sequência
except NotARGCN:
    print("Error: None of those characters A, R, G, C ou N were found in this sequence.")
else:
    print("Your file was uploaded correctly")
