import math

'''
TODO
AÑADIR RECTAS Y SUS FUNCIONES DE DISTANCIAS CON CADA CLASE
'''

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # Distancia punto-punto
    def distanciaHasta(self,otro):
        return ((otro.x-self.x)**2 + (otro.y-self.y)**2)**(1/2)

class Circulo(Punto):
    def __init__(self,x,y,radio):
        super().__init__(x,y)
        self.radio = radio
    
    # Distancia circulo-punto
    def distanciaHastaPunto(self,punto):
        return round(abs(((punto.x-self.x)**2 + (punto.y-self.y)**2)**(1/2)-self.radio),3)
    
    # Distancia circulo-circulo
    def distanciaHastaCirculo(self,circulo):
        return round(abs(((circulo.x-self.x)**2 + (circulo.y-self.y)**2)**(1/2)-self.radio-circulo.radio),3)
    
    def calcularArea(self):
        return math.pi*math.pow(self.radio,2)

    def calcularPerimetro(self):
        return math.pi*2*self.radio
