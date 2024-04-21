import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_coordinates(self):
        return self._x, self._y   

class Line:
    def __init__(self, initial_point, final_point):
        self._initial_point = initial_point
        self._final_point = final_point

    def length(self):
        x1, y1 = self._initial_point.get_coordinates() 
        x2, y2 = self._final_point.get_coordinates()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 

class Shape:
    def __init__(self):
      pass

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


class Rectangle(Shape): 
    def __init__(self):
        super().__init__()  
                                
    def compute_perimeter(self): 
        return sum(sides)   

    def compute_area(self):
        return sides[0] * sides[1] 

    def compute_angles(self): 
      return [90, 90, 90, 90]   
    
    def regular(self): 
       return "No es regular" 


class Square(Rectangle):
    def __init__(self):
        super().__init__() 
                             
    def regular(self):
       return "regular"

class Triangle(Shape): 
    def __init__(self):
        pass

    def triangle_type(self):
        if sides[0] == sides[1] == sides[2]:
            return "Equilatero"                                                       
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:      
            return "Isosceles"
        elif sides[0] ** 2 + sides[2] ** 2 == sides[1] ** 2:
            return "Rectangulo"
        elif sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
            return "Escaleno"

    def compute_perimeter(self):
        return sum(sides) 

    def compute_area(self):
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) 

    def compute_angles(self):
        ca = math.acos((sides[0] ** 2 - sides[1] ** 2 - sides[2] ** 2) / (-2 * sides[1] * sides[2])) * (180 / math.pi)
        cb = math.acos((sides[1] ** 2 - sides[0] ** 2 - sides[2] ** 2) / (-2 * sides[0] * sides[2])) * (180 / math.pi)  
        cc = math.acos((sides[2] ** 2 - sides[0] ** 2 - sides[1] ** 2) / (-2 * sides[0] * sides[1])) * (180 / math.pi)    
        return [ca, cb, cc] 
    
    def regular(self):
      triangle_type = self.triangle_type()
      if triangle_type == "Equilatero" or triangle_type == "Isosceles": 
        return "regular"
      else:
        return "No regular"

class Equilateral(Triangle):  
    def __init__(self):
        super().__init__()

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()

class Scalene(Triangle):
    def __init__(self):
        super().__init__()

class RectangleTriangle(Triangle):
    def __init__(self):
        super().__init__()

def main():
    global fo, vertices, sides
    print("   -Bienvenido- \n El siguiente programa permite analizar cuadrados, rectangulos y triangulos a partir de sus vertices, por favor ingrese datos coherentes. \n")
    fo = Shape()
    while True:
        x = int(input("Ingrese la cantidad de cordenadas de su figura (vertices);, si desea salir selecione 1: \n ")) 
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
                raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")   # En caso de que no se cumpla alguna de las dos condiciones se retorna un mensaje de error indicando que
                                                                                                                        # no corresponde ni a un rectangulo ni a un cuadrado.
        elif x == 3:  
            fo.initialize_shape(x)
            vertices = fo.get_vertices()
            sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
            triangulo = Triangle()
                                                                # Esta condición es la que analiza si se cumple la suma de 180° de cada triangulo, tependiendo del caso.
            if triangulo.triangle_type() == "Equilatero":
                if sum(triangulo.compute_angles()) != 180 and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[1]) and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")     
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

        elif x == 1:  
            break

        else:    
            raise ValueError("Opción no válida") # Retorna un error si el usuario no ingresa una opción valida.

if __name__ == "__main__":
    print(main())
  