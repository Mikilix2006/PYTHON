class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def hablar(self):
        print(f"{self.nombre} está hablando...")

class Artista:
    def __init__(self,obra):
        self.obra = obra
    
    def pintar(self):
        print(f"Pintando \"{self.obra}\"...")

class EmpleadoArtista(Persona, Artista):
    def __init__(self,nombre,edad,sexo,obra,salario):
        Persona.__init__(self,nombre,edad,sexo)
        Artista.__init__(self,obra)
        self.salario = salario
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando...")
        
    def cobrar(self):
        print(f"{self.nombre} ha cobrado {self.salario}€ al final del año.")

empleado = EmpleadoArtista("Miguel",18,"Hombre","El cali",60000)

empleado.hablar()
empleado.pintar()
empleado.trabajar()
empleado.cobrar()
