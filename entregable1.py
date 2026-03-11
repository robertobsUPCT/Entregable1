# Mantenimiento espacial
from enum import Enum

class Unidad_Combate():
    def __init__(self, id_combate:str, c_transmision:int):
        self.id_combate = id_combate
        self.c_transmision = c_transmision

class Nave(Unidad_Combate):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int):
        super().__init__(id_combate,c_transmision)
        self.nombre = nombre
        self.piezas_repuesto = []

class Ubicacion(Enum):
    Endor = 1
    Cúmulo_Raimos = 2
    Nebulosa_Kaliida = 3

class Clase(Enum):
    Ejecutor = 1
    Eclipse = 2
    Soberano = 3

class Estacion_Espacial(Nave):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int, tripulacion:int, pasaje:int, ubicacion:Ubicacion):
        super().__init__(nombre,id_combate,c_transmision)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class Nave_Estelar(Nave):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int, tripulacion:int, pasaje:int, clase:Clase):
        super().__init__(nombre,id_combate,c_transmision)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

class Caza_Estelar(Nave):
    def __init__(self, nombre:str ,id_combate:str, c_transmision:int, dotacion:int):
        super().__init__(nombre,id_combate,c_transmision)
        self.dotacion = dotacion

class Repuesto():
    def __init__(self, nombre:str, proveedor:str, stock:int, precio:float):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__stock = stock
        self.precio = precio
    
    def get_disponibles(self) -> int:
        return self.__stock

    # def set_disponibles(self, nueva_cantidad: int):
    #     if nueva_cantidad >= 0:
    #         self.__stock = nueva_cantidad
    #     else:
    #         print("Error: El stock no puede ser negativo")

    def agregar_stock(self,n):
        self.__stock += n

    def retirar_stock(self,n):
        if (self.__stock-n)>=0:
            self.__stock -= n
        else:
            print("no se actulizo el stock porque seria negativo")
    
    def __str__(self) -> str:
        return f"Repuesto: {self.nombre} | Proveedor: {self.proveedor} | Stock: {self.get_disponibles()} | Precio: {self.precio} cr"

class Almacen():
    def __init__(self, nombre:str, localizacion:str, catalogo:list[Repuesto] = None):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo = catalogo if catalogo is not None else []
    
    def buscar_repuesto(self, nom) -> Repuesto:
        for repuesto in self.catalogo:
            if repuesto.nombre == nom:
                return repuesto
        return None
    
    def mostrar_catalogo(self):
        for repuesto in self.catalogo:
            print(repuesto)

    def agregar_catalogo(self, repuesto:Repuesto):
        self.catalogo.append(repuesto)


class Usuario():
    def __init__(self,usuario:str):
        self.usuario = usuario

class Comandante(Usuario):
    def __init__(self,usuario:str,nave:Nave):
        super().__init__(usuario)
        self.nave = nave
    
    def consultar_disponibilidad(self,nombre_repuesto:str,almacen:Almacen):
        repuesto = almacen.buscar_repuesto(nombre_repuesto)

        if repuesto is not None:
            print(f"Quedan {repuesto.get_disponibles()} {repuesto.nombre}")
        else:
            print(f"el repuesto {nombre_repuesto} no esta disponible en este almacen")
    
    def adquirir_repuesto(self, nombre_repuesto:str, almacen:Almacen, n:int):
        repuesto = almacen.buscar_repuesto(nombre_repuesto)

        if repuesto is not None:
            pass

class Operario(Usuario):
    def __init__(self,usuario,almacen:Almacen):
        super().__init__(usuario)
        self.almacen = almacen
    
    def añadir_repuesto(self, repuesto: Repuesto):
        self.almacen.agregar_catalogo(repuesto)
    
    def cambiar_stock(self,nombre_repuesto:str,n:int):
        repuesto = self.almacen.buscar_repuesto(nombre_repuesto)

        if repuesto is not None:
            if n > 0:
                repuesto.agregar_stock(n)
            else:
                repuesto.retirar_stock(-n)
        