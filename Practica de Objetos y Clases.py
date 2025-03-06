# Yahir Gutierrez Turrubiartes - 24690555

'''
    Escenario 1:
    
En la tienda de mascotas "Patitas Felices", se necesita un sistema para gestionar productos, clientes, ventas, proveedores y promociones, actualmente, la tienda ofrece una amplia variedad de productos, como alimentos, juguetes y accesorios para mascotas.

Cada producto tiene un nombre, una categoría (alimento, juguete o accesorio), un precio, una cantidad disponible en inventario y un proveedor que lo suministra; por su parte los clientes de la tienda tienen un nombre, un número de identificación y un historial de compras que registra todas las ventas realizadas.

Además, la tienda ofrece promociones especiales en ciertos productos, como descuentos o "2x1", donde cada promoción tiene un nombre, una descripción, un porcentaje de descuento y una lista de productos a los que aplica.

El sistema debe permitir:

1- Registrar nuevos productos, clientes, proveedores y promociones.
2- Mostrar la lista de productos disponibles, incluyendo su nombre, categoría, precio, cantidad en inventario y proveedor.
3- Realizar una venta, donde un cliente puede comprar uno o más productos. Al realizar una venta, el sistema debe:
4- Aplicar automáticamente las promociones vigentes a los productos elegidos.
5- Actualizar el inventario de los productos vendidos.
6- Registrar la compra en el historial del cliente.
7- Mostrar el historial de compras de un cliente, incluyendo los productos comprados, la fecha de la compra, el monto total y los descuentos aplicados.
8- Gestionar proveedores, incluyendo la lista de productos que suministran y su información de contacto.
9- Gestionar promociones, incluyendo su creación, modificación y aplicación automática durante las ventas.

Además, el sistema debe manejar situaciones excepcionales, como intentar vender un producto que no tiene suficiente inventario o aplicar una promoción a un producto que no está incluido en la oferta, y proporcionar mensajes claros en esos casos.
'''

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre


class Cliente(Persona):
    def __init__(self, nombre, identificacion):
        super().__init__(nombre)
        self._identificacion = identificacion
        self._historial_compras = []

    def get_identificacion(self):
        return self._identificacion

    def set_identificacion(self, identificacion):
        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")
        self._identificacion = identificacion

    def get_historial_compras(self):
        return self._historial_compras

    def agregar_compra(self, compra):
        if not compra:
            raise ValueError("La compra no puede estar vacía.")
        self._historial_compras.append(compra)


class Proveedor(Persona):
    def __init__(self, nombre, contacto):
        super().__init__(nombre)
        self._contacto = contacto
        self._productos_suministrados = []

    def get_contacto(self):
        return self._contacto

    def set_contacto(self, contacto):
        if not contacto.strip():
            raise ValueError("El contacto no puede estar vacío.")
        self._contacto = contacto

    def get_productos_suministrados(self):
        return self._productos_suministrados

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de la clase Producto.")
        self._productos_suministrados.append(producto)


class Item:
    def __init__(self, nombre, descripcion):
        self._nombre = nombre
        self._descripcion = descripcion

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = descripcion

