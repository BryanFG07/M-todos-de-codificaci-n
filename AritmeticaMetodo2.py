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

def fraccionDiadicaMetodo2(alfa_original,beta_original):
    alfa, codificacion_alfa = expansionBinaria(alfa_original)
    beta, codificacion_beta = expansionBinaria(beta_original)
    codificacion = []
    alfa_actual = alfa
    while codificacion_alfa == codificacion_beta:
        alfa, codificacion_alfa = expansionBinaria(alfa)
        beta, codificacion_beta = expansionBinaria(beta)
        #print (f"Alfa {alfa} Beta {beta}")
        #print(f"{codificacion_alfa}, {codificacion_beta}")
        if codificacion_alfa == codificacion_beta:
            codificacion.append(codificacion_alfa)    
            alfa_actual = alfa
    if codificacion_alfa==1:
        #exepcion 1
        alfa_anterior = alfa 
        alfa, codificacion_alfa = expansionBinaria(alfa)
        if alfa_anterior == alfa:
            codificacion.append(codificacion_alfa)
    else:
        #expepcion 2
        existe_uno = False
        alfa_ac=alfa
        while alfa>0 and existe_uno==False:
            alfa, codificacion_alfa = expansionBinaria(alfa)
            #print(alfa)
            if codificacion_alfa==1:
                existe_uno = True
        #print(existe_uno)
        #print(codificacion)
        #en dado caso que si se cumpla la ocndicion del la expecion 2
        if existe_uno:
            a, c = expansionBinaria(alfa_actual)
            codificacion.append(c)
            alfa, codificacion_alfa = expansionBinaria(alfa_ac)
            codificacion.append(codificacion_alfa)
            while codificacion_alfa==0:
                alfa, codificacion_alfa = expansionBinaria(alfa_actual)
                if(codificacion!=0):
                    codificacion.append(codificacion_alfa)
            codificacion.append(1)
        if len(codificacion)==0:
            alfa, codificacion_alfa = expansionBinaria(alfa_original)
            codificacion.append(codificacion_alfa)

    return codificacion

def expansionBinaria(r):
    if r>=1:
        codificacion = 1
        r = (r-1)*2
    else:
        codificacion = 0
        r*=2
    return r, codificacion

    
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
            codificacion = fraccionDiadicaMetodo2(alfa, beta)
            com = [(combinacion, l, alfa, beta, codificacion)]
            print(com)
            valores_combinacion.append(com)
        nivel = [(i,valores_combinacion)]
        datos.append(nivel)
    print("Generado archivo csv....")
    try:
        with open('AritmeticaMetodo2.csv', mode='w', newline='', encoding='utf-8') as file:
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