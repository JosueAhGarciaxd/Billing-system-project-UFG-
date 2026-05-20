#Importar librerías necesarias
import time
import os
from datetime import datetime

#Proyecto Restaurante UFG - Sistema de Pedidos y Facturación

#Cargar el Menú (índice 0 = plato 1, índice 1 = plato 2, etc.)
menu_nombres = [
    "Pupusas de queso",   # 1
    "Plato de Carne",     # 2
    "Sopa de Frijoles",   # 3
    "Yuca Frita",         # 4
    "Gaseosa/Agua",       # 5
]

menu_precios = [1.50, 6.00, 5.50, 3.00, 1.00]

#PERSISTENCIA (determinar número de factura)
ARCHIVO_FACTURAS = "facturas.txt"

#Intentamos leer el archivo de facturas para determinar el número de la próxima factura
try:
    with open(ARCHIVO_FACTURAS, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        numero_factura = 1

        # Recorremos cada línea buscando las que digan "Factura #"
        for linea in lineas:
            if linea.startswith("Factura #"):
                numero_factura = int(linea.split("#")[1].strip()) + 1
#Si el archivo no existe, asumimos que es la primera factura (Es la primera vez que se ejecuta el programa)
except FileNotFoundError:
    numero_factura = 1   #Primera vez, el archivo se creará al guardar



# Mostrar encabezado
print("**************************************")
print("         RESTAURANTE UFG              ")
print("**************************************")
#Pausa para que el usuario pueda leer el encabezado (time.sleep() hace que el programa espere un número de segundos antes de continuar)
time.sleep(3)
print("           MENÚ DEL DÍA              ")
print("--------------------------------------")
print("No.  Plato                    Precio  ")
print("--------------------------------------")

for i in range(5):
    print(f"{i+1}   {menu_nombres[i]:<25} ${menu_precios[i]:.2f}")
print("======================================")

#TOMAR EL PEDIDO
#Arreglos paralelos del pedido
#pedido_plato: guarda el índice (número de posición) del plato elegido
pedido_plato    = []   #guarda el índice del plato (0-4)
#pedido_cantidad: guarda cuántas unidades de ese plato quiere el cliente
pedido_cantidad = []   #guarda la cantidad pedida

continuar = "si"

#El ciclo se repetirá mientras el cliente quiera seguir agregando platos al pedido. El cliente puede escribir "si" o "no" para indicar si desea continuar o no. 
#El programa acepta cualquier variación de "si" (como "Si", "SI", "sI") gracias al uso de .lower() que convierte la entrada a minúsculas antes de compararla con "si".
while continuar.lower() == "si":

    #Pedir y validar opción del menú
    while True:
        try:
            opcion = int(input("\nIngrese el número del plato que desea (1-5): "))
            if opcion < 1 or opcion > 5:
                print("Opción inválida. Por favor elija entre 1 y 5.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido.")

    #Pedir y validar cantidad
    while True:
        try:
            cantidad = int(input(f"¿Cuántas unidades de {menu_nombres[opcion-1]} desea? "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un número válido.")

    #Guardar en los arreglos paralelos
    pedido_plato.append(opcion - 1)   #convertimos a índice 0-4
    pedido_cantidad.append(cantidad)
    print("Plato agregado al pedido.")

    continuar = input("¿Desea agregar otro plato? (si/no): ").strip()
    #.strip() elimina espacios en blanco al inicio y al final del texto ingresado

time.sleep(3)

#"cls" limpia la pantalla en Windows, "clear" la limpia en Linux/Mac
os.system("cls" if os.name == "nt" else "clear")


#Calcular el total y mostrar la factura

subtotal = 0.0

print("\n")
print("======================================")
print("               CUENTA                ")
print("======================================")
print(f"{'Plato':<25} {'Cant.':>5}  {'Subtotal':>9}")
print("--------------------------------------")

for i in range(len(pedido_plato)):
    idx      = pedido_plato[i]
    cantidad = pedido_cantidad[i]
    precio   = menu_precios[idx]
    linea    = precio * cantidad

    print(f"{menu_nombres[idx]:<25} x{cantidad:>4}   ${linea:.2f}")
    subtotal += linea

#Aplicar impuesto del 13% (IVA)
#Aplicar descuento del 10% si el subtotal supera los $20

impuesto = subtotal * 0.13
total    = subtotal + impuesto

print("--------------------------------------")
print(f"Subtotal:                      ${subtotal:.2f}")
print(f"IVA (13%):                     ${impuesto:.2f}")
print("======================================")
print(f"TOTAL A PAGAR:                 ${total:.2f}")
print("======================================")

# PENDIENTE: Persistencia de datos (guardar factura en un archivo de texto)
# PERSISTENCIA: GUARDAR FACTURA

#Obtenemos la fecha y hora actual con el formato "día/mes/año hora:minuto:segundo"
fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open(ARCHIVO_FACTURAS, "a", encoding="utf-8") as f:
    #f.write() escribe una línea en el archivo (equivalente a print() pero en el archivo)
    f.write(f"Factura #{numero_factura}\n")
    f.write(f"Fecha y hora: {fecha_hora}\n")
    f.write("--------------------------------------\n")
    f.write(f"{'Plato':<25} {'Cant.':>5}  {'Subtotal':>9}\n")
    f.write("--------------------------------------\n")

    for i in range(len(pedido_plato)):
        idx      = pedido_plato[i]
        cantidad = pedido_cantidad[i]
        precio   = menu_precios[idx]
        linea    = precio * cantidad
        f.write(f"{menu_nombres[idx]:<25} x{cantidad:>4}      ${linea:.2f}\n")

    #Escribimos los totales al final de la factura
    f.write("--------------------------------------\n")
    f.write(f"Subtotal:             ${subtotal:.2f}\n")
    f.write(f"IVA (13%):            ${impuesto:.2f}\n")
    f.write("======================================\n")
    f.write(f"TOTAL A PAGAR:        ${total:.2f}\n")
    f.write("======================================\n")
    f.write("\n")

#Mensaje final de confirmación en pantalla
print(f"\nFactura #{numero_factura} guardada en '{ARCHIVO_FACTURAS}'")
print("\nGracias por visitar el restaurante UFG")
print("Regrese Pronto :D")