# Mantenimiento espacial
from enum import Enum

class Unidad_Combate():
    def __init__(self, id_combate:str, c_transmision:int):
        self.id_combate = id_combate
        self.c_transmision = c_transmision

    def __str__(self):
        return f"Unidad de Combate {self.id_combate} (transmisión={self.c_transmision})"

class Nave(Unidad_Combate):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int):
        super().__init__(id_combate,c_transmision)
        self.nombre = nombre
        self.piezas_repuesto = []

    def __str__(self):
        return f"Nave {self.nombre} [{self.id_combate}] - Transmisión {self.c_transmision}"

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

    def __str__(self):
        return (f"Estación Espacial {self.nombre} [{self.id_combate}] - "
                f"Ubicación: {self.ubicacion.name}, Tripulación: {self.tripulacion}, Pasaje: {self.pasaje}")

class Nave_Estelar(Nave):
    def __init__(self, nombre:str, id_combate:str, c_transmision:int, tripulacion:int, pasaje:int, clase:Clase):
        super().__init__(nombre,id_combate,c_transmision)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

    def __str__(self):
        return (f"Nave Estelar {self.nombre} [{self.id_combate}] - Clase: {self.clase.name}, "
                f"Tripulación: {self.tripulacion}, Pasaje: {self.pasaje}")

class Caza_Estelar(Nave):
    def __init__(self, nombre:str ,id_combate:str, c_transmision:int, dotacion:int):
        super().__init__(nombre,id_combate,c_transmision)
        self.dotacion = dotacion

    def __str__(self):
        return f"Caza Estelar {self.nombre} [{self.id_combate}] - Dotación: {self.dotacion}"

class Repuesto():
    def __init__(self, nombre:str, proveedor:str, stock:int, precio:float):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__stock = stock
        self.precio = precio
    
    def get_disponibles(self) -> int:
        return self.__stock

    def agregar_stock(self, n):
        try:
            if n < 0:
                raise ValueError("No se puede agregar stock negativo")
            self.__stock += n
        except TypeError:
            print("Error: la cantidad a agregar debe ser un número")
        except ValueError as e:
            print(f"Error: {e}")

    def retirar_stock(self, n):
        try:
            if n < 0:
                raise ValueError("No se puede retirar cantidad negativa")
            if (self.__stock - n) >= 0:
                self.__stock -= n
            else:
                raise ValueError("No hay suficiente stock para retirar")
        except TypeError:
            print("Error: la cantidad a retirar debe ser un número")
        except ValueError as e:
            print(f"Error: {e}")
    
    def __str__(self) -> str:
        return f"Repuesto: {self.nombre} | Proveedor: {self.proveedor} | Stock: {self.get_disponibles()} | Precio: {self.precio} cr"

class Almacen():
    def __init__(self, nombre:str, localizacion:str, catalogo:list[Repuesto] = None):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo = catalogo if catalogo is not None else []
    
    def __str__(self):
        return f"Almacén {self.nombre} ({self.localizacion}) - {len(self.catalogo)} repuestos"

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

    def __str__(self):
        return f"Usuario {self.usuario}"

class Comandante(Usuario):
    def __init__(self,usuario:str,nave:Nave):
        super().__init__(usuario)
        self.nave = nave
    
    def __str__(self):
        return f"Comandante {self.usuario} (Nave: {self.nave.nombre})"

    def consultar_disponibilidad(self,nombre_repuesto:str,almacen:Almacen):
        repuesto = almacen.buscar_repuesto(nombre_repuesto)

        if repuesto is not None:
            print(f"Quedan {repuesto.get_disponibles()} {repuesto.nombre}")
        else:
            print(f"el repuesto {nombre_repuesto} no esta disponible en este almacen")
    
    def adquirir_repuesto(self, nombre_repuesto:str, almacen:Almacen, n:int):
        try:
            if n <= 0:
                raise ValueError("La cantidad a adquirir debe ser mayor que cero")

            repuesto = almacen.buscar_repuesto(nombre_repuesto)
            if repuesto is None:
                raise LookupError(f"El repuesto '{nombre_repuesto}' no está disponible en el almacén")

            repuesto.retirar_stock(n)
            print(f"{self.usuario} ha adquirido {n} unidades de {nombre_repuesto}.")
        except Exception as e:
            print(f"Error al adquirir repuesto: {e}")

class Operario(Usuario):
    def __init__(self,usuario,almacen:Almacen):
        super().__init__(usuario)
        self.almacen = almacen

    def __str__(self):
        return f"Operario {self.usuario} (Almacén: {self.almacen.nombre})"
    
    def añadir_repuesto(self, repuesto: Repuesto):
        self.almacen.agregar_catalogo(repuesto)
    
    def cambiar_stock(self,nombre_repuesto:str,n:int):
        try:
            repuesto = self.almacen.buscar_repuesto(nombre_repuesto)

            if repuesto is None:
                raise LookupError(f"El repuesto '{nombre_repuesto}' no existe en el almacén")

            if n > 0:
                repuesto.agregar_stock(n)
            else:
                repuesto.retirar_stock(-n)
        except Exception as e:
            print(f"Error al cambiar stock: {e}")


def main():
    try:
        # Instanciamos algunas naves
        estacion = Estacion_Espacial("Outpost 42", "EST-001", 1234, tripulacion=120, pasaje=0, ubicacion=Ubicacion.Endor)
        caza = Caza_Estelar("Interceptor", "CZA-007", 9876, dotacion=2)

        # Creamos un almacén con algunos repuestos
        repuesto1 = Repuesto("Motor hiperespacial", "Initech", stock=5, precio=3000.0)
        repuesto2 = Repuesto("Panel de energia", "WayneTech", stock=10, precio=450.0)
        almacen = Almacen("Almacén Central", "Sector 7", catalogo=[repuesto1, repuesto2])

        # Operario añade un nuevo repuesto
        ope = Operario("Juan", almacen)
        ope.añadir_repuesto(Repuesto("Escudo deflector", "Stark", stock=3, precio=1200.0))

        # Comandante consulta y adquiere repuestos
        com = Comandante("Leia", estacion)
        com.consultar_disponibilidad("Motor hiperespacial", almacen)
        com.adquirir_repuesto("Motor hiperespacial", almacen, 2)

        # Forzar un error con una cantidad inválida
        com.adquirir_repuesto("Panel de energia", almacen, -1)
    except Exception as e:
        print(f"Ocurrió un error en la ejecución principal: {e}")


if __name__ == "__main__":
    main()
        