#Rastreo de paquetes

# Simulamos el estado del paquete basado en el número de guía

def rastrear_paquete(numero_guia):
    estado_paquete = {
        "673290": "En tránsito",
        "349091": "Entregado",
        "789102": "En proceso de entrega",
        "234198": "No encontrado"
    }
    
# Verificamos si el número de guía está en la base de datos
    if numero_guia in estado_paquete:
        return estado_paquete[numero_guia]
    else:
        return "Número de guía no válido"


def inicio():
    while True:
# Solicitamos al usuario que ingrese el número de guía
        numero_guia = input("Ingrese su número de guía (o 'S' para salir): ")
        
# Verificamos si el usuario quiere salir del programa
        if numero_guia == 'S':
            print("¡Nos vemos pronto!")
            break
    
# Realizamos el rastreo del paquete
        estado = rastrear_paquete(numero_guia)
        print(f"Estado del paquete: {estado}")

# Llamamos a la función inicio para iniciar el programa
inicio()
