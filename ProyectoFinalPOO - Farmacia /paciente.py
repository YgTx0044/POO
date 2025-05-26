from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, edad, genero, estatura, peso, curp, sintomas):
        super().__init__(nombre, edad, genero)
        self.estatura = estatura
        self.peso = peso
        self.curp = curp
        self.sintomas = sintomas

    def datos_paciente(self):
            return {
                "nombre": self.nombre,
                "edad": self.edad,
                "genero": self.genero,
                "peso": self.peso,
                "estatura": self.estatura,
                "curp": self.curp,
                "sintomas": self.sintomas
            }
