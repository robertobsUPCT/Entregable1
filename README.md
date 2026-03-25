# Entregable 1: Gestión de Flota Espacial

Un sistema en Python para gestionar naves, repuestos y usuarios.

## ¿Qué hace?

- Crear diferentes tipos de naves (Estación Espacial, Nave Estelar, Caza Estelar)
- Guardar y controlar el stock de repuestos
- Comandantes pueden consultar, comprar repuestos y comparar precios
- Operarios pueden añadir repuestos y cambiar stock

## Clases principales

- `Unidad_Combate` → `Nave` → naves especializadas
- `Repuesto` - stock privado, métodos de precio y disponibilidad
- `Almacen` - catálogo de repuestos
- `Usuario` → `Comandante` / `Operario`

## Cómo ejecutar

```bash
# Ejecutar el programa
python Entregable1.py

# Ejecutar tests
pytest tests.py
```

## Archivos

- `Entregable1.py` - Todo el código
- `tests.py` - Tests unitarios
- `README.md` - Este archivo
-  `diagramas` - carpeta con los diagramas
     - `DiagramaUML.uxf` - Diagrama de Clases
     - `Diagramas_Secuencia.uxf` - Diagramas de Secuencia
     - `diagrama_caso_uso.uxf` - Diagrama de Caso de Uso


## Técnicas POO

- Herencia (clases padre/hijas)
- Encapsulamiento (__stock privado)
- Enumeraciones (Ubicacion, Clase)
- Excepciones (validaciones)
- `__str__` en todas las clases
- Abstraccion (Clases Abstractas)

**Estado:** ✅ Completado y testeado

Autor: Roberto Bermudez Sevilla
