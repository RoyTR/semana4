def calcular_sueldo_final(sueldo_inicial, tipo_trabajador, anios_trabajo):
    #gerente= 14% anual, 18% cada 4 años
    #empleado= 8% anual, 12% cada 4 años
    #sueldo_final = sueldo_inicial
    
    for anio in range(1, anios_trabajo):
        #Determinar el porentaje segun tipo y si es multiplo de 4
        if tipo_trabajador == 'g':
            if anio % 4 == 0:
                porcentaje = 0.18
            else:
                porcentaje = 0.14
        elif tipo_trabajador == 'e':
            if anio % 4 == 0:
                porcentaje = 0.12
            else:
                porcentaje = 0.08
        
        #Aumentar el sueldo acumulativo
        sueldo_final = sueldo_final * (1 + porcentaje)
        #1000 | 18% => 0.18
        #1000* (1+0.18)
        #1000 * 1.18 = 1180
        
    return sueldo_final
    
def calcular_porcentaje_aumento(sueldo_inicial, sueldo_final):
    aumento = sueldo_final - sueldo_inicial
    porcentaje_aumento = (aumento/sueldo_inicial) * 100
    return porcentaje_aumento

def main():
    tipo_trabajador = input("Ingresar es es Gerente (g) o Empleado (e):")
    anios_trabajo = int(input("Ingresar los años de trabajo: "))
    sueldo_inicial = float(input("Ingresar el sueldo: "))
    
    sueldo_final = calcular_sueldo_final(sueldo_inicial, tipo_trabajador, anios_trabajo)
    porcentaje = calcular_porcentaje_aumento(sueldo_inicial, sueldo_final)
    
    print("Sueldo final: ", sueldo_final)
    print("Porcentaje de aumento: ", porcentaje)


main()

#1500
#1620
#1,749.6
