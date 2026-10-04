def validar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número.")

def validar_divisior(num,mensaje):
    while num == 0:
        num = validar_numero(mensaje)
    return num