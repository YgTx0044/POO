class Inventario:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("⚠️ El precio debe ser mayor a 0")

    def datos_inventario(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }
