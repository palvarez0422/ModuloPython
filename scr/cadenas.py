

""" print('Hola mundo')

year = int(input('Entre al año para evaluar (año de 4 cifas:)'))

if year %  4 == 0 and (year % 100 > 0 or year % 400 == 0):
    print(f'El año {year} es bisiesto')
else:
    print(f'El año {year} NO es bisiesto') """


columnas = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']

celda = input('Entre la posición del tablaro comenzando por la letra (ejm: A1):').strip().lower()

fila = celda[1]
col = [i + 1 for i, e in enumerate(columnas) if e == celda[0]]

print(f'fila: {fila}, Columna: {col[0]}')

print('Negro' if col[0] % 2 == 0 and fila % 2 == 0 else 'Blanco')

print(col[0] % 2 == 0 and fila % 2 == 0)

