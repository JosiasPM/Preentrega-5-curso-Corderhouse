# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Selecciona una opción: "))
        return opcion
    except ValueError:
        print("Error: debes ingresar un número.")
        return None