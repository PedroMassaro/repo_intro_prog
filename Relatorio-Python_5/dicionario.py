#!/usr/bin/env python3

#Resolução dos exercícios 1 ao 9 - Relatório_Python 5:

#01 - Escreva um script no qual você construa um dicionário de suas coisas favoritas
#Construção do dicionário com minhas coisas favoritas
fav_dict = {
    'livro': 'Reed Hastings - A regra é não ter regras',
    'som': 'Imagine Dragons - Radioactive',
    'árvore': 'Araucária'
}

print(f'Exercício 01 - Dicionário com minhas coisas favoritas:\n{fav_dict}\n')

#02 - Print o seu livro favorito
print(f'Exercício 02 - Print o meu livro favorito:\n{fav_dict['livro']}\n')

#03 - Print o seu livro favorito, mas use uma variável na chave
fav_thing = 'livro'
print('Exercício 03 - Print o seu livro favorito, mas use uma variável na chave:')
print(fav_dict[fav_thing])

#04 - Agora print a sua árvore favorita
print(f'\nExercício 04 - Print minha árvore favorita:\n{fav_dict['árvore']}\n')

#05 - Adicione o seu "organismo" favorito ao dicionário. Faça com que "organismo" seja o novo valor da chave fav_thing
#Adicionando meu organismo favorito ao dicionário
fav_dict['organismo'] = 'Peixe'
#Print do organismo favorito
fav_thing = 'organismo'

print('Exercício 05 - Adicionando meu organismo favorito ao dicionário e imprimindo ele na tela de comando:')
print(fav_dict[fav_thing])

#06 - Obtenha um valor da linha de comando para fav_thing e print o valor desse item do dicionário. Talvez você queira imprimir todas as chaves para o usuário, para que eles saibam o que escolher. Dê uma olhada em input()
#Exibindo todas as chaves do dicionário
print("\nExercício 06 - Escolha uma das categorias abaixo para ver sua favorita:")
for chave in fav_dict.keys():
    print(chave)

#Input - Escolha da chave favorita
fav_thing = input("\nDigite o nome da categoria que você quer que seja sua favorita: ").lower()

#Verificando se a chave escolhida está presente no dicionário, caso não, emitindo mensagem de erro
if fav_thing in fav_dict:
    print(f'A seu(a) {fav_thing} favorito(a) é: {fav_dict[fav_thing]}\n')
else:
    print(f'Categoria "{fav_thing}" não encontrada, selecione uma das categorias pontuadas acima.\n')

#07 - Altere o valor do seu organismo favorito
fav_dict['organismo'] = 'Urso'
print(f'Exercício 07 - Mudança do organismo favorito para "Urso":\norganismo - {fav_dict["organismo"]}\n')

#08 - Obtenha fav_thing da linha de comando e um novo valor para essa chave. Altere o valor com o valor inserido pelo usuário
print('Exercício 08 - Escolha uma das categorias abaixo para mudar seu objeto favorito:')
for chave in fav_dict.keys():
    print(chave)

fav_thing = input('\nDigite o nome da categoria realizar a mudança: ').lower()
fav_obj = input('Digite o seu novo objeto favorito para essa categoria favorita: ').lower()

fav_dict[fav_thing] = fav_obj

print(f'{fav_thing} - {fav_dict[fav_thing]}\n')

#09 - Use um loop for para imprimir cada chave e valor do dicionário.
print('Exercício 09 - Imprimindo o dicionário final obtido:')
print('Classe          Objeto favorito')
for chave in fav_dict.keys():
 print(f'{chave:<15} {fav_dict[chave]:<15}')


