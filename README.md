# Reto-6
__1__. Agrega las excepciones necesarias en los asignaciones de código del primer reto.


__2__. En el paquete Shape, identifica al menos los casos donde se necesitan excepciones (quizás al validar datos de entrada o procedimientos matemáticos), explícalos claramente usando comentarios y agrégalos al código.


------------------------------------------------------------------------------
# Prime punto
En este caso se deben cuenta los requisitos establecidos para la solución de estos 5 problemas:
<br>
1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

5. Escribir una función que reciba una lista de string y retorne únicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
----------------------------------------------------------------------------------

__Punto 1__: Tenermos 4 condiciones especiales:
- Solo hay 3 datos de entrada.
- Los dos primeros deben ser números.
- El ultimo dato debe ser uno de estos cuatro simbolos: ( '+', '-', '*', '/' )
- Solo hay una restricción al operar y es dividir por cero.

``` Python
def operacion(entrada):
    if entrada[2].strip() == '+':
        return f"El resultado de la suma es: {float(entrada[0].strip()) + float(entrada[1].strip())}"
    elif entrada[2].strip() == '-':
        return f"El resultado de la resta es: {float(entrada[0].strip()) - float(entrada[1].strip())}"
    elif entrada[2].strip() == '*':
        return f"El resultado de la multiplicación es: {float(entrada[0].strip()) * float(entrada[1].strip())}"
    elif entrada[2].strip() == '/':
        return f"El resultado de la división es: {float(entrada[0].strip()) / float(entrada[1].strip())}"

try:
    entrada = input("Ingrese sus dos valores a operar y el símbolo de la operación, separados por comas: ").split(',')
    
    if len(entrada) != 3:       # Sólo se pueden solicitar 3 datos segun el problema.
        raise ValueError("Error: solo puede ingresar dos valores y un símbolo de operación separados por comas.")
    
    if entrada[2].strip() not in ['+', '-', '*', '/']:      # Sólo hay 4 operaciones permitidas.
        raise ValueError("Error: Símbolo de operación no válido. Use '+', '-', '*', o '/'.")

    resultado = operacion(entrada) 
    print(resultado) # En caso de no tener ningun problema, se ejecuta la función.

except ValueError as e:
    print(f"Error: {e}") # En caso de ocurrir otro error no previsto. 

except ZeroDivisionError:
    print("Error: División por cero") # La división por cero es un tipo particular de error.
```
-----------------------------------------------------------------------------------
__Punto 2__: No tenemos una condición especial, pero podemos crear una: 
- Solo se pueden ingresar letras.
``` Python
def palindromo(entrada):
    entrada = entrada.lower()
    x = -1
    for i in range(len(entrada) // 2):
        if entrada[i] != entrada[x]:
            return f"{entrada} No es palíndromo"
        x -= 1
    return f"{entrada} sí es un palíndromo"

def tipo_caracter(entrada):        # Para este punto en particular con la necesidad de definir correctamente
    entrada = entrada.split(' ')       # la excepción especial se usa esta funíon para determinar si la entrada 
    for caracter in entrada:           # del usuario contiene solo letras; ya que el problema dice "palabras".
        if not caracter.isalpha():
            return True
    return False

try:
    entrada = input("Ingrese su palabra a analizar: ")
    if tipo_caracter(entrada):                 # El usuario solo puede ingresar letras.
        raise ValueError("Ingrese solo letras")

    resultado = palindromo(entrada) # En caso de no tener ningun problema, se ejecuta la función principal.

except ValueError as error:  # En caso de ocurrir otro error no previsto.
    print(f"Error: {error}")
```
----------------------------------------------------------------------
__Punto 3__: Tenemos 1 condición especial: 
- Solo se pueden ingresar números enteros.
``` Python
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
```
---------------------------------------------------------------
__Punto 4__: Tenemos 1 condición especial:
- Solo se puden ingresar números enteros.
``` Python
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
```
---------------------------------------------------------------
__Punto 5__: No hay ninguna condición especial, ya que el usuario puede ingresar cualquier tipo de caracter:
``` Python
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
```
---------------------------------------------------------------------------
# Segundo Punto
En este segundo punto debemos tener en cuenta los dos casos del paqute Shape:

---------------------------------------------------------------------------
__Caso 1__:

