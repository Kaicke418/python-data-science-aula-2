# simples 


if 10<2:
    print('teste')


if 10>2:
    print('teste2')    



# composto


if 10 < 2:
    print('teste')
else:
    print('teste2') 



# composto com elif



if 10 == 100:
    print('Teste 1')
elif 10 == 10:
    print('teste2')
elif 10 == 2:
    print('teste2.1')    
else:
    print('teste3')        




# operadores and or not 


situacao_ipva = input('Digite a situação: ') 
multas  =  int(input('Digite a quantidade: '))


if not multas > 0 and situacao_ipva == 'pago' :
    print('Parabéns')
else:
    print('Precisa pagar')    

if input('você quer pagar? sim/não>>') == 'sim':
    print('pago')                                     
else:
    print('vai conrinuar devendo até pagars')




