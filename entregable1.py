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
        self.piezas_respuesto = list(str)

class Ubicacion(Enum):
    Endor = 1
    Cúmulo_Raimos = 2
    Nebulosa = 3
    Kaliida = 4

class Clase(Enum):
    Ejecutor = 1
    Eclipse = 2
    Soberano = 3

class Estacion_Espacial(Nave):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int, tripulacion:int, pasaje:int, ubicacion:Ubicacion):
        super().__init__(nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class Nave_Estelar(Nave):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int, tripulacion:int, pasaje:int, clase:Clase):
        super().__init__(nombre)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = clase

class Caza_Estelar(Nave):
    def __init__(self, nombre:str ,id_combate:str, c_transmision:int, dotacion:int):
        super().__init__(nombre)
        self.dotacion = dotacion

class Repuesto():
    def __init__(self, nombre:str, proveedor:str, n_disponibles:int, precio:float):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__n_disponibles = n_disponibles
        self.precio = precio

class Almacen():
    def __init__(self,nombre:str, localizacion:str, catalogo:list[Repuesto]):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo = catalogo

class Usuario():
    def __init__(self,nombre:str):
        self.nombre = nombre

class Comandante(Usuario):
    def __init__(self,nombre:str,nave:Nave):
        super.__init__(nombre)
        self.nave = nave

class Operario(Usuario):
    def __init__(self,nombre,almacen:Almacen):
        super.__init__(nombre)
        self.almacen = almacen