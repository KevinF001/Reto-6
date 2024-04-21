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
En este segundo punto pese a haber dos casos las excepciones son las mismas en ambos casos, pues lo que cambia es solamente la estructura de los paquetes, por esto se puede solo cambiar uno:

---------------------------------------------------------------------------
__Caso 1__: 
```
Caso_1/
|
├── Paquete_Shape/
|      |
│      ├── __init__.py
│      └── ClassShape.py
└── main.py
```
-------------------------------------------------------------------------------------
- __Restrigción de poliformismo:__

  
  Esta restrigción va interna en el codigo y garantiza que las clases hijas de Shape ejecuten todos los metodos de esta.


  ``` Python
    def get_vertices(self):
        return self.vertices
                               
    def compute_perimeter(self):                                                      # Esto garantiza que el programa ejecutra estos metodos
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")    # en las clases hijas de Shape

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_angles(self):
        raise NotImplementedError("Subclases deben implementar compute_angles()")
    def regular (self):
        raise NotImplementedError("Subclases deben implementar compute_angles()")

  ```
  -------------------------------------------------------------------------------------
- __Restrigción de opciones de ménu:__

  
  En el codigo se le da la opción al usuario entre escoger entre crear un tetraedro, triángulo o salir del programa; para esto se dan opciones numericas, para escoger entre las figuras se da la cantidad de vertices de
  estas 3 o 4, en caso de querer salir se preciona 1 y en caso de que el usuario no ingrese una opción valida se retorna el error de opción no valida.

  
  ``` Python
    while True:
        x = int(input("Ingrese la cantidad de cordenadas de su figura (vertices);, si desea salir selecione 1: \n ")) 
        if x == 4:
            fo.initialize_shape(x) 
            ...

        elif x == 3:  
            fo.initialize_shape(x)
            ...

        elif x == 1:  
            break

        else:    
            raise ValueError("Opción no válida") # Retorna un error si el usuario no ingresa una opción valida.
  ```
---------------------------------------------------------------------------------------------
- __Restrigción en la entrada de cordenadas del usuario:__

  
  Dependiendo del tipo de figura que el usuario escoja podra empezar a operar con estas; el si estas tienen o no sentido en la figuras permitidas de momento no importa, lo importante es garantizar de primera mano que las
  cordenadas son dos números separados por una coma y ya.

   ``` Python
    def initialize_shape(self, x):  
        if x == 4:
            self.vertices = []  
            for n in range(1, 5): 
                while True:
                    try:
                        c = ([float(coordinate) for coordinate in input(f"Ingrese la cordenada {n}: ").split(',')])
                        punto = Point(c[0], c[1])
                        x_nu, y_nu = punto.get_coordinates()   # Esta estrucutra se encarga de analizar si las cordenadas son validas
                        self.vertices.append((x_nu, y_nu))          # en caso de que no retorna un error y permite intentarlo de nuevo.
                        break  
                    except ValueError:
                        print("Error: Ingrese coordenadas numéricas.")

        elif x == 3:
            self.vertices = []
            for n in range(1, 4): 
                while True:
                    try:
                        c = ([float(coordinate) for coordinate in input(f"Ingrese la cordenada {n}: ").split(',')])
                        punto = Point(c[0], c[1])
                        x_nu, y_nu = punto.get_coordinates()
                        self.vertices.append((x_nu, y_nu))
                        break  
                    except ValueError:
                        print("Error: Ingrese coordenadas numéricas.")

   ```
