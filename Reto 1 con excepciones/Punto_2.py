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