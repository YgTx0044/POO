from medico import Medico
from manejo_medicos import ver_medicos, agregar_medico, eliminar_medico
from inventario import Inventario
from manejo_inventario import agregar_medicamento, eliminar_medicamento, ver_inventario, vender_medicamento, modificar_precio, modificar_stock
from manejo_citas import ver_citas, registrar_cita, cargar_citas, eliminar_cita
from manejo_reportes import generar_reporte, cargar_reportes, ver_reportes, eliminar_reporte

def menu():
    while True:
        print("\n📌 MENÚ PRINCIPAL")
        print("1️⃣ Médicos")
        print("2️⃣ Farmacia")
        print("3️⃣ Citas")
        print("4️⃣ Reportes")
        print("0️⃣ Salir")

        opcion = input("⚡ Selecciona una opción: ")

        if opcion == "1":
            menu_medicos()
        elif opcion == "2":
            menu_farmacia()
        elif opcion == "3":
            menu_citas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

# Submenú de Médicos
def menu_medicos():
    while True:
        print("\n🩺 MENÚ MÉDICOS")
        print("1️⃣ Ver lista de médicos")
        print("2️⃣ Agregar un nuevo médico")
        print("3️⃣ Eliminar un médico")
        print("0️⃣ Volver al menú principal")

        opcion = input("⚡ Selecciona una opción: ")

        if opcion == "1":
            ver_medicos()
        elif opcion == "2":
            nombre = input("👨‍⚕️ Nombre del médico: ")
            edad = input("Edad del medico: ")
            genero = input("Genero del medico: ")
            especialidad = input("🔬 Especialidad: ")
            medico = Medico(nombre, edad, genero, especialidad)
            agregar_medico(medico)
        elif opcion == "3":
            ver_medicos()
            nombre = input("❌ Nombre del médico a eliminar: ")
            eliminar_medico(nombre)
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

# Submenú de Farmacia
def menu_farmacia():
    while True:
        print("\n💊 MENÚ FARMACIA")
        print("1️⃣ Ver lista de medicamentos")
        print("2️⃣ Agregar medicamento")
        print("3️⃣ Eliminar medicamento")
        print("4️⃣ Modificar precio")
        print("5️⃣ Modificar stock")
        print("0️⃣ Volver al menú principal")

        opcion = input("⚡ Selecciona una opción: ")

        if opcion == "1":
            ver_inventario()
        elif opcion == "2":
            nombre = input("💊 Nombre del medicamento: ")
            cantidad = input("📦 Cantidad disponible: ")
            precio = input("💲 Precio Unitario: ")
            medicamento = Inventario(nombre, cantidad, precio)
            agregar_medicamento(medicamento)
        elif opcion == "3":
            ver_inventario()
            nombre = input("❌ Nombre del medicamento a eliminar: ")
            eliminar_medicamento(nombre)
        elif opcion == "4":  # 🔥 Modificar precio
            nombre = input("📝 Nombre del medicamento a modificar el precio: ")
            nuevo_precio = int(input("💲 Nuevo precio: "))
            modificar_precio(nombre, nuevo_precio)
        elif opcion == "5":  # 🔥 Modificar stock
            nombre = input("📝 Nombre del medicamento a modificar el stock: ")
            nuevo_stock = int(input("📦 Nueva cantidad: "))
            modificar_stock(nombre, nuevo_stock)
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

# Submenú de Citas
def menu_citas():
    while True:
        print("\n📅 MENÚ CITAS")
        print("1️⃣ Registrar nueva cita")
        print("2️⃣ Ver todas las citas")
        print("3️⃣ Eliminar una cita")
        print("0️⃣ Volver al menú principal")

        opcion = input("⚡ Selecciona una opción: ")

        if opcion == "1":
            nombre = input("📝 Nombre del paciente: ")
            sintomas = input("🤕 Síntomas: ")
            registrar_cita(nombre, sintomas)
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            ver_citas()
            nombre = input("❌ Nombre del paciente a eliminar: ")
            eliminar_cita(nombre)
        elif opcion == "0":
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

# Submenú de Reportes
def menu_reportes():
    while True:
        print("\n📑 MENÚ REPORTES")
        print("1️⃣ Generar reporte de cita")
        print("2️⃣ Ver reportes generados")
        print("3️⃣ Eliminar un reporte")
        print("0️⃣ Volver al menú principal")

        opcion = input("⚡ Selecciona una opción: ")

        if opcion == "1":
            nombre = input("📑 Nombre del paciente para el reporte: ")
            diagnostico = input("🩺 Diagnóstico: ")
            medicamentos = input("💊 Medicamentos (separados por coma): ").split(", ")
            generar_reporte(nombre, diagnostico, medicamentos)

        elif opcion == "2":
            ver_reportes()

        elif opcion == "3":
            ver_reportes()
            nombre = input("❌ Nombre del paciente para eliminar el reporte: ")
            eliminar_reporte(nombre)

        elif opcion == "0":
            break

        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

menu()
