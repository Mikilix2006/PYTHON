from Clases import *
import os

# SEGUN EL SISTEMA OPERATIVO
if os.name == "nt":
    limpiar = "cls"
elif os.name == "posix":
    limpiar = "clear"

# Método para crear un nuevo punto con datos del usuario
def nuevoPunto():
    x = asegurarValorEntero("Introduce la coordenada x del punto:\n")
    y = asegurarValorEntero("Introduce la coordenada y del punto:\n")
    return Punto(x,y)

# Método que devuelve una lista con nuevos puntos introducidos por el usuario
def pedirPuntos(puntos):
    sacarPunto = True
    while sacarPunto:
        resp = input("Añadir nuevo punto a la lista? y/n:\n").upper()
        
        if resp == "Y":
            os.system(limpiar)
            puntos.append(nuevoPunto())
        elif resp == "N":
            os.system(limpiar)
            sacarPunto = False
        else:
            os.system(limpiar)
            print("Respuesta no reconocida")
            
    return puntos

# Método que muestra ordenadamente los puntos de una lista
def mostrarPuntosEnLista(lista):
    print("\nPuntos en la lista:")
    for i in range(len(lista)):
        print(f"P{i+1}: ({lista[i].x},{lista[i].y})")
    else:
        print("")

# Método que muestra distancias entre puntos que el usuario quiera
def distanciaEntrePuntos(lista):
    if len(lista) > 1:
        res = True
        while res:
            res = input("¿Quieres saber alguna distancia entre puntos?(y/n):\n").upper()
            os.system(limpiar)
            if res == "Y":
                if len(lista) == 2:
                    mensajeDistancia(lista[0],lista[1])
                    res = False
                else:
                    mostrarPuntosEnLista(lista)
                    print("Entre que puntos quieres saber su distancia?(introduce número del punto)")
                    punto1 = asegurarValorEnteroLimitado("Primer punto:\n",len(lista))-1
                    punto2 = asegurarValorEnteroLimitado("Segundo punto:\n",len(lista))-1
                    mensajeDistancia(lista[punto1],lista[punto2])
                    res = True
            elif res == "N":
                res = False
            else:
                print("Respuesta no reconocida")
    else:
        print("No hay puntos suficientes para calcular distancia entre ellos")
        
# Método que pide al usuario datos para crear un circulo
def nuevoCirculo():
    x = asegurarValorEntero("Introduce la coordenada x del centro:\n")
    y = asegurarValorEntero("Introduce la coordenada y del centro:\n")
    radioExistente = False
    while not radioExistente:
        radio = asegurarValorEntero("Introduce el valor del radio:\n")
        if not radio <= 0:
            radioExistente = True
        else:
            os.system(limpiar)
            print(f"Valor del radio inexistente: {radio}")
    return Circulo(x,y,radio)

# Método que pide al usuario confirmación para meter circulos a una lista
def pedirCirculos(circulos):
    sacarCirculo = True
    while sacarCirculo:
        resp = input("Añadir nuevo circulo a la lista? y/n:\n").upper()

        if resp == "Y":
            os.system(limpiar)
            circulos.append(nuevoCirculo())
        elif resp == "N":
            os.system(limpiar)
            sacarCirculo = False
        else:
            os.system(limpiar)
            print("Respuesta no reconocida")
        
    return circulos

# Método que muestra los circulos de una lista
def mostrarCirculosEnLista(lista):
    print("\nCírculos en la lista:")
    for i in range(len(lista)):
        print(f"C{i+1}: centro en ({lista[i].x},{lista[i].y}) radio: {lista[i].radio} u")
    else:
        print("")

def distanciaEntreCirculos(lista):
    if len(lista) > 1:
        res = True
        while res:
            res = input("¿Quieres saber alguna distancia entre circulos?(y/n):\n").upper()
            os.system(limpiar)
            if res == "Y":
                if len(lista) == 2:
                    mensajeDistancia(lista[0],lista[1])
                    res = False
                else:
                    mostrarCirculosEnLista(lista)
                    print("Entre que circulos quieres saber su distancia?(introduce número del circulo)")
                    circulo1 = asegurarValorEnteroLimitado("Primer circulo:\n",len(lista))-1
                    circulo2 = asegurarValorEnteroLimitado("Segundo circulo:\n",len(lista))-1
                    mensajeDistancia(lista[circulo1],lista[circulo2])
                    res = True
            elif res == "N":
                res = False
            else:
                print("Respuesta no reconocida")
    else:
        print("No hay círculos suficientes para calcular distancia entre ellos")

