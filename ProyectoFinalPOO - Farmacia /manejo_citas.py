import json

CITAS = "citas.json"

def cargar_citas():
    try:
        with open(CITAS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Si el archivo no existe, se inicia con una lista vacía

def guardar_citas(citas):
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump(citas, file, indent=4)

def registrar_cita(nombre_paciente, sintomas):
    citas = cargar_citas()  # Cargar las citas actuales

    nueva_cita = {"nombre": nombre_paciente, "sintomas": sintomas}
    citas.append(nueva_cita)  # Agregar la nueva cita a la lista

    guardar_citas(citas)
    print(f"✅ Cita para '{nombre_paciente}' registrada correctamente.")


def eliminar_cita(nombre_paciente):
    citas = cargar_citas()
    citas_filtradas = [cita for cita in citas if cita["nombre"] != nombre_paciente]

    if len(citas) == len(citas_filtradas):
        print(f"⚠️ No se encontró la cita de '{nombre_paciente}', nada fue eliminado.")
    else:
        guardar_citas(citas_filtradas)
        print(f"✅ Cita de '{nombre_paciente}' eliminada correctamente.")


def ver_citas():
    citas = cargar_citas()
    if not citas:
        print("⚠️ No hay citas registradas.")
        return
    
    for cita in citas:
        print(f"📌 Paciente: {cita['nombre']} - Síntomas: {cita['sintomas']}")
