def suma_mayor(entrada):
    
    a = sorted(entrada)
    x = -1
    for i in range(len(a) - 1):
        if a[x] - a[x-1] == 1:
            return f"Los dos elementos de mayor valor consecutivo son: {a[x]} y {a[x-1]} y su suma es: {a[x] + a[x-1]}"
        elif a[x] - a[x-1] == -1:
            return f"Los dos elementos de mayor valor consecutivo son: {a[x]} y {a[x-1]} y su suma es: {a[x] + a[x-1]}"
        x -= 1
    return "No existen dichos elementos"

try:
    entrada = input("Ingrese sus números separados por coma: ").split(',')
    entrada = [int(num) for num in entrada]     # convierte los datos entregados a enteros, si es posible.
    suma = suma_mayor(entrada)
    print(suma)     # En caso de no tener ningun problema, se ejecuta la función.

except ValueError as error:                         # En este caso el unico error posible generado por la
    print("Error: ingrese solo números enteros")        # entrada del usuario es ingresar un número no entero.