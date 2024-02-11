# Proyecto 3:

# Pedir al usuario que ingrese un texto

texto_usuario = input("Ingrese un texto: ")

# Pedir al usuario que ingrese tres letras

letra1 = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

# 1. Contar cuántas veces aparece cada letra

texto_usuario = texto_usuario.lower()
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

conteo_letra1 = texto_usuario.count(letra1)
conteo_letra2 = texto_usuario.count(letra2)
conteo_letra3 = texto_usuario.count(letra3)

# 2. Contar la cantidad de palabras en el texto

cantidad_palabras = len(texto_usuario.split())

# 3. Obtener la primera y última letra del texto

primera_letra = texto_usuario[0]
ultima_letra = texto_usuario[-1]

# 4. Invertir el orden de las palabras en el texto

palabras = texto_usuario.split()
texto_invertido = " ".join(palabras[::-1])

# 5. Verificar si la palabra "python" está en el texto

palabra_python = "python" in texto_usuario.lower()

# Resultados:

print("1. Cantidad de veces que aparece cada letra:")
print("   " + letra1 + ": " + str(conteo_letra1))
print("   " + letra2 + ": " + str(conteo_letra2))
print("   " + letra3 + ": " + str(conteo_letra3))

print("2. Cantidad de palabras en el texto:", cantidad_palabras)

print("3. Primera letra del texto:", primera_letra)
print("   Última letra del texto:", ultima_letra)

print("4. Texto con palabras invertidas:")
print(texto_invertido)

print("5. ¿La palabra 'python' se encuentra en el texto?:", palabra_python)