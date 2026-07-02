#Importar
from funciones import menu, leer_opcion, añadir_estudiante, buscar_estudiante, mostrar_estudiante

#Variables pre-definidas 
lista_estudiantes = []
activo = True 

#Desarrollo
while activo:
    menu()
    opcion = leer_opcion()

    if opcion == 1 :
        añadir_estudiante(lista_estudiantes )
    elif opcion == 2 :
        buscar_estudiante(lista_estudiantes )
    elif opcion == 3 :
        eliminar_estudiante(lista_estudiantes )
    elif opcion == 4 :
        actualizar_estado(lista_estudiantes )
    elif opcion == 5 :
        mostrar_estudiante(lista_estudiantes )
    else:
        print("“Gracias por usar el sistema. Vuelva Pronto”")
        activo = False