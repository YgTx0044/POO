from persona import Persona

class Medico(Persona):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad =especialidad

    def ver_reporte_paciente(self, nombre):
        pass

    def crear_reporte(self, diagnostico, medicamentos):
        pass

    def datos_doctor(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "especialidad": self.especialidad
        }
    
