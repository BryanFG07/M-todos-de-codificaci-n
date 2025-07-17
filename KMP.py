def funcion_prefijo(patron):
    m = len(patron)
    prefijo = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and patron[k] != patron[q]:
            k = prefijo[k - 1]
        if patron[k] == patron[q]:
            k += 1
        prefijo[q] = k
    return prefijo

def KMP(text, patron):
    n = len(text)
    m = len(patron)
    prefijo = funcion_prefijo(patron)
    q = 0  
    r = 0
    for i in range(n):
        while q > 0 and patron[q] != text[i]:
            q = prefijo[q - 1]
        if patron[q] == text[i]:
            q += 1
        if q == m:
            print(f"El patrón se encontró en la posición {i - m + 2}")
            q = prefijo[q - 1]
            r +=1
    if r==0:
        print("No se encontró en patrón en el texto")
    


text = "bacbababaabcbaababacabababaca"
patron = "ababaca"
print(text)
print(patron)
KMP(text, patron)
