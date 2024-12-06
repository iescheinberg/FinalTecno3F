# Se importan los modulos necesarios
import random, json


# Funcion para cargar tickets creados
def cargar_tickets():
    try:
        with open('tickets.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Se guarda los datos en un diccionario
tickets = cargar_tickets()


# Guardar tickets en archivo .JSON
def guardar_tickets():
    with open('tickets.json', 'w') as f:
        json.dump(tickets, f)
        print("\nTicket guardado correctamente✔")





# Funcion para generar numero aleatorio entre 1000 y 9999 
def crear_numero_ticket():
    return random.randint(1000, 9999)





# Funcion para ingresar datos del ticket
def alta_ticket():
    print("Ingrese los datos para generar un nuevo Ticket")
    nombre = input("Ingrese su nombre: ")
    sector = input("Ingrese su sector: ")
    asunto = input("Ingrese asunto: ")
    problema = input("Ingrese un mensaje: ")

    # Genero numero de ticket y guardo en una variable
    numero_ticket = crear_numero_ticket()

    # Guardar ticket generado
    tickets[numero_ticket] = {
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "problema": problema
    }

    # Mostrar ticket generado
    print(f"\nTicket generado: {numero_ticket}")
    print(f"Nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Problema: {problema}")
    print("\n⚠Recuerde su número de Ticket!⚠")

    guardar_tickets()


    # Preguntar si desea crear otro ticket
    pregunta = input("¿Desea crear otro ticket? (s/n): ").strip().lower()
    if pregunta == "s":
        alta_ticket()
    else:
        menu_principal()




# Funcion para leer tickets
def leer_ticket():
    # Solcitar un numero de ticket
    numero_ticket = int(input("Ingresá un número de ticket: "))

    if numero_ticket in tickets:
        ticket = tickets[numero_ticket]
        print(f"`\nTicket número: {numero_ticket}")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Problema: {ticket['problema']}\n")
    
    else:
        print("\n❌Ticket no encontrado❌")
    
    leer_otro_ticket = input("¿Desea leer otro ticket? (s/n): ").strip().lower()

    if leer_otro_ticket == "s":
        leer_ticket()
    else:
        menu_principal()


def salir():
    # Confirmar salida del programa
    confirmacion = input("¿Está seguro que desea salir del programa? (s/n): ").strip().lower()

    if confirmacion == "s":
        print("Saliendo del programa...")
        exit()
    else:
        menu_principal()




def menu_principal():
    while True:
        # Muestro menu por pantalla
        print("\n🔹🔹MENU🔹🔹")
        print("1. Alta Ticket: ")
        print("2. Leer Ticket: ")
        print("3. Salir: ")

        # Ingresar opcion de menu
        opcion = input("Seleccione una opcion de menú(1/2/3): ").strip()

        # Evitar que el usuario ingrese una opcion invalida
        if opcion.isdigit():
            opcion = int(opcion) #convertir opcion en entero

            if opcion == 1:
                # Llamar a la funcion alta_ticket
                print("\nSeleccionaste Alta Ticket: ")
                alta_ticket()
            
            elif opcion == 2:
                # Llamar a la funcion leer_ticket
                print("\nSeleccionaste Leer Ticket: ")
                leer_ticket()
            
            elif opcion == 3:
                guardar_tickets()
                salir()
            
            else:
                print("Opción no válida. Intente nuevamente: ")


# Ejecucion del programa
menu_principal()




















