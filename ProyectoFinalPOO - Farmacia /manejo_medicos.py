import json
from colorama import Fore, Style, init

# Inicializar colorama (necesario en Windows para los colores en terminal)
init(autoreset=True)

# Archivo donde se guardan los datos de los médicos
MEDICOS = "medicos.json"

def cargar_medicos():
    """Carga la lista de médicos desde el archivo JSON"""
    try:
        with open(MEDICOS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 🔥 Si no existe el archivo, se devuelve una lista vacía

def guardar_medicos(medicos):
    """Guarda la lista de médicos en el archivo JSON"""
    with open(MEDICOS, "w", encoding="utf-8") as file:
        json.dump(medicos, file, indent=4)

def agregar_medico(medico):
    """Agrega un nuevo médico si no está registrado ya"""
    medicos = cargar_medicos()
    
    # Verificar si el médico ya está en la lista
    for m in medicos:
        if m["nombre"] == medico.nombre:
            print(f"{Fore.YELLOW}⚠️ El médico '{medico.nombre}' ya está registrado.{Style.RESET_ALL}")
            return
    
    # Agregar y guardar
    medicos.append(medico.datos_doctor())  
    guardar_medicos(medicos)
    print(f"{Fore.GREEN}✅ Médico '{medico.nombre}' registrado exitosamente.{Style.RESET_ALL}")

def ver_medicos():
    """Muestra los médicos disponibles con formato y color"""
    medicos = cargar_medicos()
    
    if not medicos:
        print(f"{Fore.RED}⚠️ No hay médicos registrados.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}\n📋 LISTA DE MÉDICOS DISPONIBLES")
    print("=" * 40 + Style.RESET_ALL)
    
    for medico in medicos:
        print(f"⚕️ {Fore.BLUE}Nombre: {medico['nombre']}{Style.RESET_ALL}")
        print(f"   🎂 Edad: {Fore.GREEN}{medico['edad']} años{Style.RESET_ALL}")
        print(f"   🚻 Género: {medico['genero']}")
        print(f"   🩺 Especialidad: {Fore.BLUE}{medico['especialidad']}{Style.RESET_ALL}")
        print("-" * 40)

def eliminar_medico(nombre):
    """Elimina un médico si existe por su nombre"""
    medicos = cargar_medicos()
    nuevos_medicos = [medico for medico in medicos if medico["nombre"] != nombre]

    # Si no se eliminó ninguno, el médico no estaba
    if len(nuevos_medicos) == len(medicos):  
        print(f"{Fore.RED}⚠️ No se encontró un médico con el nombre '{nombre}'.{Style.RESET_ALL}")
        return
    
    # Guardar la nueva lista sin el médico eliminado
    guardar_medicos(nuevos_medicos)  
    print(f"{Fore.GREEN}✅ Médico '{nombre}' eliminado correctamente.{Style.RESET_ALL}")

def limpiar_registros(CITAS):
    """Limpia todos los registros en el archivo indicado (como citas)"""
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)
    print(f"{Fore.RED}❌ Registros en '{CITAS}' eliminados correctamente.{Style.RESET_ALL}")
