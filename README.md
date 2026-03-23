# PCD Entregable 1: Sistema de Gestión de Mantenimiento de la Flota Espacial

## Descripción

Este proyecto implementa un sistema de gestión de mantenimiento para la flota espacial del Imperio Galáctico, desarrollado en Python utilizando principios de programación orientada a objetos (POO). El sistema permite gestionar diferentes tipos de naves, repuestos, almacenes y usuarios (comandantes y operarios), facilitando la consulta, adquisición y mantenimiento de piezas de repuesto.

El proyecto cumple con los requisitos del enunciado del entregable 1 del curso de Programación para Ciencia de Datos (2025/2026), incluyendo herencia, enumeraciones, encapsulamiento, gestión de excepciones y tests unitarios.

## Características Principales

### Clases Implementadas
- **Unidad_Combate**: Clase base para unidades de combate con ID y clave de transmisión.
- **Nave**: Hereda de Unidad_Combate, representa naves con nombre y lista de piezas de repuesto.
- **Estacion_Espacial**: Nave especializada con tripulación, pasaje y ubicación.
- **Nave_Estelar**: Nave especializada con tripulación, pasaje y clase.
- **Caza_Estelar**: Nave especializada con dotación.
- **Repuesto**: Gestiona piezas con nombre, proveedor, stock (privado), precio y métodos de utilidad.
- **Almacen**: Contiene catálogo de repuestos con métodos de búsqueda e inventario.
- **Usuario**: Clase base para usuarios del sistema.
- **Comandante**: Usuario que puede consultar y adquirir repuestos, además de comparar precios.
- **Operario**: Usuario que gestiona el catálogo y stocks de almacenes.

### Funcionalidades
- **Gestión de Stock**: Agregar/retirar stock con validaciones y excepciones.
- **Consultas y Adquisiciones**: Comandantes pueden consultar disponibilidad y adquirir repuestos.
- **Utilidades**: Cálculo de precios totales, verificación de disponibilidad, actualización de precios, inventarios, búsquedas por proveedor, eliminación de repuestos.
- **Comparación de Precios**: Buscar el mejor precio entre múltiples almacenes.
- **Representación String**: Todas las clases tienen método `__str__` para impresión legible.

### Técnicas POO Utilizadas
- **Herencia**: Jerarquía de clases (Unidad_Combate → Nave → subclases de naves).
- **Encapsulamiento**: Atributos privados (ej. `__stock` en Repuesto).
- **Enumeraciones**: Ubicacion y Clase para valores fijos.
- **Polimorfismo**: Métodos `__str__` en todas las clases.
- **Gestión de Excepciones**: Validaciones en métodos con try/except y raise de ValueError/LookupError.

## Instalación

1. **Requisitos Previos**:
   - Python 3.x instalado.
   - pytest para ejecutar tests: `pip install pytest`

2. **Clonación del Repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/pcd_entregable1_tu-nombre.git
   cd pcd_entregable1_tu-nombre
   ```

3. **Ejecución**:
   - Programa principal: `python Entregable1.py`
   - Tests: `pytest tests.py`

## Uso

### Ejecución del Programa
Ejecuta `python Entregable1.py` para ver un caso de uso completo que demuestra todas las funcionalidades:
- Creación de naves, almacenes y usuarios.
- Operaciones de operarios (añadir repuestos, cambiar stock).
- Operaciones de comandantes (consultar, adquirir, comparar precios).
- Utilidades de repuestos y almacenes.
- Pruebas de excepciones.

### Ejecución de Tests
Ejecuta `pytest tests.py` para validar todas las funcionalidades con tests unitarios que cubren:
- Creación y modificación de instancias.
- Métodos de utilidad (precios, inventarios, búsquedas).
- Validaciones y excepciones.

## Estructura del Proyecto

```
Entregable1/
├── Entregable1.py          # Código principal con clases y función main()
├── tests.py                # Tests unitarios con pytest
├── enunciado_entregable.txt # Enunciado del ejercicio
└── README.md               # Este archivo
```

## Desarrollo y Versionado

El proyecto utiliza Git para control de versiones:
- **Rama main**: Proyecto final.
- **Rama development**: Desarrollo incremental.
- **Tags**: v1.0 (versión funcional inicial).

Repositorio público en GitHub: [pcd_entregable1_tu-nombre](https://github.com/tu-usuario/pcd_entregable1_tu-nombre)

## Contribución

Proyecto académico desarrollado para el curso de Programación para Ciencia de Datos. No se aceptan contribuciones externas.

## Licencia

Este proyecto no tiene licencia específica y es propiedad del autor para fines educativos.

## Autor

Roberto - Estudiante de Ciencia e Ingeniería de Datos, Universidad Politécnica de Cartagena.