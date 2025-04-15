lista = ["Hola", "Adios", 23, True, "Equisde"]
lista2 = [213, 345, 546, 457,True, False, 12, 435]

#Cuenta la cantidad de elementos de una lista
cantidad_elementos = len(lista)

#Agrega elementos a la lista
lista.append(33)

#Agrega elementos a la lista donde le digas
lista.insert(2, "JIJIJIJA")

#Elimina elementos de la lista donde le digas, si pones numeros negativos, eliminas de derecha a izquierda
lista.pop(-1)

#Elimina elementos de la lista según le des
lista.remove(23)

#Elimina todos los elementos de la lista
#lista.clear()

#Da la vuelta a la lista sin ordenarla de ninguna manera
lista2.reverse()
print(lista2)

#Ordena los elementos numéricos y booleanos de una lista de menor a mayor, empezando por los booleanos
lista2.sort()
print(lista2)
lista2.sort(reverse=True)
print(lista2)


print(cantidad_elementos)
print(lista)