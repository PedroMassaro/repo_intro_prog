#!/usr/bin/env python3

mensagem = '' # cria uma variável vazia
for x in (1,2,3,4,5): #Construindo um loop
	if x > 4:
		print("Olá")
		mensagem = 'x é grande'
	else:
		print(x)
		mensagem = 'x é pequeno'

print(mensagem)
print('Pronto!')
