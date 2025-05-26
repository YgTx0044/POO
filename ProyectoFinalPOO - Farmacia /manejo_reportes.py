import json
from colorama import Fore, Style, init
from manejo_citas import eliminar_cita
from manejo_inventario import cargar_inventario
from manejo_inventario import actualizar_inventario

# Inicializa colorama para dar color a los textos en consola
init(autoreset=True)

# Archivos a usar
CITAS = "citas.json"
REPORTES = "reportes.json"

# Carga las citas desde el archivo JSON
def cargar_citas():
    try:
        with open(CITAS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Devuelve lista vacía si no existe

# Guarda las citas actualizadas en el archivo
def guardar_citas(citas):
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump(citas, file, indent=4)

# Carga los reportes generados
def cargar_reportes():
    try:
        with open(REPORTES, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Guarda los reportes generados
def guardar_reportes(reportes):
    with open(REPORTES, "w", encoding="utf-8") as file:
        json.dump(reportes, file, indent=4)

# Muestra las citas en consola con formato
def ver_citas():
    citas = cargar_citas()
    
    if not citas:
        print(f"{Fore.RED}⚠️ No hay citas registradas.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}\n📅 LISTA DE CITAS")
    print("=" * 40 + Style.RESET_ALL)
    
    for cita in citas:
        print(f"📌 {Fore.BLUE}Paciente: {cita['nombre']}{Style.RESET_ALL}")
        print(f"   🤕 Síntomas: {Fore.YELLOW}{cita['sintomas']}{Style.RESET_ALL}")
        print("-" * 40)

# Limpia el archivo de reportes (vacía la lista)
def limpiar_registros():
    try:
        with open("reportes.json", "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print(f"{Fore.GREEN}✅ Todos los reportes han sido eliminados correctamente.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error al limpiar los registros: {e}.{Style.RESET_ALL}")

# Genera un nuevo reporte a partir de una cita y medicamentos recetados
def generar_reporte(curp, diagnostico, medicamentos, medico):
    citas = cargar_citas()
    inventario = cargar_inventario()  # Para obtener precios

    if not citas:
        print(f"{Fore.RED}⚠️ No hay citas registradas.{Style.RESET_ALL}")
        return

    # Busca la cita del paciente por CURP
    paciente_reporte = next((cita for cita in citas if cita["curp"] == curp), None)

    if not paciente_reporte:
        print(f"{Fore.RED}⚠️ No se encontró una cita con la CURP {curp}.{Style.RESET_ALL}")
        return

    if not isinstance(medicamentos, list):
        medicamentos = []

    # Actualiza inventario y asigna cantidad entregada
    actualizar_inventario(medicamentos)

    total_costo = 0  # Total a pagar por medicamentos

    # Calcula el costo por medicamento y el total
    for medicamento in medicamentos:
        nombre = medicamento["nombre"]
        cantidad_entregada = medicamento.get("cantidad_entregada", 0)

        item_inventario = next((item for item in inventario if item["nombre"] == nombre), None)

        if item_inventario:
            precio_unitario = float(item_inventario["precio"])
            costo_total = cantidad_entregada * precio_unitario

            medicamento["precio_unitario"] = precio_unitario
            medicamento["costo_total"] = costo_total
            total_costo += costo_total

    # Crea el reporte con toda la info del paciente y medicamentos
    reporte = {
        "curp": curp,
        "nombre": paciente_reporte["nombre"],
        "edad": paciente_reporte["edad"],
        "genero": paciente_reporte["genero"],
        "estatura": paciente_reporte["estatura"],
        "peso": paciente_reporte["peso"],
        "sintomas": paciente_reporte["sintomas"],
        "diagnostico": diagnostico,
        "medico": medico,
        "medicamentos": medicamentos,
        "total_costo": total_costo
    }

    reportes = cargar_reportes()
    reportes.append(reporte)

    try:
        guardar_reportes(reportes)  # Guarda el nuevo reporte
        eliminar_cita(curp)  # Borra la cita del paciente
        print(f"{Fore.GREEN}✅ Reporte generado por el médico {medico} para {paciente_reporte['nombre']} con CURP {curp}.{Style.RESET_ALL}")
        print(f"💊 Detalle de costos por medicamento:")
        for medicamento in medicamentos:
            print(f"   - {medicamento['nombre']}: {medicamento['cantidad_entregada']} unidades x ${medicamento['precio_unitario']:.2f} = ${medicamento['costo_total']:.2f}")

        print(f"💰 {Fore.YELLOW}Costo total de medicamentos vendidos: ${total_costo:.2f}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}❌ Error al generar el reporte: {e}.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚠️ La cita de {paciente_reporte['nombre']} sigue activa.{Style.RESET_ALL}")

# Muestra todos los reportes generados con información detallada
def ver_reportes():
    reportes = cargar_reportes()

    if not reportes:
        print(f"{Fore.RED}⚠️ No hay reportes generados.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}📑 LISTA DE REPORTES{Style.RESET_ALL}")
    print("=" * 40)

    for reporte in reportes:
        print(f"\n📑 Reporte de {Fore.BLUE}{reporte['nombre']}{Style.RESET_ALL} (CURP: {reporte['curp']})")
        print(f"🩺 Diagnóstico: {Fore.BLUE}{reporte['diagnostico']}{Style.RESET_ALL}")
        print(f"👨‍⚕️ Médico: {Fore.CYAN}{reporte.get('medico', 'No registrado')}{Style.RESET_ALL}")
        print("💊 Medicamentos Recetados:")

        medicamentos = reporte.get("medicamentos", [])
        if not medicamentos:
            print(f"   ⚠️ {Fore.RED}No hay medicamentos registrados en este reporte.{Style.RESET_ALL}")
        else:
            for medicamento in medicamentos:
                if isinstance(medicamento, dict):
                    nombre = medicamento.get("nombre", "Desconocido")
                    cantidad = medicamento.get("cantidad", "No especificada")
                    print(f"   ✅ {nombre} - {cantidad} unidades recetadas")
                else:
                    print(f"   ⚠️ {Fore.RED}Error: formato de medicamento inválido.{Style.RESET_ALL}")

        print("=" * 40)

    print(f"{Fore.GREEN}✅ Reportes mostrados correctamente.{Style.RESET_ALL}")

# Muestra todos los reportes de un paciente por su CURP
def ver_expediente(curp):
    reportes = cargar_reportes()
    expediente = [r for r in reportes if r["curp"] == curp]

    if not expediente:
        print(f"{Fore.RED}⚠️ No se encontraron reportes para la CURP {curp}.{Style.RESET_ALL}")
        return

    print(f"\n📂 {Fore.CYAN}EXPEDIENTE DEL PACIENTE{Style.RESET_ALL}")
    print("=" * 40)

    for i, reporte in enumerate(expediente, 1):
        print(f"\n📝 {Fore.BLUE}Reporte #{i}{Style.RESET_ALL}")
        print(f"   🆔 CURP: {Fore.BLUE}{reporte['curp']}{Style.RESET_ALL}")
        print(f"   👤 Nombre: {Fore.BLUE}{reporte['nombre']}{Style.RESET_ALL}")
        print(f"   🤕 Síntomas: {Fore.BLUE}{reporte['sintomas']}{Style.RESET_ALL}")
        print(f"   🩺 Diagnóstico: {Fore.BLUE}{reporte.get('diagnostico', 'No registrado')}{Style.RESET_ALL}")
        print(f"   👨‍⚕️ Médico: {Fore.CYAN}{reporte.get('medico', 'No registrado')}{Style.RESET_ALL}")
        print("   💊 Medicamentos Recetados:")

        for medicamento in reporte["medicamentos"]:
            nombre = medicamento["nombre"]
            cantidad_solicitada = medicamento["cantidad"]
            print(f"      ✅ {nombre} - Recetado: {cantidad_solicitada}")

        print("-" * 40)

    print(f"{Fore.GREEN}✅ Expediente mostrado correctamente.{Style.RESET_ALL}")
