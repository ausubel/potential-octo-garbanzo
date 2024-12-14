"""
Descripción: Pide al usuario que ingrese una cadena de texto y determina cuántas vocales (a, e, i, o, u) contiene. Muestra el número total de vocales encontradas.
Pistas:

Puedes convertir la cadena a minúsculas con .lower().
Itera sobre cada carácter y comprueba si es una vocal.
Incrementa un contador para cada vocal encontrada.
"""
def contar_vocales():
    lista = ['a', 'e', 'i', 'o', 'u']
    nombre = input("Ingrese una cadena de texto porfavor: ").lower()
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for i in nombre:
        if i == lista[0]:
            contador_a += 1
        elif i == lista[1]:
            contador_e += 1
        elif i == lista[2]:
            contador_i += 1
        elif i == lista[3]:
            contador_o += 1
        elif i == lista[4]:
            contador_u += 1
        else:
            pass
    
    print("Estas son la cantidad de vocales encontradas")
    print(f'vocal "a": {contador_a}')
    print(f'vocal "e": {contador_e}')
    print(f'vocal "i": {contador_i}')
    print(f'vocal "o": {contador_o}')
    print(f'vocal "u": {contador_u}')
    print(f'vocales totales: {contador_a + contador_e + contador_i + contador_o + contador_u}')

if __name__=='__main__':
    contar_vocales()