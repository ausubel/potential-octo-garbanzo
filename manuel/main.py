"""
Descripción: Solicita un número entero positivo n y calcula la suma de todos los enteros desde 1 hasta n. Muestra el resultado.
Pistas:

Puedes usar un bucle for o la función sum() con range().
Por ejemplo, si el usuario ingresa 5, la salida debería ser 1+2+3+4+5 = 15.
"""
def run():
    # Comentario cualquiera para hacer la rama.
    while True:
        try:
            entero = int(input("Ingrese un entero positivo: "))
            if entero > 0:
                print("Número ingresado correctamente.")
                break
            else:
                print("Entero no positivo, intente nuevamente.")
        except:
            print("Error al ingresar el número. Intente nuevamente.")

    # Inicio de la suma
    suma = sum(range(entero + 1))

    # Resultado
    print(f"Se ha ingresado el número {entero} y la suma del 1 hasta dicho número es {suma}.")

if __name__=='__main__':
    run()
