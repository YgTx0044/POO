# Importaciones de módulos necesarios
from colorama import Fore, Style, init  # Para darle color al texto en la consola
from medico import Medico  # Clase para manejar datos de médicos
from manejo_medicos import ver_medicos, agregar_medico, eliminar_medico, limpiar_registros, cargar_medicos  # Funciones para médicos
from inventario import Inventario  # Clase para medicamentos
from manejo_inventario import agregar_medicamento, eliminar_medicamento, ver_inventario, modificar_precio, modificar_stock, limpiar_registros, vender_medicamento, cargar_inventario  # Funciones del inventario
from manejo_citas import ver_citas, registrar_cita, cargar_citas, eliminar_cita, limpiar_registros  # Funciones para manejar citas
from manejo_reportes import generar_reporte, cargar_reportes, ver_reportes, limpiar_registros, ver_expediente  # Funciones para los reportes médicos
from paciente import Paciente  # Clase de pacientes

# Menú principal del sistema
def menu():
    while True:
        # Opciones del menú
        print(f"\n{Fore.BLUE}📌 MENÚ PRINCIPAL{Style.RESET_ALL}")
        print("=" * 40)
        print(f"{Fore.YELLOW}1️⃣ Médicos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2️⃣ Farmacia{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3️⃣ Citas{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4️⃣ Reportes{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5️⃣ Limpiar todos los datos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}0️⃣ Salir{Style.RESET_ALL}")

        opcion = input(f"\n{Fore.GREEN}⚡ Selecciona una opción:{Style.RESET_ALL} ")

        # Navegación a submenús
        if opcion == "1":
            menu_medicos()
        elif opcion == "2":
            menu_farmacia()
        elif opcion == "3":
            menu_citas()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            # Limpia todos los registros de los archivos JSON
            archivos = ["medicos.json", "inventario.json", "citas.json", "reportes.json"]
            for archivo in archivos:
                limpiar_registros(archivo)
        elif opcion == "0":
            print(f"{Fore.MAGENTA}👋 ¡Hasta luego!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}⚠️ Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")

# Submenú para gestión de médicos
def menu_medicos():
    while True:
        print(f"\n{Fore.BLUE}🩺 MENÚ MÉDICOS{Style.RESET_ALL}")
        print("=" * 40)
        print(f"{Fore.YELLOW}1️⃣ Ver lista de médicos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2️⃣ Agregar un nuevo médico{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3️⃣ Eliminar un médico{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4️⃣ Eliminar registros de médicos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}0️⃣ Volver al menú principal{Style.RESET_ALL}")

        opcion = input(f"\n{Fore.GREEN}⚡ Selecciona una opción:{Style.RESET_ALL} ")

        if opcion == "1":
            ver_medicos()
        elif opcion == "2":
            # Registro de nuevo médico
            nombre = input("👨‍⚕️ Nombre del médico: ")
            edad = input("⭕ Edad del médico: ")
            genero = input("🚻 Género del médico: ")
            especialidad = input("🔬 Especialidad: ")
            medico = Medico(nombre, edad, genero, especialidad)
            agregar_medico(medico)
        elif opcion == "3":
            # Eliminación de un médico
            ver_medicos()
            nombre = input("❌ Nombre del médico a eliminar: ")
            eliminar_medico(nombre)
        elif opcion == "4":
            # Limpia todos los médicos registrados
            limpiar_registros("medicos.json")
        elif opcion == "0":
            break
        else:
            print(f"{Fore.RED}⚠️ Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")

# Submenú para farmacia/inventario
def menu_farmacia():
    while True:
        print(f"\n{Fore.BLUE}💊 MENÚ FARMACIA{Style.RESET_ALL}")
        print("=" * 40)
        print(f"{Fore.YELLOW}1️⃣ Ver lista de medicamentos{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2️⃣ Agregar medicamento{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3️⃣ Eliminar medicamento{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4️⃣ Modificar precio{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5️⃣ Modificar stock{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6️⃣ Vender medicamento{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}7️⃣ Eliminar registros de inventario{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}0️⃣ Volver al menú principal{Style.RESET_ALL}")

        opcion = input(f"\n{Fore.GREEN}Selecciona una opción:{Style.RESET_ALL} ")

        if opcion == "1":
            ver_inventario()
        elif opcion == "2":
            # Agrega nuevo medicamento al inventario
            nombre = input("💊 Nombre del medicamento: ")
            cantidad = int(input("📦 Cantidad disponible: "))
            precio = float(input("💲 Precio Unitario: "))
            medicamento = Inventario(nombre, cantidad, precio)
            agregar_medicamento(medicamento)
        elif opcion == "3":
            ver_inventario()
            nombre = input("❌ Nombre del medicamento a eliminar: ")
            eliminar_medicamento(nombre)
        elif opcion == "4":
            nombre = input("📝 Nombre del medicamento a modificar el precio: ")
            nuevo_precio = float(input("💲 Nuevo precio: "))
            modificar_precio(nombre, nuevo_precio)
        elif opcion == "5":
            nombre = input("📝 Nombre del medicamento a modificar el stock: ")
            nuevo_stock = int(input("📦 Nueva cantidad: "))
            modificar_stock(nombre, nuevo_stock)
        elif opcion == "6":
            # Procesa la venta de múltiples medicamentos
            inventario = cargar_inventario()
            lista_medicamentos = [item["nombre"] for item in inventario]
            ver_inventario()
            medicamentos_a_vender = []
            print("\n🛒 Agrega los medicamentos que deseas comprar (escribe 'fin' para terminar):")
            while True:
                nombre_med = input("💊 Nombre del medicamento: ")
                if nombre_med.lower() == "fin":
                    break
                if nombre_med not in lista_medicamentos:
                    print(f"{Fore.RED}⚠️ '{nombre_med}' no está en el inventario. Intenta nuevamente.{Style.RESET_ALL}")
                    continue
                cantidad_med = int(input("📦 Cantidad a vender: "))
                medicamentos_a_vender.append({"nombre": nombre_med, "cantidad": cantidad_med})
            for medicamento in medicamentos_a_vender:
                vender_medicamento(medicamento["nombre"], medicamento["cantidad"])
        elif opcion == "7":
            limpiar_registros("inventario.json")
        elif opcion == "0":
            break
        else:
            print(f"{Fore.RED}⚠️ Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")

