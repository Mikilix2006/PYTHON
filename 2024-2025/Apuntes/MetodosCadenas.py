cadena = "Hola Hola soy Miguel"

#Mayuscula, minuscula y primera mayuscula
mayusc = cadena.upper()
minusc = cadena.lower()
primera_letra_mayusc = cadena.capitalize()

#Busca en que posición esta lo que le pides encontrar
#Si no hay coincidencias devuelve -1
busqueda_find = cadena.find("s")

#Cuenta la cantidad de veces que hay una coincidencia dentro de una cadena
contar_coincidencias = cadena.count("o")

#Cuenta cuantos caracteres hay en la cadena
contar_caracteres = len(cadena)

#Verifica si una cadena empieza por x
empieza_por = cadena.startswith("Hola")

#Verifica si una cadena termina por x
termina_por = cadena.endswith("Miguel")

#Reemplaza un trozo de la cadena por otro (Qué remplazar, por qué reemplazar)
reemplazar_por = cadena.replace("Hola", "Adios")

#Separa cadenas con las cadenas que le des
separar_por = cadena.split(" ")

print(mayusc)
print(minusc)
print(primera_letra_mayusc)
print(busqueda_find)
print(contar_coincidencias)
print(contar_caracteres)
print(empieza_por)
print(termina_por)
print(reemplazar_por)
print(separar_por)
