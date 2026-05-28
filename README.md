# 🇸🇻 RESTAURANTE UFG — Sistema de Facturación Digital

¡Bienvenido al repositorio de la **RESTAURANTE UFG **! Este es un proyecto escolar desarrollado en Python que simula el sistema de toma de pedidos y facturación automatizada para un restaurante especializado en gastronomía tradicional salvadoreña. 

El sistema gestiona de manera eficiente el flujo completo de una venta: desde el despliegue del menú interactivo, pasando por la validación estricta de las órdenes, hasta el cálculo final de los impuestos y el almacenamiento persistente de los comprobantes fiscales.

---

## 📝 Descripción del Proyecto

Este software fue diseñado para resolver las necesidades operativas básicas de un negocio de comida típica mediante una interfaz de consola ágil e intuitiva. Su principal atractivo es la **dinamicidad en la selección de platillos**, permitiendo al operador personalizar pedidos masivos como las pupusas o los antojitos fritos sin romper la estructura de almacenamiento interna. Además, garantiza la integridad del negocio mediante filtros que evitan la introducción de datos erróneos o maliciosos.

---

## ✨ Características Principales (Features)

* **🗂️ Estructura de Arreglos Paralelos:** Mapea el menú base (platillos y precios) y lo procesa de forma síncrona con el arreglo dinámico del "pedido" (índices seleccionados y cantidades).
* **🌽 Especialidades Dinámicas:** Al elegir bases generales como *Pupusas* o *Antojitos*, el sistema despliega un sub-menú inmediato para especificar la variedad (ej. queso, revueltas, yuca, empanadas). El sistema concatena esta especificación al nombre final del producto antes de procesarlo.
* **🛡️ Validación de Cantidades de Seguridad:** Incorpora un bucle de control robusto que restringe el ingreso de unidades a un rango comercial lógico y realista por plato, bloqueando valores absurdos o accidentales (como `999999`).
* **🧮 Módulo de Cálculo Fiscal:** Computa de forma automática el subtotal acumulado de la orden, desglosa el Impuesto al Valor Agregado (IVA) correspondiente y totaliza el monto neto de cara al cliente.
* **💾 Persistencia de Datos:** Implementa lecturas y escrituras físicas en el archivo local `facturas.txt`. El programa autodetecta el correlativo de la última venta para asignar un **ID único** por factura y estampa de forma exacta la fecha y hora de la transacción.

---

## 🛠️ Tecnologías Utilizadas

Para garantizar la portabilidad y ligereza del sistema, se utilizaron únicamente tecnologías nativas de Python, eliminando la necesidad de dependencias externas:

* **Python 3.x** (Lenguaje principal de desarrollo)
* **Módulo `datetime`** (Para la captura y formateo del tiempo real de la transacción)
* **Módulo `os`** (Para la limpieza dinámica de la consola entre pantallas de usuario)
* **Módulo `time`** (Para la gestión de transiciones cronometradas en la interfaz)

---

## 📄 Instalación

Bash:
git clone [https://github.com/tu-usuario/caja-registradora-ufg.git](https://github.com/tu-usuario/caja-registradora-ufg.git)

---

## 📄 Ejemplo de Factura (`facturas.txt`)

Cada vez que se cierra una orden de manera exitosa, el sistema añade una estructura limpia y estandarizada al archivo histórico. A continuación se muestra cómo se visualiza un registro real en el archivo:

```text
Factura #42
Fecha y hora: 27/05/2026 19:42:15
--------------------------------------------------------
Plato                                    Cant.  Subtotal
--------------------------------------------------------
Pupusas Queso                            x   1   $  1.50
Antojitos Yuca                           x   4   $  4.00
Agua                                     x   3   $  3.00
--------------------------------------------------------
Subtotal:                                       $  8.50
IVA (13%):                                      $  1.10
========================================================
TOTAL A PAGAR:                                  $  9.61
========================================================
