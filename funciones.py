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

def añadir_estudiante(lista):
    try:
        while True:
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            if nombre_estudiante != "" :
                break
            else:
                print("El nombre no puede estar vacío ni ser solo espacios en blanco.")
        while True:
            edad_estudiante = int(input("Ingrese la edad del estudiante: "))
            if edad_estudiante > 0 :
                break
            else:
                print("La edad debe ser un número entero mayor que cero.")
        while True:
            nota_estudiante = float(input("Ingrese la nota del estudiante: "))
            if 1 <= nota_estudiante <= 7 :
                break
            else:
                print("La nota debe ser un número decimal entre 1.0 y 7.0.")

        alumno = {
        "nombre": nombre_estudiante,
        "edad": edad_estudiante,
        "nota": nota_estudiante,
        "estado": ""
    }

        lista.append(alumno)
        print("Alumno agregado correctamente")
        
    except ValueError:
        print("Ingrese un tipo de dato válido")

def buscar_estudiante(lista):
    if not lista:
        print("No hay estudiantes registrados")
        return
    
    estudiante_b = input("Ingrese el nombre del estudiante: ")
    encontrado = False
    
    for i, estudiante in enumerate(lista):
        if estudiante_b == estudiante["nombre"]:
            print(str(i+1) + ".")
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])
            print("Nota:", estudiante["nota"])
            print("Estado:", estudiante["estado"])
            encontrado = True
    
    if not encontrado:
        print("El estudiante no está registrado")

            

def mostrar_estudiante(lista):
    if not lista:
        print("No hay estudiantes registrados")
        return
    print("=== LISTA DE ESTUDIANTES ===")
    for i, estudiante in enumerate(lista):
        print(str(i+1)+".")
        print("Nombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Nota:", estudiante["nota"])
        print("Estado:", estudiante["estado"])
        print("******************************************** ")


def eliminar_estudiante(lista):
    if not lista:
        print("No hay estudiantes registrados")
        return
    estudiante_e = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if estudiante not in lista:
        print("No hay estudiantes registrados")
        return
    else:
        for estudiante in lista :
            if estudiante_e == estudiante["nombre"] :
                lista.pop(estudiante)

def actualizar_estado(lista):
    if not lista :
        print("No hay estudiantes registrados")
        return
    for estudiante in lista:
        if estudiante["nota"] >= 4 :
            estudiante["estado"] = "APROBADO"
        elif estudiante["nota"] <= 4 :
            estudiante["estado"] = "REPROBADO"
    

