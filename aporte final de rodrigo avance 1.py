usuario = ()
factura = ()
paquete = ()

while True:
    print("1. Registrar cuenta de usuario")
    print("2. Registrar factura electrónica")
    print("3. Crear paquete")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        usuario = (
            input("Ingrese el correo electrónico: "),
            input("Ingrese el nombre del comercio: "),
            input("Ingrese el teléfono del comercio: "),
            input("Ingrese el nombre del dueño: "),
            input("Ingrese la ubicación del local: ")
        )
        print("Cuenta de usuario registrada exitosamente.")
    elif opcion == "2":
        factura = (
            input("Ingrese el tipo de cédula: "),
            input("Ingrese el número de cédula: "),
            input("Ingrese el nombre registrado: "),
            input("Ingrese el teléfono: "),
            input("Ingrese el correo: "),
            input("Ingrese la provincia: "),
            input("Ingrese el cantón: "),
            input("Ingrese el distrito: ")
        )
        print("Factura electrónica registrada exitosamente.")
    elif opcion == "3":
        paquete = (
            input("Ingrese el nombre del destinatario: "),
            input("Ingrese el teléfono del destinatario: "),
            input("Ingrese el número de cédula del destinatario: "),
            input("Ingrese el peso del paquete en kilogramos: "),
            input("¿Habrá cobro contra entrega? (1: Si, 2: No): "),
            int(input("Ingrese el monto a cobrar (en colones): ") if input("¿Habrá cobro contra entrega? (1: Si, 2: No): ") == "1" else 0)
        )
        print("Paquete creado exitosamente.")
    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

