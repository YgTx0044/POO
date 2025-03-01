class Persona:
    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

class Cliente(Persona):
    def __init__(self, nombre, correo, telefono, contrasena):
        super().__init__(nombre, correo, telefono)
        self.__contrasena = contrasena
        self.__reservas = []  # Lista para almacenar reservas del cliente

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def registrar_cliente(self):
        print(f"Registrando cliente: {self.get_nombre()}")

    def iniciar_sesion(self, correo, contrasena):
        # Compara correo y contraseña
        return self.get_correo() == correo and self.__contrasena == contrasena

    def modificar_datos(self, nombre, correo, telefono):
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    def consultar_reservas(self):
        print("Consultando reservas...")
        return self.__reservas  # Retorna la lista de reservas

    def cancelar_reservas(self, codigo):
        print(f"Cancelando reserva con código: {codigo}")

class Notificaciones(Persona):
    def __init__(self, correo_cliente, mensaje):
        super().__init__(None, correo_cliente, None)
        self.__mensaje = mensaje

    def get_mensaje(self):
        return self.__mensaje

    def set_mensaje(self, mensaje):
        self.__mensaje = mensaje

    def enviar_correo(self):
        print(f"Enviando correo a: {self.get_correo()}")

    def generar_notificacion(self):
        print(f"Generando notificación: {self.__mensaje}")

class Pelicula:
    def __init__(self, titulo, genero, duracion, clasificacion, formatos_disponibles):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracion = duracion
        self.__clasificacion = clasificacion
        self.__formatos_disponibles = formatos_disponibles
        self.__reservas = []  # Lista para almacenar reservas de la película

    # Métodos getters
    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_duracion(self):
        return self.__duracion

    def get_clasificacion(self):
        return self.__clasificacion

    def get_formatos_disponibles(self):
        return self.__formatos_disponibles

    # Métodos setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_clasificacion(self, clasificacion):
        self.__clasificacion = clasificacion

    def registrar_pelicula(self):
        print(f"Registrando película: {self.__titulo}")

    def modificar_datos_pelicula(self, titulo, genero, duracion, clasificacion):
        self.set_titulo(titulo)
        self.set_genero(genero)
        self.set_duracion(duracion)
        self.set_clasificacion(clasificacion)
        print(f"Modificando datos de la película: {self.__titulo}")

    def consultar_peliculas(self):
        print("Consultando películas disponibles...")

    def agregar_reserva(self, reserva):
        self.__reservas.append(reserva)

    def obtener_reservas(self):
        return self.__reservas  # Retorna la lista de reservas

class Sala:
    def __init__(self, numero, capacidad, formato):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__formato = formato
        self.__reservas = []  # Lista para almacenar reservas de la sala

    # Métodos getters
    def get_numero(self):
        return self.__numero

    def get_capacidad(self):
        return self.__capacidad

    def get_formato(self):
        return self.__formato

    # Métodos setters
    def set_numero(self, numero):
        self.__numero = numero

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def set_formato(self, formato):
        self.__formato = formato

    def registrar_sala(self):
        print(f"Registrando sala: {self.__numero}")

    def consultar_salas_disponibles(self):
        print("Consultando salas disponibles...")

    def agregar_reserva(self, reserva):
        self.__reservas.append(reserva)

    def obtener_reservas(self):
        return self.__reservas  # Retorna la lista de reservas

from datetime import date, time

class Horario:
    def __init__(self, fecha, hora, sala):
        self.__fecha = fecha
        self.__hora = hora
        self.__sala = sala
        self.__reservas = []  # Lista para almacenar reservas del horario

    # Métodos getters
    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_sala(self):
        return self.__sala

    # Métodos setters
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_hora(self, hora):
        self.__hora = hora

    def set_sala(self, sala):
        self.__sala = sala

    def registrar_horario(self, fecha, hora, sala):
        print(f"Registrando horario: {fecha} a las {hora} en la sala {sala.get_numero()}")

    def validar_empalmes(self, sala, fecha, hora):
        print("Validando empalmes para la sala:", sala.get_numero())
        return True

    def consultar_horarios_disponibles(self):
        print("Consultando horarios disponibles...")
        return []

    def agregar_reserva(self, reserva):
        self.__reservas.append(reserva)

    def obtener_reservas(self):
        return self.__reservas  # Retorna la lista de reservas

