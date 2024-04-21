

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

