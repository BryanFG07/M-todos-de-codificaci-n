def regla_mal_caracter(patron):
    desplazamiento_mal_caracter = {}
    longitud = len(patron)
    #Obtenemos los desplazamientos que podemos hacer para cada caracter por regla mal caracter
    for i in range(longitud - 1):
        desplazamiento_mal_caracter[patron[i]] = longitud - i - 1
    return desplazamiento_mal_caracter

def regla_buen_sufijo(patron):
    longitud = len(patron)
    desplazamiento_buen_sufijo = [0] * (longitud + 1)
    posicion_borde = [0] * (longitud + 1)
    #Obtener los dezplazamientos de la regla del buen sufijo
    i = longitud
    j = longitud + 1
    posicion_borde[i] = j
    while i > 0:
        while j <= longitud and patron[i - 1] != patron[j - 1]:
            if desplazamiento_buen_sufijo[j] == 0:
                desplazamiento_buen_sufijo[j] = j - i
            j = posicion_borde[j]
        i -= 1
        j -= 1
        posicion_borde[i] = j
    
    j = posicion_borde[0]
    for i in range(longitud + 1):
        if desplazamiento_buen_sufijo[i] == 0:
            desplazamiento_buen_sufijo[i] = j
        if i == j:
            j = posicion_borde[j]
    
    return desplazamiento_buen_sufijo



def boyer_moore(texto, patron):
    desplazamiento_mal_caracter = regla_mal_caracter(patron)
    desplazamiento_buen_sufijo = regla_buen_sufijo(patron)
    m = len(patron)
    n = len(texto)
    s = 0
    encontro = False
    while s <= n - m:
        j = m - 1
        #Compara el patron con la subcadena del texto
        while j >= 0 and patron[j] == texto[s + j]:
          j -= 1

        #Cuando j es menor a 0 significa que todo el patron coincidio
        if j < 0:
            print(f"Patrón encontrado en la posición {s + 1}")
            #Se recorre con el dezplamiento maximo del buen sufijo porque se encontro el patron completo
            s += desplazamiento_buen_sufijo[0]
            print(f"Se utiliza la regla del buen sufijo para saltar a la posición {s+1}")
            encontro = True
        else:
            #se establece verifica obtiene el mal caracter
            mal_caracter = texto[s + j]
            desplazamiento_mal_caracter_valor = desplazamiento_mal_caracter.get(mal_caracter, m)
            #Se verifica cual tiene mas dezplazamientos entre las dos reglas para desplazar esos espacios
            desplazamiento = max(desplazamiento_mal_caracter_valor, desplazamiento_buen_sufijo[j + 1])

            if desplazamiento_mal_caracter_valor >= desplazamiento_buen_sufijo[j + 1]:
                print(f"Se utiliza la regla del mal carácter para saltar a la posición {s + desplazamiento_mal_caracter_valor +1}")
            else:
                print(f"Se utiliza la regla del buen sufijo para saltar a la posición {s + desplazamiento_buen_sufijo[j + 1] + 1}")
            s += desplazamiento
    if encontro==False:
        print("No se encontró el patrón en el texto")


# Ingresar texto y patron
texto = "GCTTCTGCTACCTTTTGCGCGCGCGCGGAACCTTTTGCAD"
patron = "CCTTTTGC"
boyer_moore(texto, patron)

