import json

CITAS = "citas.json"
REPORTES = "reportes.json"

def cargar_citas():
    try:
        with open(CITAS, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_citas(citas):
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump(citas, file, indent=4)

def cargar_reportes():
    try:
        with open(REPORTES, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_reportes(reportes):
    with open(REPORTES, "w", encoding="utf-8") as file:
        json.dump(reportes, file, indent=4)

def ver_citas():
    citas = cargar_citas()
    if not citas:
        print("⚠️ No hay citas registradas.")
        return
    
    for cita in citas:
        print(f"📌 Paciente: {cita['nombre']} - Síntomas: {cita['sintomas']}")

def generar_reporte(nombre_paciente, diagnostico, medicamentos):
    citas = cargar_citas()
    reportes = cargar_reportes()

    # Evita reportes duplicados
    for reporte in reportes:
        if reporte["nombre"] == nombre_paciente:
            print(f"⚠️ Ya existe un reporte para '{nombre_paciente}', no se duplicará.")
            return

    # Filtrar citas eliminando la del paciente
    citas_filtradas = [cita for cita in citas if cita["nombre"] != nombre_paciente]

    if len(citas) == len(citas_filtradas):
        print(f"⚠️ No se encontró la cita de '{nombre_paciente}', no se generó reporte.")
        return

    # Crear y guardar el reporte
    nuevo_reporte = {
        "nombre": nombre_paciente,
        "sintomas": next(c["sintomas"] for c in citas if c["nombre"] == nombre_paciente),
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }
    reportes.append(nuevo_reporte)
    guardar_reportes(reportes)

    # Guardar el JSON actualizado sin la cita
    guardar_citas(citas_filtradas)

    print(f"✅ Reporte generado y cita de '{nombre_paciente}' eliminada correctamente.")

def eliminar_reporte(nombre_paciente):
    reportes = cargar_reportes()
    
    # Filtrar los reportes que NO coincidan con el nombre dado
    nuevos_reportes = [reporte for reporte in reportes if reporte["nombre"] != nombre_paciente]

    if len(nuevos_reportes) == len(reportes):  # 🔥 Si la lista sigue igual, significa que no encontró el reporte
        print(f"⚠️ No se encontró un reporte para '{nombre_paciente}'.")
        return
    
    # Guardar la lista actualizada en el JSON
    guardar_reportes(nuevos_reportes)  
    print(f"✅ Reporte de '{nombre_paciente}' eliminado correctamente.")

def ver_reportes():
    reportes = cargar_reportes()
    if not reportes:
        print("⚠️ No hay reportes generados.")
    else:
        print("\n📑 Lista de Reportes:")
        for reporte in reportes:
            print(f"📌 Paciente: {reporte['nombre']} - Diagnóstico: {reporte['diagnostico']} - Medicamentos: {', '.join(reporte['medicamentos'])}")
