def menu() :
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def leer_opcion() :
    try:
        while True:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6 :
                return opcion
            else:
                print("Debe ingresar una opción válida.")
    except ValueError:
        print("Debe ingresar una opción válida.")
