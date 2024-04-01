num_guia = input("Ingrese el número de guía: ")
nombre_comercio = input("Ingrese el nombre del comercio: ")
telefono_comercio = input("Ingrese el teléfono del comercio: ")
nombre_destinatario = input("Ingrese el nombre del destinatario: ")
telefono_destinatario = input("Ingrese el teléfono del destinatario: ")
requiere_cobro = input("¿Requiere cobro? (1: sí / 2: no): ")

if requiere_cobro == '1':
    requiere_cobro = True
    monto_cobro = float(input("Ingrese el monto a cobrar: "))
else:
    requiere_cobro = False
    monto_cobro = 0

print("Guía de Envío")
print("Número de Guía:", num_guia)
print("Información de Comercio:")
print("Nombre:", nombre_comercio)
print("Teléfono:", telefono_comercio)
print("Información del Destinatario:")
print("Nombre:", nombre_destinatario)
print("Teléfono:", telefono_destinatario)
if requiere_cobro:
    print("Requiere Cobro")
    print("Monto a Cobrar:", monto_cobro)
else:
    print("No requiere cobro")
