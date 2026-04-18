def gestor_tareas():
    tareas = []

    while True:
        print("\n=== Gestor de Tareas ===") # prueba de commit
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            tareas.append(tarea)
            print("Tarea agregada correctamente.")

        elif opcion == "2":
            if not tareas:
                print("No hay tareas registradas.")
            else:
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")

        elif opcion == "3":
            try:
                num = int(input("Ingrese el número de la tarea a eliminar: "))
                eliminada = tareas.pop(num - 1)
                print(f"Tarea '{eliminada}' eliminada.")
            except (ValueError, IndexError):
                print("Número inválido.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

gestor_tareas()