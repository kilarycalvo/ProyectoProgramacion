class EstadisticasEnvios:
    def __init__(self):
        self.cantidad_envios = 0
        self.lista_paquetes = []
        self.monto_total_cobrado = 0
        self.paquetes_por_telefono = {}
        self.paquetes_por_cedula = {}

    def agregar_envio(self, paquete):
        self.cantidad_envios += 1
        self.lista_paquetes.append(paquete)

        # Actualizar estadísticas por teléfono
        if paquete.telefono in self.paquetes_por_telefono:
            self.paquetes_por_telefono[paquete.telefono] += 1
        else:
            self.paquetes_por_telefono[paquete.telefono] = 1

        # Actualizar estadísticas por cédula
        if paquete.cedula in self.paquetes_por_cedula:
            self.paquetes_por_cedula[paquete.cedula] += 1
        else:
            self.paquetes_por_cedula[paquete.cedula] = 1

        # Actualizar monto total cobrado
        self.monto_total_cobrado += paquete.monto

    def mostrar_estadisticas_generales(self):
        print("Estadísticas generales:")
        print("Cantidad total de envíos:", self.cantidad_envios)
        print("Monto total cobrado:", self.monto_total_cobrado)

    def mostrar_estadisticas_por_telefono(self):
        print("Estadísticas por número de teléfono:")
        for telefono, cantidad in self.paquetes_por_telefono.items():
            print("Teléfono:", telefono, "- Cantidad de paquetes enviados:", cantidad)

    def mostrar_estadisticas_por_cedula(self):
        print("Estadísticas por número de cédula:")
        for cedula, cantidad in self.paquetes_por_cedula.items():
            print("Cédula:", cedula, "- Cantidad de paquetes enviados:", cantidad)


class Paquete:
    def __init__(self, telefono, cedula, monto):
        self.telefono = telefono
        self.cedula = cedula
        self.monto = monto


def main():
    estadisticas = EstadisticasEnvios()

    while True:
        print("\nMenú:")
        print("1. Registrar envío de paquete")
        print("2. Mostrar estadísticas generales")
        print("3. Mostrar estadísticas por número de teléfono")
        print("4. Mostrar estadísticas por número de cédula")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            telefono = input("Ingrese el número de teléfono del destinatario: ")
            cedula = input("Ingrese el número de cédula del destinatario: ")
            monto = float(input("Ingrese el monto de cobro: "))
            paquete = Paquete(telefono, cedula, monto)
            estadisticas.agregar_envio(paquete)
            print("Envío registrado exitosamente.")

        elif opcion == "2":
            estadisticas.mostrar_estadisticas_generales()

        elif opcion == "3":
            estadisticas.mostrar_estadisticas_por_telefono()

        elif opcion == "4":
            estadisticas.mostrar_estadisticas_por_cedula()

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
