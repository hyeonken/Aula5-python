# metodo que aprendemos em sala
numero = int(input('Digite um número inteiro de 3 digitos: '))   # 136
num_invertido = (numero // 100)                  # 1
num_invertido2 = (numero % 100)                  # 36
num_invertido3 = (num_invertido2 // 10)          # 3
num_invertido4 = (num_invertido2 % 10)                #6
print(f'Número invertido: {num_invertido4}{num_invertido3}{num_invertido}')