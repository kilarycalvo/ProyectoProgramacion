usuario = ["", "", "", "", "", 0]  
factura = ["", "", "", "", "", "", "", ""]  
paquete = ["", "", "", "", "", "", "Creado"]
guias = []

def registrar_usuario():
    usuario[0] = input("Ingrese el correo electrónico: ")
    usuario[1] = input("Ingrese el nombre del comercio: ")
    usuario[2] = input("Ingrese el teléfono del comercio: ")
    usuario[3] = input("Ingrese el nombre del dueño: ")
    usuario[4] = input("Ingrese la ubicación del local: ")
    usuario[5] += 1  
    print("Cuenta de usuario registrada exitosamente.")


def mostrar_info_usuario():
    print("Información del usuario:")
    print("Correo electrónico:", usuario[0])
    print("Nombre del comercio:", usuario[1])
    print("Teléfono del comercio:", usuario[2])
    print("Nombre del dueño:", usuario[3])
    print("Ubicación del local:", usuario[4])
    print("Cantidad de envíos realizados:", usuario[5])


def registrar_factura():
    factura[0] = input("Ingrese el tipo de cédula: ")
    factura[1] = input("Ingrese el número de cédula: ")
    factura[2] = input("Ingrese el nombre registrado: ")
    factura[3] = input("Ingrese el teléfono: ")
    factura[4] = input("Ingrese el correo: ")
    factura[5] = input("Ingrese la provincia: ")
    factura[6] = input("Ingrese el cantón: ")
    factura[7] = input("Ingrese el distrito: ")
    print("Factura electrónica registrada exitosamente.")


def mostrar_info_factura():
    print("Información de la factura electrónica:")
    print("Tipo de cédula:", factura[0])
    print("Número de cédula:", factura[1])
    print("Nombre registrado:", factura[2])
    print("Teléfono:", factura[3])
    print("Correo:", factura[4])
    print("Provincia:", factura[5])
    print("Cantón:", factura[6])
    print("Distrito:", factura[7])


def crear_paquete():
    global guias
    paquete[0] = input("Ingrese el nombre del destinatario: ")
    paquete[1] = input("Ingrese el teléfono del destinatario: ")
    paquete[2] = input("Ingrese el número de cédula del destinatario: ")
    paquete[3] = input("Ingrese el peso del paquete en kilogramos: ")
    paquete[4] = input("¿Habrá cobro contra entrega? (1: Si, 2: No): ") == "1"
    if paquete[4]:
        paquete[5] = input("Ingrese el monto a cobrar (en colones): ")
    paquete[6] = "Creado"
    numero_guia = input("Ingrese el número de guía único para el paquete: ")
    guia = paquete[:6] + [numero_guia]  
    guias += [guia]
    print("Paquete creado exitosamente.")


def mostrar_info_paquete():
    print("Información del paquete:")
    print("Destinatario:", paquete[0])
    print("Teléfono del destinatario:", paquete[1])
    print("Número de cédula del destinatario:", paquete[2])
    print("Peso del paquete en kilogramos:", paquete[3])
    print("Requiere cobro contra entrega:", "Sí" if paquete[4] else "No")
    if paquete[4]:
        print("Monto a cobrar:", paquete[5])
    print("Estado del paquete:", paquete[6])


def cambiar_estado_paquete():
    numero_guia = input("Ingrese el número de guía del paquete: ")
    encontrado = False
    for guia in guias:
        if guia[6] == numero_guia:
            estado = input("Ingrese el nuevo estado del paquete (1: Recolectado, 2: Entrega Fallida, 3: Entregado): ")
            if estado == "1":
                guia[6] = "Recolectado"
                paquete[6] = "Recolectado"  
                encontrado = True
            elif estado == "2":
                guia[6] = "Entrega Fallida"
                paquete[6] = "Entrega Fallida"  
                encontrado = True
            elif estado == "3":
                guia[6] = "Entregado"
                paquete[6] = "Entregado"  
                encontrado = True
            else:
                print("Opción no válida.")
            if encontrado:
                print("Estado del paquete actualizado exitosamente.")
            break
    if not encontrado:
        print("Número de guía no encontrado.")


def rastrear_paquete():
    numero_guia = input("Ingrese el número de guía del paquete: ")
    encontrado = False
    for guia in guias:
        if guia[6] == numero_guia:
            print("Estado del paquete:", guia[6])
            encontrado = True
            break
    if not encontrado:
        print("Número de guía no encontrado.")


def modulo_estadisticas():
    print("Cantidad de envíos realizados:", usuario[5])
    print("Lista de paquetes enviados:")
    for guia in guias:
        print("Número de guía:", guia[6], "- Estado:", guia[6])
    monto_total_cobrado = sum(float(guia[5]) for guia in guias if guia[5])  
    print("Monto total cobrado:", monto_total_cobrado)
    cantidad_por_telefono = {}
    cantidad_por_cedula = {}
    for guia in guias:
        telefono = guia[1]
        cedula = guia[2]
        cantidad_por_telefono[telefono] = cantidad_por_telefono.get(telefono, 0) + 1
        cantidad_por_cedula[cedula] = cantidad_por_cedula.get(cedula, 0) + 1
    print("Cantidad de paquetes por número de teléfono:")
    for telefono, cantidad in cantidad_por_telefono.items():
        print("Teléfono:", telefono, "- Cantidad de paquetes:", cantidad)
    print("Cantidad de paquetes por número de cédula:")
    for cedula, cantidad in cantidad_por_cedula.items():
        print("Cédula:", cedula, "- Cantidad de paquetes:", cantidad)


while True:
    print("1. Registrar cuenta de usuario")
    print("2. Registrar factura electrónica")
    print("3. Crear paquete")
    print("4. Mostrar información de usuario")
    print("5. Mostrar información de factura")
    print("6. Mostrar información de paquete")
    print("7. Cambiar estado de paquete")
    print("8. Rastrear paquete")
    print("9. Módulo de estadísticas")
    print("10. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        registrar_factura()
    elif opcion == "3":
        crear_paquete()
    elif opcion == "4":
        mostrar_info_usuario()
    elif opcion == "5":
        mostrar_info_factura()
    elif opcion == "6":
        mostrar_info_paquete()
    elif opcion == "7":
        cambiar_estado_paquete()
    elif opcion == "8":
        rastrear_paquete()
    elif opcion == "9":
        modulo_estadisticas()
    elif opcion == "10":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
