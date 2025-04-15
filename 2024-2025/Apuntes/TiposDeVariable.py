#FORMATOS
num = 5
#Para adaptar el tipo de variable:
man = f"Tengo {num} manzanas"
#Borrar variable:
del num

print(man)


#MODIFICAR DATOS DE UNA LISTA
lista = ["Hola", True, 5, 3.4]
lista[1] = False

print(lista)

#CONJUNTO (set)
conjunto = {"Hola", True, 5, 3.4}

#DICCIONARIO
diccionario = {
    "nombre" : "Miguel",
    "apellido" : "Glezz",
    "altura": 1.70,
    "estudiando": True
}

print(diccionario["altura"] + 2)
