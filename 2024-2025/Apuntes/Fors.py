'''
range() ayuda a iterar por números.
enumerate() da índices y zip() combina listas.
for-else se ejecuta si no hay break.
Se pueden anidar bucles.
'''

# Output: 1 2 3 4 5 6
numeros = [1,2,3,4,5,6]
for num in numeros:
    print(num)

# Output: M i g u e l o n
palabra = "Miguelon"
for letra in palabra:
    print(letra)

# Output: nombre : Juan \n edad : 30
# Output: nombre -> Juan \n edad -> 30
datos = {"nombre": "Juan", "edad": 30}
for dato in datos:
    print(dato, ':', datos[dato])
for dato, valor in datos.items():
    print(dato, '->', valor)

# Output: 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# Output: 2 3 4 5
for i in range(2, 6):
    print(i)
    
# Output: 2 4 6
for i in range(2, 7, 2):
    print(i)

# Output: 10 9 8 7 6 5 4 3 2 1
for i in range(10, 0, -1):
    print(i)

# Output: 1 : Ana
#         2 : Luis
#         3 : Carlos
nombres = ["Ana", "Luis", "Carlos"]
for i, nombre in enumerate(nombres):
    print(f"Índice {i}: {nombre}")

# Output: Ana tiene 25 años
#         Luis tiene 30 años
#         Carlos tiene 22 años
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# Imprime los numeros y al terminar ejecuta el else
for num in range(5):
    print(num)
else:
    print("Finalizado sin interrupciones")

# Imprime los numeros y al cuando se alcance el 2 sale del for sin ejecutar el else
for num in range(5):
    print(num)
    if num == 2:
        break
else:
    print("Esto no se imprimirá")

# Fors anidados
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