def asegurarValorEnteroLimitado(mensaje, valorMaximo):
    correcto = False
    while not correcto:
        try:
            valor = int(input(mensaje))
            if  valor > valorMaximo or valor < 1:
                raise Exception("")
            correcto = True
        except:
            os.system(limpiar)
            print("Valor introducido incorrecto")
    return valor

def asegurarValorEntero(mensaje):
    correcto = False
    while not correcto:
        try:
            valor = int(input(mensaje))
            correcto = True
        except:
            os.system(limpiar)
            print("Valor introducido incorrecto")
    return valor

# Método que muestra un mensaje sobre la distancia entre dos objetos dados segun sus tipos
def mensajeDistancia(obj1, obj2):
    if type(obj1) == Punto and type(obj2) == Punto:
        print(f"La distancia desde ({obj1.x},{obj1.y}) hasta ({obj2.x},{obj2.y}) es de {obj1.distanciaHasta(obj2)} unidades")
    elif type(obj1) == Circulo and type(obj2) == Circulo:
        print(f"La distancia desde centro ({obj1.x},{obj1.y}) hasta centro ({obj2.x},{obj2.y}) es de {obj1.distanciaHastaCirculo(obj2)} unidades")
    elif type(obj1) == Circulo and type(obj2) == Punto:
        print(f"La distancia desde centro ({obj1.x},{obj1.y}) hasta centro ({obj2.x},{obj2.y}) es de {obj1.distanciaHastaPunto(obj2)} unidades")
    elif type(obj1) == Punto and type(obj2) == Circulo:
        objAux = obj1
        obj1 = obj2
        obj2 = objAux
        print(f"La distancia desde centro ({obj1.x},{obj1.y}) hasta centro ({obj2.x},{obj2.y}) es de {obj1.distanciaHastaPunto(obj2)} unidades")

@staticmethod
def mostrarMenu():
    return asegurarValorEnteroLimitado('''=== MENÚ ===\n1. METER OBJETO EN LISTA\n2. VER LISTAS\n3. CALCULAR DISTANCIAS\n4. QUITAR OBJETO DE LISTA\n5. SALIR DEL PROGRAMA\n''',5)

@staticmethod
def mostrarOpcion1():
    return asegurarValorEnteroLimitado('''=== METER OBJETO EN LISTA ===\n1. METER PUNTOS EN UNA LISTA\n2. METER CIRCULOS EN UNA LISTA\n3. MENÚ\n''',3)

@staticmethod
def mostrarOpcion2():
    return asegurarValorEnteroLimitado('''=== VER LISTA ===\n1. VER LISTA DE PUNTOS\n2. VER LISTA DE CÍRCULOS\n3. MENÚ\n''',3)

@staticmethod
def mostrarOpcion3():
    return asegurarValorEnteroLimitado('''=== CALCULAR DISTANCIA ===\n1. DISTANCIA ENTRE PUNTOS\n2. DISTANCIA ENTRE CÍRCULOS\n3. DISTANCIA PUNTO-CÍRCULO\n4. MENÚ\n''',4)

@staticmethod
def mostrarOpcion4():
    return asegurarValorEnteroLimitado('''=== QUITAR OBJETO DE LISTA ===\n1. QUITAR PUNTOS\n2. QUITAR CÍRCULOS\n3. MENÚ\n''',3)

@staticmethod
def distanciaCirculoPunto(lista1,lista2):
    if len(lista1) == 0 or len(lista2) == 0:
        print("No hay elementos suficientes en las listas como para calcular distancias")
    else:
        mostrarPuntosEnLista(lista1)
        mostrarCirculosEnLista(lista2)
        pun = asegurarValorEnteroLimitado("¿Desde qué punto quieres calcular la distancia?",len(lista1))-1
        cir = asegurarValorEnteroLimitado("¿Hasta qué círculo quieres calcular la distancia?",len(lista2))-1
        mensajeDistancia(lista1[pun],lista2[cir])

def quitarPunto(lista):
    correcto = False
    while not correcto:
        try:
            mostrarPuntosEnLista(lista)
            punto = int(input("¿Qué punto quieres quitar?\n"))-1
            if punto < 0 or punto > len(lista)-1:
                raise Exception("")
            correcto = True
        except:
            os.system(limpiar)
            print(f"Valor incorrecto: {punto}")
    lista.pop(punto)
    return lista

def quitarCirculo(lista):
    correcto = False
    while not correcto:
        try:
            mostrarCirculosEnLista(lista)
            circ = int(input("¿Qué círculo quieres quitar?\n"))-1
            if circ < 0 or circ > len(lista)-1:
                raise Exception("")
            correcto = True
        except:
            os.system(limpiar)
            print(f"Valor incorrecto: {circ}")
    lista.pop(circ)
    return lista