# Submenú para gestionar citas médicas
def menu_citas():
    while True:
        print(f"\n{Fore.BLUE}📅 MENÚ CITAS{Style.RESET_ALL}")
        print("=" * 40)
        print(f"{Fore.YELLOW}1️⃣ Registrar nueva cita{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2️⃣ Ver todas las citas{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3️⃣ Eliminar una cita{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4️⃣ Eliminar registros de citas{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}0️⃣ Volver al menú principal{Style.RESET_ALL}")

        opcion = input(f"\n{Fore.GREEN}Selecciona una opción:{Style.RESET_ALL} ")

        if opcion == "1":
            # Registro de cita nueva con datos del paciente
            nombre = input("📝 Nombre del paciente: ")
            edad = input("⭕ Edad del paciente: ")
            genero = input("🚻 Género del paciente: ")
            peso = input("⚖️ Peso del paciente: ")
            estatura = input("📏 Estatura del paciente: ")
            curp = input("🆔 CURP del paciente: ")
            sintomas = input("🤕 Síntomas: ")
            paciente = Paciente(nombre, edad, genero, peso, estatura, curp, sintomas)
            registrar_cita(paciente)
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            ver_citas()
            curp = input("❌ CURP del paciente a eliminar: ")
            eliminar_cita(curp)
        elif opcion == "4":
            limpiar_registros("citas.json")
        elif opcion == "0":
            break
        else:
            print(f"{Fore.RED}⚠️ Opción no válida. Inténtalo de nuevo.{Style.RESET_ALL}")

# Submenú para reportes y expedientes médicos
def menu_reportes():
    while True:
        print("\n📑 MENU DE REPORTES")
        print("=" * 40)
        print("1️⃣ Generar Reporte")
        print("2️⃣ Ver Reportes")
        print("3️⃣ Ver Expediente de un Paciente")
        print("4️⃣ Limpiar Registros")
        print("0️⃣ Volver al Menú Principal")
        opcion = input("🔹 Selecciona una opción: ")

        if opcion == "1":
            citas = cargar_citas()
            if not citas:
                print(f"{Fore.RED}⚠️ No hay citas registradas, no se puede generar un reporte.{Style.RESET_ALL}")
                continue
            ver_citas()
            curp = input("🆔 Ingresa la CURP del paciente para el reporte: ")
            paciente = next((cita for cita in citas if cita["curp"] == curp), None)
            if not paciente:
                print(f"{Fore.RED}⚠️ No se encontró ninguna cita con la CURP {curp}.{Style.RESET_ALL}")
                continue
            diagnostico = input("🩺 Diagnóstico: ")
            medicos = cargar_medicos()
            lista_medicos = [medico["nombre"] for medico in medicos]
            ver_medicos()
            while True:
                medico = input("👨‍⚕️ Nombre del médico que genera el reporte: ")
                if medico in lista_medicos:
                    break
                print(f"{Fore.RED}⚠️ El nombre ingresado no coincide con un médico registrado. Intenta nuevamente.{Style.RESET_ALL}")
            medicamentos = []
            print("\n💊 Agrega los medicamentos recetados (escribe 'fin' para terminar):")
            while True:
                nombre_med = input("   💊 Nombre del medicamento: ")
                if nombre_med.lower() == "fin":
                    break
                cantidad_med = int(input("   📦 Cantidad recetada: "))
                medicamentos.append({"nombre": nombre_med, "cantidad": cantidad_med})
            generar_reporte(curp, diagnostico, medicamentos, medico)
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            curp_expediente = input("📑 Ingresa la CURP del paciente para ver su expediente: ")
            reportes = cargar_reportes()
            existe_expediente = any(r["curp"] == curp_expediente for r in reportes)
            if existe_expediente:
                ver_expediente(curp_expediente)
            else:
                print(f"{Fore.RED}⚠️ No se encontraron reportes para la CURP {curp_expediente}.{Style.RESET_ALL}")
        elif opcion == "4":
            limpiar_registros()
        elif opcion == "0":
            break
        else:
            print(f"{Fore.RED}⚠️ Opción inválida, intenta nuevamente.{Style.RESET_ALL}")

# Llama al menú principal al iniciar
menu()
