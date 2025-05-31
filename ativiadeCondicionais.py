print(bool('oi'))
dados = {
    'projeto_1': input('sucesso ou falha?>>'),
    'projeto_2': input('sucesso ou falha?>>'),
    'projeto_3': input('sucesso ou falha?>>')

}

custo = {
    'projeto_1': float(input('quanto custou?>>')),
    'projeto_2': float(input('quanto custou?>>')),
    'projeto_3': float(input('quanto custou?>>'))
}

registros = {
    'nome1': 'kaicke',
    'nome2': 'laila',
    'nome3': 'rafael'
}
print('''
1 - mostra o dado
2 - alterar dado
3 - coletar rersultado de um dado  
4 - soma de dados
5 - localizar registro no conjunto de dados

''')
escolha = int(input('escolha qual irá fazer>>'))

if escolha == 1:
    dado = input('escolha o dado que quer ver: projeto_1, projeto_2, projeto_3>>')
    print(dados[dado])
elif escolha == 2:
    dado = input('escolha o dado que quer ver: projeto_1, projeto_2, projeto_3>>')
    dados[dado] = input('escreva se o projeto foi um suceso ou se ele fracassou')
    print('dado alterado com sucesso')
    print(dados)
elif escolha == 3:
    preco = input('escolha um projeto para ver o custo: projeto_1, projeto_2, projeto_3>>')
    print(custo[preco])
elif escolha == 4:   
     dado1 = input('escolha um projeto para soma de custos: projeto_1, projeto_2, projeto_3>>')
     dado2 = input('escolha outro projeto para soma de custos: projeto_1, projeto_2, projeto_3>>')
     print(f'a soma dos custos é:   {custo[dado1] + custo[dado2]}')
elif escolha == 5:
     nome = input('digite: nome1, nome2, nome3>>')
     if bool(registros[nome]) == True :
        print(registros[nome])
     else:
        print('não existe')
else:
    print('isso não existe')