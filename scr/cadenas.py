

print('Hola mundo')

year = int(input('Entre al año para evaluar (año de 4 cifas:)'))

if year %  4 == 0 and (year % 100 > 0 or year % 400 == 0):
    print(f'El año {year} es bisiesto')
else:
    print(f'El año {year} NO es bisiesto')

