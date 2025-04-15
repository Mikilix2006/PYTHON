class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def hablar(self):
        print(f"{self.nombre} está hablando...")

class Estudiante(Persona):
    def __init__(self,nombre,edad,nota,curso):
        super().__init__(nombre,edad)
        self.nota = nota
        self.curso = curso
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando...")
    
    def examen(self):
        print(f"{self.nombre} ha sacado un {self.nota}.")

estudiante = Estudiante("Miguel",18,8,"DAW")

print(f"{estudiante.nombre} está en {estudiante.curso}.")
estudiante.estudiar()
estudiante.examen()
