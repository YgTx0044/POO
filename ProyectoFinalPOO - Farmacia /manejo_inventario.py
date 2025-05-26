import json
from colorama import Fore, Style, init

# Inicializar colorama (necesario para Windows)
init(autoreset=True)

# Ruta del archivo donde se guarda el inventario
INVENTARIO = "inventario.json"

def cargar_inventario():
    """Carga los medicamentos desde el archivo JSON"""
    try:
        with open(INVENTARIO, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Si el archivo no existe, devuelve lista vacía

def guardar_inventario(inventario):
    """Guarda el inventario actualizado en el archivo JSON"""
    with open(INVENTARIO, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4)

def ver_inventario():
    """Muestra el inventario con colores y mejor formato"""
    inventario = cargar_inventario()
    
    if not inventario:
        print(f"{Fore.RED}\n⚠️ No hay medicamentos registrados.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}\n📋 LISTA DE MEDICAMENTOS DISPONIBLES")
    print("=" * 40 + Style.RESET_ALL)
    
    for item in inventario:
        print(f"💊 {Fore.BLUE}Medicamento: {item['nombre']}{Style.RESET_ALL}")
        print(f"   💰 Precio: {Fore.GREEN}${item['precio']}{Style.RESET_ALL}")
        print(f"   📦 Stock: {Fore.YELLOW}{item['stock']} unidades{Style.RESET_ALL}")
        print("-" * 40)

def vender_medicamento(nombre, cantidad):
    """Descuenta el stock al vender un medicamento y muestra el total a pagar"""
    inventario = cargar_inventario()
    
    for item in inventario:
        if item["nombre"] == nombre:
            if cantidad <= 0:
                print(f"{Fore.YELLOW}⚠️ La cantidad debe ser mayor a 0.{Style.RESET_ALL}")
                return
            if cantidad > item["stock"]:
                print(f"{Fore.YELLOW}⚠️ No hay suficiente stock de '{nombre}'. Disponibles: {item['stock']}.{Style.RESET_ALL}")
                return
            
            item["stock"] -= cantidad
            guardar_inventario(inventario)

            # Calcular y mostrar costo total
            precio_unitario = item["precio"]
            costo_total = cantidad * precio_unitario  

            print(f"{Fore.GREEN}✅ Venta exitosa: {cantidad} unidades de '{nombre}'. Precio unitario: ${precio_unitario:.2f}. Total a pagar: ${costo_total:.2f}. Stock restante: {item['stock']}.{Style.RESET_ALL}")
            return
    
    print(f"{Fore.RED}⚠️ Medicamento '{nombre}' no encontrado en el inventario.{Style.RESET_ALL}")

def agregar_medicamento(medicamento):
    """Agrega un medicamento si no está registrado aún"""
    inventario = cargar_inventario()

    if any(item["nombre"] == medicamento.nombre for item in inventario):
        print(f"{Fore.YELLOW}\n⚠️ El medicamento '{medicamento.nombre}' ya está registrado.{Style.RESET_ALL}")
        return

    inventario.append(medicamento.datos_inventario())
    guardar_inventario(inventario)
    print(f"{Fore.GREEN}\n✅ Medicamento '{medicamento.nombre}' agregado exitosamente.{Style.RESET_ALL}")

def eliminar_medicamento(nombre):
    """Elimina un medicamento si existe"""
    inventario = cargar_inventario()
    nuevo_inventario = [item for item in inventario if item["nombre"] != nombre]

    if len(nuevo_inventario) == len(inventario):
        print(f"{Fore.RED}\n⚠️ Medicamento '{nombre}' no encontrado en el inventario.{Style.RESET_ALL}")
        return

    guardar_inventario(nuevo_inventario)
    print(f"{Fore.GREEN}\n✅ Medicamento '{nombre}' eliminado correctamente.{Style.RESET_ALL}")

def modificar_precio(nombre, nuevo_precio):
    """Actualiza el precio de un medicamento"""
    if nuevo_precio <= 0:
        print(f"{Fore.YELLOW}⚠️ No se puede asignar un precio menor o igual a 0.{Style.RESET_ALL}")
        return

    inventario = cargar_inventario()

    for item in inventario:
        if item["nombre"] == nombre:
            item["precio"] = nuevo_precio
            guardar_inventario(inventario)
            print(f"{Fore.GREEN}✅ Precio actualizado: '{nombre}' ahora cuesta ${nuevo_precio}.{Style.RESET_ALL}")
            return
    
    print(f"{Fore.RED}⚠️ Medicamento '{nombre}' no encontrado en el inventario.{Style.RESET_ALL}")

def modificar_stock(nombre, nuevo_stock):
    """Actualiza el stock de un medicamento"""
    if nuevo_stock < 0:
        print(f"{Fore.YELLOW}⚠️ No se puede asignar un stock negativo.{Style.RESET_ALL}")
        return

    inventario = cargar_inventario()

    for item in inventario:
        if item["nombre"] == nombre:
            item["stock"] = nuevo_stock
            guardar_inventario(inventario)
            print(f"{Fore.GREEN}✅ Stock actualizado: '{nombre}' ahora tiene {nuevo_stock} unidades disponibles.{Style.RESET_ALL}")
            return
    
    print(f"{Fore.RED}⚠️ Medicamento '{nombre}' no encontrado en el inventario.{Style.RESET_ALL}")

def limpiar_registros(CITAS):
    """Elimina todos los registros del archivo especificado"""
    with open(CITAS, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)
    print(f"{Fore.RED}❌ Registros en '{CITAS}' eliminados correctamente.{Style.RESET_ALL}")

def actualizar_inventario(medicamentos):
    """
    Actualiza el inventario restando las cantidades entregadas
    Se añade la clave 'cantidad_entregada' para cada medicamento
    """
    inventario = cargar_inventario()

    # Asegura que el stock sea entero
    for item in inventario:
        item["stock"] = int(item["stock"])

    for medicamento in medicamentos:
        nombre = medicamento["nombre"]
        cantidad_solicitada = medicamento["cantidad"]

        item_inventario = next((item for item in inventario if item["nombre"] == nombre), None)

        if item_inventario:
            stock_disponible = item_inventario["stock"]
            cantidad_entregada = min(stock_disponible, cantidad_solicitada)

            item_inventario["stock"] -= cantidad_entregada
            medicamento["cantidad_entregada"] = cantidad_entregada

            if cantidad_entregada < cantidad_solicitada:
                print(f"⚠️ {nombre}: Solo {cantidad_entregada} disponibles, faltaron {cantidad_solicitada - cantidad_entregada}.")
                item_inventario["stock"] = 0
            else:
                print(f"✅ {nombre}: {cantidad_entregada} unidades descontadas del inventario.")

    try:
        with open("inventario.json", "w", encoding="utf-8") as file:
            json.dump(inventario, file, ensure_ascii=False, indent=4)
        print(f"{Fore.GREEN}✅ Inventario actualizado correctamente.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error al actualizar el inventario: {e}.{Style.RESET_ALL}")
