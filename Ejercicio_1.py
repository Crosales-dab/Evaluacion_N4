#Importar
from funciones import menu, leer_opcion


#Variables pre-definidas 
lista_alumnos = []
activo = True 

#Desarrollo
while activo:
    menu()
    opcion = leer_opcion()

    if opcion == 1 :
        agregar_estudiante()
    elif opcion == 2 :
        buscar_estudiante()
    elif opcion == 3 :
        eliminar_estudiante()
    elif opcion == 4 :
        actualizar_estado()
    elif opcion == 5 :
        mostrar_estudiantes()
    else:
        print("“Gracias por usar el sistema. Vuelva Pronto”")
        activo = False