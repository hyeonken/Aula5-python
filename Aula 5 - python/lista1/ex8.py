import os # Import os é para limpar o console depois de executar uma parte para ficar mais limpo.


nome = str(input('Informe seu nome: '))
carros = int(input('Informe a quantidade de carros vendidos: '))
valortotal = float(input('Informe o valor total de vendas: '))

os.system('cls' if os.name=='nt' else 'clear') # Resto do import os, deixando a experiencia final mais limpa para testes.


print(f'Nome do vendedor: {nome}')
print(f'Quantidades de carros vendidos: {carros}')
print(f'Valor total de vendas: {valortotal}')
print(f'O vendedor {nome} receberá um salário total de: {valortotal * 0.02 + 200 * carros + 2500}')