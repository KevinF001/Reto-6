def primos(a):
    x = []
    for i in a:
        numero = int(i) # Combierte todos los datos de str a int, si es posible.
        if numero < 2:
            continue
        primo = True
        for j in range(2, int(numero**0.5) + 1):
            if (numero % j) == 0:
                primo = False
                break
        if primo:
            x.append(numero)
    return f"Los números primos son: {set(x)}"

try:
    entrada = input("Ingrese sus números enteros separados por coma: ").split(',')
    primos_encontrados = primos(entrada)
    print(primos_encontrados)   # En caso de no tener ningun problema, se ejecuta la función.

except ValueError as error:                         # El unico error posible generado por la entrada del usuario
    print("Error: ingrese solo números enteros")    # es el de no ingresar un número entero; en cuyo caso se activa este error general.

