from funciones import funciones_aritmeticas as fa
from funciones import funciones_validacion as fv

def main():

    print("Operaciones aritméticas disponibles\n")
    print("Sumar (1)","Restar (2)", "Multiplicar (3)", "Dividir (4)", sep="\n", end="\n"*2)

    seleccionar_operacion = "Selecciona la operación aritmética que desees realizar (1,2,3,4): "
    seleccionar_num1 = "Introduce el primer número: "
    seleccionar_num2 = "Introduce el segundo número: "
    divisor_erroneo = "Divisor inválido. Introduce un divisor distinto de cero: "

    while True:
        try:
            operacion = fv.validar_numero(seleccionar_operacion)
            if operacion not in(1,2,3,4):
                raise ValueError("La operación seleccionada no existe")
            break
        except ValueError as e:
            print(f"Error: {e}")

    num_1 = fv.validar_numero(seleccionar_num1)
    num_2 = fv.validar_numero(seleccionar_num2)

    
    try:
        
        if operacion == 1:
            resultado = fa.sumar(num_1,num_2)
        elif operacion == 2:
            resultado = fa.restar(num_1,num_2)
        elif operacion == 3:
            resultado = fa.multiplicar(num_1,num_2)
        elif operacion == 4:
            num_2 = fv.validar_divisior(num_2,divisor_erroneo)
            resultado = fa.dividir(num_1,num_2)
                  
    except Exception as e:
        print(f"Error: {e}")
    else:
        
        print(f"El resultado de la operación es {resultado}")

if __name__ == "__main__":
    main()
