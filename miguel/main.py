"""
Descripción: Pide al usuario un número entero positivo y calcula su factorial. El factorial de n se define como n! = n × (n-1) × (n-2) × ... × 1. Por ejemplo, 5! = 120.
Pistas:

Si el usuario ingresa 0, el factorial es 1.
Usa un bucle for o while para multiplicar todos los números desde 1 hasta n.
"""
def run():
    numero_ingresado = int(input('Ingresa un número entero positivo: '))
    factorial = 1
    for i in range(1, numero_ingresado + 1):
        factorial *= i
    print(f'El factorial de {numero_ingresado} es {factorial}')



if __name__=='__main__':
    run()