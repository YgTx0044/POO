import json

INVENTARIO = "inventario.json"

def cargar_inventario():
    """Carga la lista de medicamentos desde el JSON."""
    try:
        with open(INVENTARIO, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Si el archivo no existe, se inicia con una lista vacía

def guardar_inventario(inventario):
    """Guarda la lista de medicamentos en el JSON."""
    with open(INVENTARIO, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4)

def eliminar_medicamento(nombre):
    """Elimina un medicamento del inventario sin detener el flujo si no existe."""
    inventario = cargar_inventario()

    # Filtrar los medicamentos que NO coincidan con el nombre dado
    nuevo_inventario = [item for item in inventario if item["nombre"] != nombre]

    if len(nuevo_inventario) == len(inventario):
        return  # No hace nada si el medicamento no existe, pero no detiene el flujo

    guardar_inventario(nuevo_inventario)
    print(f"✅ Medicamento '{nombre}' eliminado correctamente.")

def agregar_medicamento(medicamento):
    """Agrega un nuevo medicamento al inventario evitando duplicados."""
    inventario = cargar_inventario()

    # 🔥 Verificar si ya existe el medicamento
    if any(item["nombre"] == medicamento.nombre for item in inventario):
        print(f"⚠️ El medicamento '{medicamento.nombre}' ya está registrado.")
        return

    inventario.append(medicamento.datos_inventario())
    guardar_inventario(inventario)
    print(f"✅ Medicamento '{medicamento.nombre}' agregado exitosamente.")

def ver_inventario():
    """Muestra la lista de medicamentos disponibles."""
    inventario = cargar_inventario()
    if not inventario:
        print("⚠️ No hay medicamentos registrados.")
        return
    for item in inventario:
        print(f"💊 {item['nombre']} - Precio: ${item['precio']}, Stock: {item['stock']}")

def vender_medicamento(nombre, cantidad):
    """Vende un medicamento si hay suficiente stock y la cantidad es válida."""
    inventario = cargar_inventario()

    for item in inventario:
        if item["nombre"] == nombre:
            if cantidad <= 0:
                print("⚠️ La cantidad debe ser mayor a 0.")
                return
            if cantidad > item["stock"]:
                print(f"⚠️ No hay suficiente stock de '{nombre}'. Disponibles: {item['stock']}.")
                return
            
            item["stock"] -= cantidad  # Reducir el stock
            guardar_inventario(inventario)
            print(f"✅ Venta exitosa: {cantidad} unidades de '{nombre}'. Stock restante: {item['stock']}.")
            return
    
    print(f"⚠️ Medicamento '{nombre}' no encontrado en el inventario.")

def modificar_precio(nombre, nuevo_precio):
    """Modifica el precio de un medicamento en el JSON sin detener la ejecución si es inválido."""
    if nuevo_precio <= 0:
        print("⚠️ No se puede asignar un precio menor o igual a 0.")
        return  

    inventario = cargar_inventario()

    for item in inventario:
        if item["nombre"] == nombre:
            item["precio"] = nuevo_precio
            guardar_inventario(inventario)  
            print(f"✅ Precio de '{nombre}' actualizado a ${nuevo_precio}.")
            return

    print(f"⚠️ No se encontró el medicamento '{nombre}' en el inventario.")

def modificar_stock(nombre, nuevo_stock):
    """Modifica el stock de un medicamento en el JSON sin eliminarlo si llega a 0."""
    if nuevo_stock < 0:
        print("⚠️ No se puede asignar un stock negativo.")
        return  # No detiene la ejecución

    inventario = cargar_inventario()

    for item in inventario:
        if item["nombre"] == nombre:
            item["stock"] = nuevo_stock  # Actualiza el stock
            guardar_inventario(inventario)  # Guarda los cambios en el JSON
            print(f"✅ Stock de '{nombre}' actualizado a {nuevo_stock} unidades.")
            return

    print(f"⚠️ No se encontró el medicamento '{nombre}' en el inventario.")  #  No detiene

