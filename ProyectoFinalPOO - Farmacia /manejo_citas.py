import json
from colorama import Fore, Style, init
from paciente import Paciente

# Inicializar colorama para permitir colores en la consola
init(autoreset=True)

# Archivo donde se almacenan las citas
CITAS = "citas.json"

def cargar_citas():
    """Carga la lista de citas desde el archivo JSON."""
    try:
        with open(CITAS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Si el archivo no existe, se devuelve una lista vacía

def guardar_citas(citas):
    """Guarda la lista de citas en el archivo JSON."""
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump(citas, file, indent=4)

def registrar_cita(paciente):
    """
    Registra una nueva cita solo si el paciente no tiene una cita previa.
    Verifica duplicidad por CURP.
    """
    citas = cargar_citas()
    
    # Verificar si ya existe una cita con esa CURP
    for c in citas:
        if c["curp"] == paciente.curp:
            print(f"{Fore.YELLOW}⚠️ El paciente '{paciente.nombre}' con CURP {paciente.curp} ya tiene una cita registrada.{Style.RESET_ALL}")
            return
    
    # Agrega nueva cita y guarda
    citas.append(paciente.datos_paciente())  
    guardar_citas(citas)

    print(f"{Fore.GREEN}✅ Cita registrada para {paciente.nombre} ({paciente.edad} años, {paciente.genero}) con CURP: {paciente.curp}.{Style.RESET_ALL}")

def eliminar_cita(curp):
    """
    Elimina la cita de un paciente según su CURP.
    Si no se encuentra, se notifica al usuario.
    """
    citas = cargar_citas()
    
    if not citas:
        print(f"{Fore.RED}⚠️ No hay citas registradas.{Style.RESET_ALL}")
        return

    # Filtra todas las citas excepto la que coincide con el CURP
    nuevas_citas = [cita for cita in citas if cita["curp"] != curp]

    if len(nuevas_citas) == len(citas):
        print(f"{Fore.RED}⚠️ No se encontró una cita con la CURP {curp}.{Style.RESET_ALL}")
    else:
        guardar_citas(nuevas_citas)
        print(f"{Fore.GREEN}✅ Cita eliminada para el paciente con CURP {curp}.{Style.RESET_ALL}")

def ver_citas():
    """Muestra todas las citas registradas con formato amigable."""
    citas = cargar_citas()
    
    if not citas:
        print(f"{Fore.RED}⚠️ No hay citas registradas.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}\n📅 LISTA DE CITAS")
    print("=" * 40 + Style.RESET_ALL)

    for cita in citas:
        # Mostrar cada cita con formato visual
        print(f"📌 {Fore.BLUE}Paciente: {cita['nombre']}{Style.RESET_ALL}")
        print(f"   🆔 CURP: {Fore.BLUE}{cita['curp']}{Style.RESET_ALL}")
        print(f"   🤕 Síntomas: {Fore.YELLOW}{cita['sintomas']}{Style.RESET_ALL}")
        print("-" * 40)

def limpiar_registros(archivo):
    """Limpia todos los registros del archivo especificado (deja el archivo vacío)."""
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)
    print(f"{Fore.RED}❌ Registros en '{archivo}' eliminados correctamente.{Style.RESET_ALL}")
