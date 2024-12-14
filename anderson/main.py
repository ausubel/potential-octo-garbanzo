"""
Descripción: Dada una lista de elementos (por ejemplo, [1, 2, 3, 4]), crea un programa que la invierta sin usar la función reverse() ni la sintaxis [::-1] incorporadas.
Pistas:

Puedes crear una lista nueva e ir agregando los elementos desde el final de la lista original hasta el inicio.
Usa un bucle for o while para recorrer la lista.

"""
def run():
    print("Hello Anderson")
    def investir_lista(lista):
        lista_invertida = []
        for elemento in lista:
            lista_invertida.insert(0, elemento)
        return lista_invertida

    lista_pedida = [1,2,3,4]
    lista_pedida_invertida = investir_lista(lista_pedida)
    print("Lista original: ", lista_pedida)
    print("Lista invertida: ", lista_pedida_invertida)

if __name__=='__main__':
    run()