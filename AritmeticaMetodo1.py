import csv
from itertools import product
def ingresar_caracteres():
    cantidad_caracteres = int(input("Ingresa la cantidad de caracteres diferentes: "))
    caracteres = {}
    for i in range(0,cantidad_caracteres):
        caracter = input(f"Ingresa el caracter {i+1}: ")
        frecuencia = 2
        while(frecuencia<0 or frecuencia>1):
            frecuencia = float(input(f"Ingresa la frecuencia del caracter {caracter}: "))
            if(frecuencia<0 or frecuencia>1):
                print("La frecuencia debe estar entre 0 y 1")
        caracteres[caracter] = frecuencia
    return caracteres

def generar_combinaciones(cadena, espacios):
    combinaciones = [''.join(p) for p in product(cadena, repeat=espacios)]
    return combinaciones

def fraccionDiadicaMetodo1(l,alfa,beta):
    t = 1
    t_calculo = pow(0.5,t)
    while t_calculo>l:
        t+=1
        t_calculo = pow(0.5,t)
    dosT = pow(2,-t)
    dosMenosT = pow(2,-t+1)
    if (dosT<=l and l<dosMenosT):
        desigualdadMenor = alfa * (pow(2,t))
        desigualdadMayor = beta * (pow(2,t))
        if(desigualdadMenor%2==0):
            x = desigualdadMenor
        else:
            x = desigualdadMayor
        codificacion = expansionBinaria(x, t)  
    elif dosT<=l:
        x = alfa * (pow(2,t))
        codificacion = expansionBinaria(x, t)  
    elif l<dosMenosT:
        x = beta*(pow(2,t))
        codificacion = expansionBinaria(x, t)  
    else: 
        codificacion = "Error"
    return codificacion

def expansionBinaria(x,t):
    r = x/(pow(2,t))
    calculo = (r*2)
    calculo_anterior = r*2+1
    codificacion = "["
    while calculo!=calculo_anterior:
        calculo_anterior = calculo
        if calculo>=1:
            codificacion = codificacion + "1"
            calculo = (calculo-1)*2
        else:
            codificacion = codificacion + "0"
            calculo*=2
    codificacion = codificacion + "]"
    return codificacion
    
caracteres = ingresar_caracteres()
claves = caracteres.keys()
string_caracteres = ''.join(claves)
if(sum(caracteres.values())==1):
    datos = []
    print("Generado codificaciones....")
    for i in range(1,len(string_caracteres)+1):
        combinaciones_nivel = generar_combinaciones(string_caracteres, i)
        beta = 0
        alfa = 0
        valores_combinacion = []
        #print(f"Nivel {i}")
        for combinacion in combinaciones_nivel:
            l = 1
            for c in combinacion:
                l = l * caracteres[c]
            alfa = beta 
            beta = alfa + l
            codificacion = fraccionDiadicaMetodo1(l, alfa, beta)
            com = [(combinacion, l, alfa, beta, codificacion)]
            valores_combinacion.append(com)
            #print(com)
        nivel = [(i,valores_combinacion)]
        datos.append(nivel)
    print("Generado archivo csv....")
    try:
        with open('AritmeticaMetodo1.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for dato in datos:  
                writer.writerow([ '', 'Longitud', 'Alfa', 'Beta', 'Codificacion'])
                writer.writerow([f"Nivel {dato[0][0]}", "", ""])
                for c in dato[0][1]:
                    writer.writerow([c[0][0],c[0][1],c[0][2],c[0][3],c[0][4]])
                writer.writerow([''])
        print("Archivo generado con exito")
    except Exception as e:
        print("Error al generar archivo csv")
        
else:
    print("La suma de las frecuencias debe de ser 1")