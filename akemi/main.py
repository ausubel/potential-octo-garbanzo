"""
Descripción: Escribe un programa que solicite al usuario una temperatura en grados Celsius y conviértela a grados Fahrenheit. Luego, muestra el resultado.

Pistas:
Fórmula de conversión: °F = (°C × 9/5) + 32
Usa la función input() para leer datos del usuario y float() para convertir la entrada a un número decimal.
"""

def run():
    print('Hello Akemi from main')

    while True:
        try:
            celsius = float(input('Ingresa la temperatura en grados Celsius: '))
            break
        except ValueError:
            print('Debes ingresar un número.')
            
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.')



if __name__=='__main__':
    run()