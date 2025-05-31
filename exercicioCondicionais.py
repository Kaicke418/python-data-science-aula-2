frequencia =  [10,3,3,5,6,6]

escolha = int(input('''
Digite: 

1 - Mostra o dado
2 - Alterar o dado
3 - coletar dado
4 - soma de dados
---
'''))
if escolha  ==  1:
    print('dados:', frequencia)

elif escolha  == 2:
     novo_dado = int(input('digite o dado: '))
     alterar = int(input('Digite a localização: '))
     frequencia[alterar] = novo_dado
     print(frequencia)                                 
else:
    print('Essa opção não existe')       
