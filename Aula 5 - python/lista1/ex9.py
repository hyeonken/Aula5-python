A = int(input('Informe um número inteiro para ser amazenado na variavel A: '))
B = int(input('Informe outro número inteiro para ser armazenado na variavel B: '))
temp = B
B = A
A = temp
print(f'Os valores armazenados nas variaveis A e B, respectivamente: {A} e {B}')