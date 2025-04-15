class Estudiante:
    
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando.")

nombre = input("Nombre del estudiante: ")
edad = int(input(f"Edad de {nombre}: "))
grado = input(f"Grado de {nombre}: ")

estudiante1 = Estudiante(nombre, edad, grado)

estudiante1.estudiar()
