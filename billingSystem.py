#Importar librerías necesarias
import time
import os
from datetime import datetime

#Proyecto Restaurante UFG - Sistema de Pedidos y Facturación

#Cargar el Menú (índice 0 = plato 1, índice 1 = plato 2, etc.)
menu_nombres = [
    "Pupusas de Especialidad",   # 1
    "Plato de Comida Tipica",    # 2
    "Sopa del Día",              # 3
    "Antojitos",                 # 4
    "Gaseosa",                   # 5
    "Agua",                      # 6
]

 #Precios correspondientes a cada plato 
menu_precios = [1.50, 5.00, 5.50, 1.00, 1.25, 1.00] 

# SUB-OPCIONES: Especialidades disponibles para los platos que las requieren.
# Clave: índice del plato en menu_nombres (0-based).
# Valor: lista de especialidades disponibles para ese plato.
especialidades = {
    0: [                         # Pupusas de Especialidad (índice 0)
        "Queso",
        "Frijol con Queso",
        "Revueltas",
        "Otro...",
    ],
    3: [                         # Antojitos (índice 3)
        "Yuca",
        "Empanadas",
        "Pasteles",
        "Otro...",
    ],
}

#PERSISTENCIA (determinar número de factura)
ARCHIVO_FACTURAS = "FacturasUFG.txt"

#Intentamos leer el archivo de facturas para determinar el número de la próxima factura
try:
    with open(ARCHIVO_FACTURAS, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        numero_factura = 1

        #Recorremos cada línea buscando las que digan "Factura #"
        for linea in lineas:
            if linea.startswith("Factura #"):
                #Extraemos el número de factura de la línea (dividimos por "#" y tomamos la parte después del "#", luego convertimos a entero y sumamos 1 para la próxima factura)
                numero_factura = int(linea.split("#")[1].strip()) + 1
#Si el archivo no existe, asumimos que es la primera factura (Es la primera vez que se ejecuta el programa)
except FileNotFoundError:
    numero_factura = 1   #Primera vez, el archivo se creará al guardar



#Mostrar encabezado
print("**************************************")
print("         RESTAURANTE UFG              ")
print("**************************************")
#Pausa para que el usuario pueda leer el encabezado (time.sleep() hace que el programa espere un número de segundos antes de continuar)
time.sleep(3)
print("           MENÚ DEL DÍA              ")
print("--------------------------------------")
print("No.  Plato                    Precio  ")
print("--------------------------------------")

for i in range(6):
    print(f"{i+1}   {menu_nombres[i]:<25} ${menu_precios[i]:.2f}")
print("======================================")

#TOMAR EL PEDIDO
#Arreglos paralelos del pedido
#pedido_plato: guarda el índice (número de posición) del plato elegido
pedido_plato    = []   #guarda el índice del plato (0-5)
#pedido_cantidad: guarda cuántas unidades de ese plato quiere el client
pedido_cantidad = []   #guarda la cantidad pedida
#pedido_nombre_final: guarda el nombre del plato con su especialidad (si aplica)
pedido_nombre_final = []   #guarda el nombre completo del plato, incluyendo especialidad

continuar = "si"

#El ciclo se repetirá mientras el cliente quiera seguir agregando platos al pedido. El cliente puede escribir "si" o "no" para indicar si desea continuar o no. 
#El programa acepta cualquier variación de "si" (como "Si", "SI", "sI") gracias al uso de .lower() que convierte la entrada a minúsculas antes de compararla con "si".
while continuar == "si":

    #Pedir y validar opción del menú
    while True:
        try:
            opcion = int(input("\nIngrese el número del plato que desea (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Opción inválida. Por favor elija entre 1 y 6.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un carácter válido.")

    # SUB-OPCIONES: Si el plato elegido tiene especialidades disponibles,
    # mostramos el submenú y pedimos al usuario que elija una.
    idx_plato = opcion - 1   #convertimos a índice 0-based para verificar en el diccionario

    if idx_plato in especialidades:
        #Mostramos las especialidades disponibles para el plato elegido
        print(f"\n{menu_nombres[idx_plato]} disponibles:")
        lista_especialidades = especialidades[idx_plato]
        for j, esp in enumerate(lista_especialidades):
            print(f"  {j+1}. {esp}")

        #Pedimos y validamos la especialidad deseada
        while True:
            try:
                opcion_esp = int(input(f"Elija una especialidad (1-{len(lista_especialidades)}): "))
                if opcion_esp < 1 or opcion_esp > len(lista_especialidades):
                    print(f"Opción inválida. Por favor elija entre 1 y {len(lista_especialidades)}.")
                else:
                    break
            except ValueError:
                print("Por favor ingrese un carácter válido.")

        #Construimos el nombre final uniendo el nombre base del plato con la especialidad elegida.
        #Ejemplo: "Pupusa de Frijol con Queso" o "Antojitos"
        especialidad_elegida = lista_especialidades[opcion_esp - 1]
        nombre_plato_final = f"{menu_nombres[idx_plato].replace('de Especialidad', '').strip()} {especialidad_elegida}"

    else:
        #El plato no tiene especialidades; usamos el nombre tal como está en el menú
        nombre_plato_final = menu_nombres[idx_plato]

    #Pedir y validar cantidad
    while True:
        try:
            #El mensaje muestra el nombre final del plato (con especialidad si aplica)
            cantidad = int(input(f"¿Cuántas unidades de {nombre_plato_final} desea? "))
            if cantidad < 1 or cantidad > 200:
                print("Cantidad inválida. Por favor elija un rango entre 1 y 200 unidades.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un carácter válido.")

    #Guardar en los arreglos paralelos
    pedido_plato.append(idx_plato)           #índice 0-5 del plato base (para obtener el precio)
    pedido_cantidad.append(cantidad)
    pedido_nombre_final.append(nombre_plato_final)   #nombre completo con especialidad
    print("Plato agregado al pedido.")

    # Validación:bucle que repite la pregunta si la respuesta no es "si" o "no"
    while True:
        continuar = input("¿Desea agregar otro plato? (si/no): ").strip().lower()
        #.strip() elimina espacios en blanco al inicio y al final del texto ingresado
        #.lower() converts la entrada a minúsculas para aceptar "Si", "SI", "sI", etc.
        if continuar in ("si", "no"):
            break   #Salimos del bucle solo si la respuesta es válida
        print("Opción inválida. Por favor, ingrese 'si' o 'no'.")

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
    #Usamos pedido_nombre_final[i] para mostrar el nombre completo con especialidad
    print(f"{pedido_nombre_final[i]:<25} x{cantidad:>4}   ${linea:.2f}")
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
        #Usamos pedido_nombre_final[i] para guardar el nombre completo con especialidad
        f.write(f"{pedido_nombre_final[i]:<25} x{cantidad:>4}      ${linea:.2f}\n")

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

time.sleep(2)
print("\nGracias por visitar el restaurante UFG")
print("Regrese Pronto :D")
print("\n")