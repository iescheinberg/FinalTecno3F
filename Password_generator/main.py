import random
import string

def generar_password_letras(longitud):
    """ 
    Genera un password aleatorio de la longitud especificada.
    Genera un password solo de letras
    """
    return "".join(random.choice(string.ascii_letters) for _ in range(longitud))


def generar_password_numeros(longitud):
    """ 
    Genera un password aleatorio de la longitud especificada.
    Genera un password solo de números
    """
    return "".join(random.choice(string.digits) for _ in range(longitud))

def generar_password_completo(longitud):
    """ 
    Genera un password aleatorio de la longitud especificada.
    Genera un password completo que contenga letras y números
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))


def menu():
    """ 
    Muestra el menu y gestiona las opciones
    """
    
    while True:
        print("\n 🔒🔒 Generador de contraseñas 🔒🔒")
        print("1. Generar password de letras")
        print("2. Generar password de números")
        print("3. Generar password completo")
        print("0. Salir")
        
        try:
            opcion = int(input("Elige una opción (1-2-3-0): "))
        except ValueError:
            print("Opción incorrecta. Intente de nuevo.")
            continue
        
        if opcion == 0:
            print("¡Gracas por usar el generador de contraseñas!")
            break
        
        if opcion < 1 or opcion > 3:
            print("Opción incorrecta. Intente de nuevo.")
            continue
        
        try:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 6): "))
            if longitud < 6:
                print("\nLongitud de contraseña incorrecta. Debe ser mínimo 6. Intenta de nuevo!")
                continue
        except ValueError:
            print("Por favor, introduce un número válido para la longitud.")
            continue
        
        if opcion == 1:
            print(f"\n🔑Contraseña generada🔑: {generar_password_letras(longitud)}")
        
        elif opcion == 2:
            print(f"\n🔑Contraseña generada🔑: {generar_password_numeros(longitud)}")
        
        elif opcion == 3:
            print(f"\n🔑Contraseña generada🔑: {generar_password_completo(longitud)}")


# Ejecutar el menu
menu()
