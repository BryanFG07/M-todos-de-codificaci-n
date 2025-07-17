#Problema 1 
import csv
def combinaciones(posicion, conjunto):
    if posicion == 0:
        return [[]]  
    else:
        combinaciones_previas = combinaciones(posicion - 1, conjunto)
        nuevas_combinaciones = []
        for c in combinaciones_previas:
            for elemento in conjunto:
                nuevas_combinaciones.append(c + [elemento])
        return nuevas_combinaciones

A = {'0', '1'}
B = {'0', '1', '*'}
iteraciones = 5
with open('Problema1_canal_discreto.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Escribir la cabecera del CSV
    writer.writerow([ 'Combinaciones A', 'Numero de A', 'Combinaciones B', 'Numero de B'])
    for posicion in range(1, iteraciones+1):  # 1 lugar, 2 lugares, 3 lugares
        combinaciones_A = combinaciones(posicion, A)
        combinaciones_B = combinaciones(posicion, B)
        '''print(f'*********************l: {posicion}*********************')
        print('A:', combinaciones_A)
        print('nA: ',str(len(combinaciones_A)) )
        print('', combinaciones_B)
        print('nB: ',str(len(combinaciones_B)) )
        print()'''
        writer.writerow([combinaciones_A, len(combinaciones_A), combinaciones_B, len(combinaciones_B)])



