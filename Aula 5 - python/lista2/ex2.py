#Metodo ensinado em aula
segundos = int(input('Segundos: '))
horas = segundos // 3600
resto = segundos % 3600  
minutos = resto // 60
segundos2 = segundos % 60
print(f'{segundos} segundos corresponde a {horas}, {minutos} minutos e {segundos2} segundos')