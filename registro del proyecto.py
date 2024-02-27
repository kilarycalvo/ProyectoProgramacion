
class Usuario:
    def __init__(self, correo, nombre_comercio, telefono, nombre_dueno, ubicacion):
        self.correo = correo
        self.nombre_comercio = nombre_comercio
        self.telefono = telefono
        self.nombre_dueno = nombre_dueno
        self.ubicacion = ubicacion

def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    nombre_comercio = input("Ingrese el nombre del comercio: ")
    telefono = input("Ingrese el teléfono del comercio: ")
    nombre_dueno = input("Ingrese su nombre: ")
    ubicacion = input("Ingrese la ubicación de su local: ")

    usuario = Usuario(correo, nombre_comercio, telefono, nombre_dueno, ubicacion)

    print("\n¡Usuario registrado exitosamente!\n")
    print("Detalles de la cuenta:")
    print("Correo electrónico:", usuario.correo)
    print("Nombre del comercio:", usuario.nombre_comercio)
    print("Teléfono del comercio:", usuario.telefono)
    print("Nombre del dueño:", usuario.nombre_dueno)
    print("Ubicación del local:", usuario.ubicacion)

# Ejecutar el programa
registrar_usuario()
