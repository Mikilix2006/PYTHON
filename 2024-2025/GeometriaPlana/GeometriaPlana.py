from Clases import *
from Funciones import *
import os

'''
TODO
HACER FUNCION PARA COMPROBAR SI 3 PUNTOS ESTAN ALINEADOS O NO
REFACTORIZAR:
    BLOQUES -> MÉTODOS
    DOCUMENTAR MÉTODOS
    OPTIMIZAR
BUG
EN OPCION 4 SI HAY UNA LISTA VACIA Y QUIERES QUITAR OBJETOS DE ELLA SE QUEDA EN BUCLE
'''

# SEGUN EL SISTEMA OPERATIVO
if os.name == "nt":
    limpiar = "cls"
elif os.name == "posix":
    limpiar = "clear"

os.system(limpiar)

circulos = []
puntos = []
programaActivo = True

while programaActivo:
    eleccionMenu = mostrarMenu()
    os.system(limpiar)
    # METER OBJETO EN LISTA
    if eleccionMenu == 1:
        eleccionOpc1 = mostrarOpcion1()
        if eleccionOpc1 == 1:
            # METER PUNTOS EN UNA LISTA
            puntos = pedirPuntos(puntos)
        elif eleccionOpc1 == 2:
            # METER CIRCULOS EN UNA LISTA
            circulos = pedirCirculos(circulos)
        elif eleccionOpc1 == 3:
            # SALIR AL MENU
            os.system(limpiar)
            eleccionOpc1 = 0
            eleccionMenu = 0
    
    # VER LISTAS
    elif eleccionMenu == 2:
        eleccionOpc2 = mostrarOpcion2()
        os.system(limpiar)
        if eleccionOpc2 == 1:
            # VER LISTA PUNTOS
            try:
                mostrarPuntosEnLista(puntos)
            except:
                print("No hay puntos suficientes en la lista")
        elif eleccionOpc2 == 2:
            # VER LISTA CIRCULOS
            try:
                mostrarCirculosEnLista(circulos)
            except:
                print("No hay círculos suficientes en la lista")
        elif eleccionOpc2 == 3:
            # SALIR AL MENU
            os.system(limpiar)
            eleccionOpc2 = 0
            eleccionMenu = 0
        
    # CALCULAR DISTANCIAS
    elif eleccionMenu == 3:
        eleccionOpc3 = mostrarOpcion3()
        if eleccionOpc3 == 1:
            # DISTANCIA ENTRE PUNTOS
            try:
                os.system(limpiar)
                distanciaEntrePuntos(puntos)
            except:
                print("No hay puntos suficientes en la lista")
        elif eleccionOpc3 == 2:
            # DISTANCIA ENTRE CIRCULOS
            try:
                os.system(limpiar)
                distanciaEntreCirculos(circulos)
            except:
                print("No hay círculos suficientes en la lista")
        elif eleccionOpc3 == 3:
            # DISTANCIA ENTRE CIRCULO Y PUNTO
            try:
                os.system(limpiar)
                distanciaCirculoPunto(puntos,circulos)
            except:
                print("No hay puntos o círculos suficientes en las listas")
        elif eleccionOpc3 == 4:
            # SALIR AL MENU
            os.system(limpiar)
            eleccionOpc3 = 0
            eleccionMenu = 0
        
    # QUITAR OBJETO DE LISTA
    elif eleccionMenu == 4:
        eleccionOpc4 = mostrarOpcion4()
        if eleccionOpc4 == 1:
            if len(puntos) > 0:
                # QUITAR PUNTOS
                os.system(limpiar)
                puntos = quitarPunto(puntos)
            else:
                print ("No hay suficientes puntos")
        elif eleccionOpc4 == 2:
            if len(circulos) > 0:
                # QUITAR CÍRCULOS
                os.system(limpiar)
                circulos = quitarCirculo(circulos)
            else:
                print ("No hay suficientes circulos")
        elif eleccionOpc4 == 3:
            # SALIR AL MENU
            os.system(limpiar)
            eleccionOpc4 = 0
            eleccionMenu = 0
    
    # SALIR
    elif eleccionMenu == 5:
        programaActivo = False

print("Programa finalizado")
