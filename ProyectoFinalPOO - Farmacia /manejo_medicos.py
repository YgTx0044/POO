import json

MEDICOS = "medicos.json"

def cargar_medicos():
    """Carga la lista de médicos desde el JSON."""
    try:
        with open(MEDICOS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # 🔥 Si no existe el archivo, devuelve una lista vacía

def guardar_medicos(medicos):
    """Guarda la lista de médicos en el JSON."""
    with open(MEDICOS, "w", encoding="utf-8") as file:
        json.dump(medicos, file, indent=4)

def agregar_medico(medico):
    """Agrega un médico solo si no está repetido en el JSON."""
    medicos = cargar_medicos()
    
    # 🔥 Verificar si ya existe un médico con el mismo nombre
    for m in medicos:
        if m["nombre"] == medico.nombre:
            print(f"⚠️ El médico '{medico.nombre}' ya está registrado.")
            return
    
    medicos.append(medico.datos_doctor())  # ✅ Si no está repetido, lo agrega
    guardar_medicos(medicos)
    print(f"✅ Médico '{medico.nombre}' registrado exitosamente.")


def ver_medicos():
    """Muestra la lista de médicos registrados."""
    medicos = cargar_medicos()
    if not medicos:
        print("⚠️ No hay médicos registrados.")
        return
    for medico in medicos:
        print(f"👨‍⚕️ {medico['nombre']}, {medico['edad']} años, Especialidad: {medico['especialidad']}")

def eliminar_medico(nombre):
    """Elimina un médico del JSON por su nombre."""
    medicos = cargar_medicos()
    
    # Filtrar los médicos que NO coincidan con el nombre dado
    nuevos_medicos = [medico for medico in medicos if medico["nombre"] != nombre]

    if len(nuevos_medicos) == len(medicos):  # 🔥 Si la lista sigue igual, significa que no encontró al médico
        print(f"⚠️ No se encontró un médico con el nombre '{nombre}'.")
        return
    
    # Guardar la lista actualizada en el JSON
    guardar_medicos(nuevos_medicos)  
    print(f"✅ Médico '{nombre}' eliminado correctamente.")