------------------------------------------------------------------------------------------------------
- __Restrigción en la validez de las cordenadas__:


  El programa solo es capaz de calcular rectangulos y cuadrados por el lado de los tetraedros y todos los tipos de triángulos; pero no siempre se formaran estas figuras, por lo que deben haber garantias de la validez de    estas, por parte de los
  tetraedros tenemos 3 dependiendo de la figura:

  
    -----------------------------------------------------------------------------------------------------

  a. En el caso de los rectangulos y cuadrados se deben cumplir tres cosas:
     - Tener sus lados opuestos iguales (rectangulo), tener todos sus lados iguales (cuadrado).
     - Tener todos sus ángulos internos de 90°.
     - Tener sus dos diagonales iguales.

     Es en esta ultima condición es donde esta la clave, el analizar si todos los lados son iguales o son iguales los opuestos se hace al calular la longitud de las lineas que conforman a las figuras; pero en el caso de
     los ángulos internos hay un  problema y es que no siempre se garantiza que una figura de 4 lados iguales sea un cuadrado o una de lados opuestos, un rectangulo, por lo que para verificar esto y confirmar al 100% la
     validez de la figura, se analiza si las dos diagonales son iguales, si lo son quiere decir que todos los ángulos son de 90°. En caso de no cumplirse estos criterios el programa retorna un error.


     ``` Python
     if x == 4:
            fo.initialize_shape(x) 
            vertices = fo.get_vertices() 
            sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
            rectangulo = Rectangle()

            if sum(sides)/4 == sides[0]: 
                cu = Square()
                diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
                diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
                if diagonal_1 != diagonal_2:
                    raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

                print(f"\n La figura corresponde a un cuadrado de lados {sides[0]} con vertices en las cordenadas: {fo.get_vertices()} ")
                print(f"   Su perimetro es de: {cu.compute_perimeter()} y su área de {cu.compute_area()}")
                print(f"   Es una figura {cu.regular()}  y sus angulos internos son: {cu.compute_angles()} \n")

            elif sides[0] == sides[2] and sides[1] == sides[3]:
                diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
                diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
                if diagonal_1 != diagonal_2:
                    raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

                print(f"\n La figura corresponde a un rectangulo de lados {sides[0]} x {sides[1]} con vertices en las cordenadas: {fo.get_vertices()} ")
                print(f"   Su perimetro es de: {rectangulo.compute_perimeter()} y su área de: {rectangulo.compute_area()}")
                print(f"   Es una figura {rectangulo.regular()}  y sus angulos internos son: {rectangulo.compute_angles()} \n")

            else:
                raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos") # En caso de que no se cumpla alguna de las dos condiciones se retorna un mensaje de error indicando que la figura de cuatro vertices
                                                                                                                        # no corresponde ni a un rectangulo ni a un cuadrado. 
     ```


  b. En los triangulos se deben cumplir 2 cosas en particular:
     - Tener todos sus ángulos interno de 180°, esto se calcula con el terema del seno a partir de la longitud de los tres lados.
     - Cumplir las caracteristicas de alguno de estos tipos de triángulo: escaleno, isoceles, equilatero o rectangulo.


    Realmente lo importante es cumplir la primera condición, ya que si se cumple la figura si o si es un triángulo, por este motivo el caso de error estaria en esta verificación.


    ``` Python
    elif x == 3:  
            fo.initialize_shape(x)
            vertices = fo.get_vertices()
            sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
            triangulo = Triangle()

            if triangulo.triangle_type() == "Equilatero":
                if sum(triangulo.compute_angles()) != 180 and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[1]) and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")  # Esta condición es la que analiza si se cumple la suma de 180° de cada triangulo, tependiendo del caso.
                else:
                    eq = Equilateral()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo equilátero con todos sus lados de valor {sides[0]} por lo que es una figura {triangulo.regular()}")
                    print(f" Su perímetro es de: {eq.compute_perimeter()} y su área de: {eq.compute_area()}")
                    print(f" Sus ángulos internos son: {eq.compute_angles()} \n")

            elif triangulo.triangle_type() == "Isosceles":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != triangulo.compute_angles()[1] and triangulo.compute_angles()[0] != triangulo.compute_angles()[2] and triangulo.compute_angles()[1] != triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    iso = Isosceles()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo isósceles de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()}  ")
                    print(f"   Su perímetro es de: {iso.compute_perimeter()} y su área es: {iso.compute_area()}")
                    print(f"   Sus ángulos internos son: {iso.compute_angles()} \n ")

            elif triangulo.triangle_type() == "Escaleno":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] == triangulo.compute_angles()[1] or triangulo.compute_angles()[0] == triangulo.compute_angles()[2] or triangulo.compute_angles()[1] == triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    es = Scalene()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde con un triángulo escaleno de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
                    print(f"   Su perímetro es de: {es.compute_perimeter()} y su área es: {es.compute_area()}")
                    print(f"   Sus ángulos internos son: {es.compute_angles()} \n ")

            elif triangulo.triangle_type() == "Rectangulo":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != 90 and triangulo.compute_angles()[1] != 90 and triangulo.compute_angles()[2] != 90):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    rec = RectangleTriangle()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo rectángulo de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
                    print(f"   Su perímetro es de: {rec.compute_perimeter()} y su área de: {rec.compute_area()}")
                    print(f"   Sus ángulos internos son: {rec.compute_angles()} \n ")

            else:
                raise ValueError("Los datos ingresados no corresponden a un triangulo")

    ```
--------------------------------------------------------------------------------------
# Gracias por leer :)
  


     
    
       

