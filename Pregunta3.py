def clave_es_valida(clave):
    contador = 0#ayudara para saber en que posicion estoy
    digito_centena = 0
    digito_millar = 0
    
    #La variable clave es un texto, cadena, string
    #string, no se puede realizar operaciones matematicas
    #sumar,restar, dividir, etc
    
    longitud = len(clave)
    #longitud = 7
    
    for caracter in clave:
        contador += 1
        posicion_derecha = longitud - contador + 1
        # 7 - 1 + 1 = 7  => el carcter es 1
        # 7 - 2 + 1 = 6  => el carcter es 2
        # 7 - 3 + 1 = 5  => el carcter es 3
        # 7 - 4 + 1 = 4  => el carcter es 4
        # 7 - 5 + 1 = 3  => el carcter es 4
        # 7 - 6 + 1 = 2  => el carcter es 7
        # 7 - 7 + 1 = 1  => el carcter es 8
        
        if posicion_derecha == 3:
            digito_centena = int(caracter)
        elif posicion_derecha == 4:
            digito_millar = int(caracter)
    
    suma = digito_centena + digito_millar
    
    print("digito_centena: ", digito_centena)
    print("digito_millar: ", digito_millar)
    print("Suma: ", suma)
    
    if suma % 2 == 0:#la suma es numero par?
        print("La clave es correcta")
    else:
        print("La clave es incorrecta (La suma no es par)")

def main():
    clave = input("Ingresar clave: ")
    
    numero_de_digitos = len(clave)
    
    if numero_de_digitos<4:
        print("La clave es invalida (menos de 4 digitos)")
    else:
        clave_es_valida(clave)
    
main()

