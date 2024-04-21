def mismos_caracteres(a):

    x = []
    for i in range(len(a)):
        conjunto_palabra = set(a[i])
        for j in range(i + 1, len(a)):
            conjunto_comparar = set(a[j])
            if conjunto_palabra == conjunto_comparar and a[j] not in x:
                x.append(a[i])
                x.append(a[j])

    return f"Las palabras con los mismos caracteres son: {set(x)}"

try:
    a = [palabra.strip() for palabra in input("Ingrese sus palabras separadas por comas: ").split(',')]
    print(mismos_caracteres(a))     # En caso de no tener ningun problema, se ejecuta la función.

except ValueError as error:
    print(error)                # El problema habla de caracteres en general (strings), por lo que el usuario 
                                    # no debería causar un error con su entrada, igual en caso de algo se presenta cualquier error inprevisto.