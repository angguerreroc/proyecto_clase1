def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

stock = 120
prestamos_activos = 0
total_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Libros disponibles actualmente: {stock}")

    elif opcion == "2":
        try:
            cantidad = int(input("Ingrese cantidad de libros a prestar: "))
            if cantidad <= 0:
                print("Cantidad inválida. Debe ser mayor a 0.")
            elif cantidad > stock:
                print("No hay suficientes libros disponibles.")
            else:
                stock -= cantidad
                prestamos_activos += cantidad
                total_prestamos += cantidad
                print(f"Préstamo realizado con éxito. Libros restantes: {stock}")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    elif opcion == "3":
        try:
            cantidad = int(input("Ingrese cantidad de libros a devolver: "))
            if cantidad <= 0:
                print("Cantidad inválida. Debe ser mayor a 0.")
            elif stock + cantidad > 120:
                print("No se puede superar la capacidad máxima de 120 libros.")
            else:
                stock += cantidad
                prestamos_activos -= cantidad
                print(f"Devolución registrada. Libros disponibles: {stock}")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    elif opcion == "4":
        print(f"Total de préstamos activos: {prestamos_activos}")
        print(f"Total de préstamos realizados en la sesión: {total_prestamos}")

    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
