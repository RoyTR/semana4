def contar_cantidad_digitos(numero):
    numero_de_digitos = len(numero)
    print("El numero de digitos es", numero_de_digitos)
    
def contar_cantidad_numero_repetido(numero, numero_a_buscar):
    contador = 0
    
    for digito in numero:
        if numero_a_buscar == digito:
            #contador = contador + 1
            contador += 1
    
    print("El numero", numero_a_buscar, "se repite", contador, "veces")

def main():
    numero = input("Ingresar un numero: ")
    numero_a_buscar = input("Ingresar el numero a buscar: ")
    
    contar_cantidad_digitos(numero)
    contar_cantidad_numero_repetido(numero, numero_a_buscar)
    #print("Aca va el codigo")


main()

