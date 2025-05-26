from persona import Persona

class Medico(Persona):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad =especialidad

    def datos_doctor(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "especialidad": self.especialidad
        }
