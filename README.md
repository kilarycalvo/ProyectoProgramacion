# Registro de datos para una factura electrónica

# Inicializamos un diccionario vacío para almacenar los datos
factura = {}

# Solicitamos los datos al usuario
factura["Tipo de cédula"] = input("Tipo de cédula: ")
factura["Número de cédula"] = input("Número de cédula: ")
factura["Nombre registrado"] = input("Nombre registrado: ")
factura["Teléfono"] = input("Teléfono: ")
factura["Correo"] = input("Correo: ")
factura["Provincia"] = input("Provincia: ")
factura["Cantón"] = input("Cantón: ")
factura["Distrito"] = input("Distrito: ")

# Mostramos los datos registrados
print("\nDatos registrados para la factura electrónica:")
for campo, valor in factura.items():
    print(f"{campo}: {valor}")