class Producto(Item):
    def __init__(self, nombre, categoria, precio, cantidad_inventario, proveedor):
        super().__init__(nombre, categoria)
        self._precio = precio
        self._cantidad_inventario = cantidad_inventario
        self._proveedor = proveedor

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    def get_cantidad_inventario(self):
        return self._cantidad_inventario

    def set_cantidad_inventario(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad en inventario no puede ser negativa.")
        self._cantidad_inventario = cantidad

    def get_proveedor(self):
        return self._proveedor

    def set_proveedor(self, proveedor):
        if not isinstance(proveedor, Proveedor):
            raise TypeError("El proveedor debe ser una instancia de la clase Proveedor.")
        self._proveedor = proveedor


class Promocion(Item):
    def __init__(self, nombre, descripcion, porcentaje_descuento):
        super().__init__(nombre, descripcion)
        self._porcentaje_descuento = porcentaje_descuento
        self._productos_aplicables = []

    def get_porcentaje_descuento(self):
        return self._porcentaje_descuento

    def set_porcentaje_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self._porcentaje_descuento = porcentaje

    def get_productos_aplicables(self):
        return self._productos_aplicables

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser una instancia de la clase Producto.")
        self._productos_aplicables.append(producto)

from colorama import Fore, init

init(autoreset=True)

def menu():
    productos = []
    clientes = []
    proveedores = []
    promociones = []

    while True:
        # Menú
        print(Fore.CYAN + "\n" + "="*40)
        print("=== Menú de Sistema Interactivo ===")
        print("="*40)
        print(Fore.GREEN + "1. Registrar producto")
        print("2. Registrar cliente")
        print("3. Registrar proveedor")
        print("4. Registrar promoción")
        print(Fore.YELLOW + "5. Mostrar productos")
        print("6. Realizar venta")
        print("7. Mostrar historial de compras de un cliente")
        print(Fore.RED + "8. Salir")
        print("="*40)
        
        try:
            opcion = int(input(Fore.CYAN + "\nSeleccione una opción: "))

            if opcion == 1:  # Registrar producto
                print(Fore.MAGENTA + "=== Registrar Producto ===")
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto (Alimento, Juguete, Accesorio): ")
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad en inventario: "))
                proveedor_nombre = input("Nombre del proveedor: ")

                # Crear un proveedor temporal si no existe
                proveedor = next((p for p in proveedores if p.get_nombre() == proveedor_nombre), None)
                if not proveedor:
                    contacto = input("Contacto del proveedor: ")
                    proveedor = Proveedor(proveedor_nombre, contacto)
                    proveedores.append(proveedor)
                producto = Producto(nombre, categoria, precio, cantidad, proveedor)
                productos.append(producto)
                print(Fore.GREEN + "Producto registrado con éxito.")
            
            elif opcion == 2:  # Registrar cliente
                print(Fore.MAGENTA + "=== Registrar Cliente ===")
                nombre = input("Nombre del cliente: ")
                identificacion = input("Identificación del cliente: ")
                cliente = Cliente(nombre, identificacion)
                clientes.append(cliente)
                print(Fore.GREEN + "Cliente registrado con éxito.")
            
            elif opcion == 3:  # Registrar proveedor
                print(Fore.MAGENTA + "=== Registrar Proveedor ===")
                nombre = input("Nombre del proveedor: ")
                contacto = input("Contacto del proveedor: ")
                proveedor = Proveedor(nombre, contacto)
                proveedores.append(proveedor)
                print(Fore.GREEN + "Proveedor registrado con éxito.")
            
            elif opcion == 4:  # Registrar promoción
                print(Fore.MAGENTA + "=== Registrar Promoción ===")
                nombre = input("Nombre de la promoción: ")
                descripcion = input("Descripción de la promoción: ")
                porcentaje = float(input("Porcentaje de descuento: "))
                promocion = Promocion(nombre, descripcion, porcentaje)
                print(Fore.CYAN + "Seleccione los productos para esta promoción:")
                for i, producto in enumerate(productos):
                    print(f"{i + 1}. {producto.get_nombre()}")
                seleccion = input("Ingrese los números de los productos separados por comas: ")
                indices = [int(x) - 1 for x in seleccion.split(",")]
                for idx in indices:
                    promocion.agregar_producto(productos[idx])
                promociones.append(promocion)
                print(Fore.GREEN + "Promoción registrada con éxito.")
            
            elif opcion == 5:  # Mostrar productos
                print(Fore.CYAN + "=== Lista de Productos ===")
                if not productos:
                    print(Fore.YELLOW + "No hay productos registrados.")
                else:
                    for producto in productos:
                        print(f"{producto.get_nombre()} - Categoría: {producto.get_descripcion()} - Precio: ${producto.get_precio()} - Inventario: {producto.get_cantidad_inventario()} - Proveedor: {producto.get_proveedor().get_nombre()}")
            
            elif opcion == 6:  # Realizar venta
                print(Fore.MAGENTA + "=== Realizar Venta ===")
                if not clientes:
                    print(Fore.RED + "Debe registrar clientes antes de realizar una venta.")
                elif not productos:
                    print(Fore.RED + "Debe registrar productos antes de realizar una venta.")
                else:
                    cliente_nombre = input("Ingrese el nombre del cliente: ")
                    cliente = next((c for c in clientes if c.get_nombre() == cliente_nombre), None)
                    if not cliente:
                        print(Fore.RED + "Cliente no encontrado.")
                    else:
                        productos_comprados = []
                        while True:
                            print(Fore.CYAN + "\nSeleccione un producto para la compra:")
                            for i, producto in enumerate(productos):
                                print(f"{i + 1}. {producto.get_nombre()} - Inventario: {producto.get_cantidad_inventario()} - Precio: ${producto.get_precio()}")
                            try:
                                seleccion = int(input("Ingrese el número del producto (0 para finalizar): "))
                                if seleccion == 0:
                                    break
                                producto = productos[seleccion - 1]
                                cantidad = int(input(f"Ingrese la cantidad para {producto.get_nombre()}: "))
                                if producto.get_cantidad_inventario() < cantidad:
                                    print(Fore.RED + f"No hay suficiente inventario para {producto.get_nombre()}.")
                                    continue
                                productos_comprados.append((producto, cantidad))
                            except Exception as e:
                                print(Fore.RED + f"Error: {e}. Intente nuevamente.")
                        if productos_comprados:
                            total = 0
                            for producto, cantidad in productos_comprados:
                                descuento = 0
                                for promocion in promociones:
                                    if producto in promocion.get_productos_aplicables():
                                        descuento = promocion.get_porcentaje_descuento()
                                precio_descuento = producto.get_precio() * (1 - descuento / 100)
                                total += precio_descuento * cantidad
                                producto.set_cantidad_inventario(producto.get_cantidad_inventario() - cantidad)
                            cliente.agregar_compra({
                                "productos": [(p.get_nombre(), c) for p, c in productos_comprados],
                                "total": total
                            })
                            print(Fore.GREEN + f"Venta realizada con éxito. Total: ${total:.2f}")
                        else:
                            print(Fore.YELLOW + "No se seleccionaron productos para la compra.")
            
            elif opcion == 7:  # Historial de compras
                print(Fore.MAGENTA + "=== Historial de Compras ===")
                cliente_nombre = input("Ingrese el nombre del cliente: ")
                cliente = next((c for c in clientes if c.get_nombre() == cliente_nombre), None)
                if not cliente:
                    print(Fore.RED + "Cliente no encontrado.")
                else:
                    for compra in cliente.get_historial_compras():
                        print(f"Productos: {compra['productos']}, Total: ${compra['total']:.2f}")
            
            elif opcion == 8:  # Salir
                print(Fore.YELLOW + "Saliendo del sistema. ¡Hasta luego!")
                break
            
            else:
                print(Fore.RED + "Opción no válida. Intente de nuevo.")
        
        except Exception as e:
            print(Fore.RED + f"Error: {e}. Intente nuevamente.")

        print(Fore.CYAN + "\n" + "="*40)

if __name__ == "__main__":
    menu()