class Reserva:
    def __init__(self, codigo, cliente, pelicula, sala, horario, numero_boletos):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__pelicula = pelicula
        self.__sala = sala
        self.__horario = horario
        self.__numero_boletos = numero_boletos
        self.__notificaciones = []  # Lista para almacenar notificaciones de la reserva

    # Métodos getters
    def get_codigo(self):
        return self.__codigo

    def get_cliente(self):
        return self.__cliente

    def get_pelicula(self):
        return self.__pelicula

    def get_sala(self):
        return self.__sala

    def get_horario(self):
        return self.__horario

    def get_numero_boletos(self):
        return self.__numero_boletos

    # Métodos setters
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_pelicula(self, pelicula):
        self.__pelicula = pelicula

    def set_sala(self, sala):
        self.__sala = sala

    def set_horario(self, horario):
        self.__horario = horario

    def set_numero_boletos(self, numero):
        self.__numero_boletos = numero

    def crear_reserva(self):
        print(f"Creando reserva con código: {self.__codigo}")
        self.__pelicula.agregar_reserva(self)
        self.__sala.agregar_reserva(self)
        self.__horario.agregar_reserva(self)
        self.__cliente.consultar_reservas().append(self)

    def modificar_reserva(self):
        print(f"Modificando reserva con código: {self.__codigo}")

    def cancelar_reserva(self):
        print(f"Cancelando reserva con código: {self.__codigo}")
        self.__notificaciones.append(Notificaciones(self.__cliente.get_correo(), f"Reserva {self.__codigo} cancelada"))

    def verificar_disponibilidad_asientos(self):
        print("Verificando disponibilidad de asientos...")
        return True

    def generar_codigo(self):
        import uuid
        self.__codigo = str(uuid.uuid4())
        print(f"Código generado para la reserva: {self.__codigo}")

    def agregar_notificacion(self, notificacion):
        self.__notificaciones.append(notificacion)

    def obtener_notificaciones(self):
        return self.__notificaciones  # Retorna la lista de notificaciones

class ReporteVentas:
    def __init__(self, fecha_inicio, fecha_fin, total_ventas):
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__total_ventas = total_ventas
        self.__peliculas = []  # Lista para almacenar las películas en el reporte
        self.__horarios = []   # Lista para almacenar los horarios en el reporte

    # Métodos getters
    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin

    def get_total_ventas(self):
        return self.__total_ventas

    # Métodos setters
    def set_fecha_inicio(self, fecha):
        self.__fecha_inicio = fecha

    def set_fecha_fin(self, fecha):
        self.__fecha_fin = fecha

    def set_total_ventas(self, total):
        self.__total_ventas = total

    def agregar_pelicula(self, pelicula):
        self.__peliculas.append(pelicula)

    def obtener_peliculas(self):
        return self.__peliculas  # Retorna la lista de películas en el reporte

    def agregar_horario(self, horario):
        self.__horarios.append(horario)

    def obtener_horarios(self):
        return self.__horarios  # Retorna la lista de horarios en el reporte


def main():
    # Crear una instancia de Cliente
    cliente1 = Cliente("Juan Pérez", "juan@example.com", "123456789", "pass123")
    cliente1.registrar_cliente()

    # Intentar iniciar sesión
    if cliente1.iniciar_sesion("juan@example.com", "pass123"):
        print("Inicio de sesión exitoso")
    else:
        print("Fallo en el inicio de sesión")

    # Modificar datos del cliente
    cliente1.modificar_datos("Juan P.", "juanp@example.com", "987654321")
    print(f"Cliente modificado: {cliente1.get_nombre()}, {cliente1.get_correo()}, {cliente1.get_telefono()}")

    # Crear y registrar una película
    pelicula1 = Pelicula("Matrix", "Ciencia Ficción", 136, "PG-13", ["2D", "3D"])
    pelicula1.registrar_pelicula()

    # Crear una reserva
    sala1 = Sala(1, 100, "2D")
    horario1 = Horario(date(2023, 3, 15), time(20, 0), sala1)
    reserva1 = Reserva("R123", cliente1, pelicula1, sala1, horario1, 2)
    reserva1.crear_reserva()

    # Consultar reservas del cliente
    reservas_cliente = cliente1.consultar_reservas()
    for reserva in reservas_cliente:
        print(f"Reserva: {reserva.get_codigo()}, Película: {reserva.get_pelicula().get_titulo()}")

if __name__ == "__main__":
    main()
