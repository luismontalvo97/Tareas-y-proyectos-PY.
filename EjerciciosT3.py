#Ejercicios – Tema 3

#1.	Encuentra y muestra por pantalla qué caracter ocupa la 3 posición dentro de la siguiente palabra: “escritorio”.

palabra = "escritorio"
tercer_caracter = palabra[2]
print("El tercer caracter de la palabra \"escritorio\" es:", tercer_caracter)


#2.	Muestra por pantalla el índice de la primera aparición de la palabra “videojuego” en la siguiente frase: “No es por nada, pero este videojuego es demasiado fácil”.

frase = "No es por nada, pero este videojuego es demasiado fácil"
indice_videojuego = frase.find("videojuego")
print(indice_videojuego)


#3.	Muestra por pantalla el índice de la última aparición de la palabra “ejercicio” en la siguiente frase: “Tengo que asegurarme de comprobar el ejercicio para que no tenga errores”.

frase = "Tengo que asegurarme de comprobar el ejercicio para que no tenga errores"
indice_ultima_ejercicio = frase.rfind("ejercicio")
print(indice_ultima_ejercicio)



#4.	Extrae la primera palabra de la siguiente frase usando slicing, y muéstrala por pantalla: “Escribir código es fundamental para aprender programación”.

frase = "Escribir código es fundamental para aprender programación"
primera_palabra = frase[:frase.find(" ")]
print("La primera palabra de la frase es: ", primera_palabra)


#5.	Coge cada tercer caracter empezando desde el sexto hasta el final de la frase, e imprime el resultado: “Python es uno de los lenguajes más populares de la actualidad”.

frase = "Python es uno de los lenguajes más populares de la actualidad"
resultado_5 = frase[5::3]
print(resultado_5)


#6.	Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado por pantalla: “Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida”.

frase = "Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida"
resultado_6 = frase[::-1]
print("Frase invertida:", resultado_6)

#7.	Imprime el siguiente texto en mayúsculas, usando métodos de strings. “Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación”.

texto = "Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación"
resultado_7 = texto.upper()
print("Texto en mayúsculas:", resultado_7)


#8.	Dada la siguiente lista, únela completa en un string, separando cada elemento con un espacio. Usa métodos específicos para ello, y muestra el resultado por pantalla:

palabras = ["Este", "curso", "me", "gusta"]
resultado_8 = " ".join(palabras)
print("Lista unida en un string:", resultado_8)

#9.	Haz reemplazos en la siguiente frase: “No sé con cuál quedarme, si con el primero o con el segundo”. Debes cambiar “el primero” por “JavaScript” y “el segundo” por “Python”. Muestra el resultado por pantalla.

frase = "No sé con cuál quedarme, si con el primero o con el segundo"
frase_modificada = frase.replace("el primero", "JavaScript").replace("el segundo", "Python")
print("Frase modificada:", frase_modificada)

#10. Verifica si la palabra “trabajo” no se encuentra en la siguiente frase. Debes imprimir el booleano: “Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado”.

frase = "Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado"
resultado_10 = "trabajo" not in frase
print(resultado_10)

#11. Concatena 12 veces la palabra “Python” y muestra el resultado por pantalla. Recuerda que los strings son multiplicables.

palabra = "Python" * 12
print(palabra)


#12. Muestra el largo de la palabra “esternocleidomastoideo”. Hazlo por pantalla y con el número de caracteres.

palabra = "esternocleidomastoideo"
largo = len(palabra)
print("Largo de la palabra:", largo)

#13. Crea una lista con 8 elementos, dentro de la variable “lista”. Puedes incluir los tipos de datos que quieras. Muéstrala por pantalla.

lista = [99, "nueve", True, 3.8, ["Python", "Java"], {'a': 1, 'b': 2}, None, (4, 5)]
print("Lista creada:", lista)

#14. Agrega el elemento “JavaScript” a la siguiente lista (No modifiques la línea de código dada, sino que debes usar métodos apropiados para listas).

lenguajes = ["Python", "Ruby", "PHP", "CSS"]
lenguajes.append("JavaScript")
print("Lista con 'JavaScript' agregado:", lenguajes)


#15. Usa el método pop() para quitar el quinto elemento de la siguiente lista llamada marcas, y almacénalo en una variable llamada “eliminada”. Usa métodos de listas para no alterar la línea de código:

marcas = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
eliminada = marcas.pop(4)
print("Elemento eliminado:", eliminada)
print("Lista actualizada:", marcas)

#16. Crea un diccionario que almacene la siguiente información: Tu nombre, tu primer apellido, tu edad y tu profesión.

informacion_personal = {"nombre": "Luis", "apellido": "Montalvo", "edad": 26, "profesion": "MP Manager"}
print("Diccionario creado:", informacion_personal)

#17. Usa print para que devuelva el segundo ítem del diccionario que creaste antes. Muéstralo por pantalla, y deberás asegurarte de que, si cambia el código te siga mostrando el valor almacenado en dicha clave.

print("Segundo ítem del diccionario:", informacion_personal["apellido"])

#18. Dado el siguiente diccionario:

#diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
# Añade una clave que sea "país", sin tilde, y dale el valor que quieras
# Muestra el resultado por pantalla
# No modifiques la línea de código

diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28}
diccionario["pais"] = "España"
print("Diccionario con clave \"país\" añadida:", diccionario)

#19. Usa un método de tuplas para contar la cantidad de veces que aparece el valor 3 en la siguiente tupla y muestra el resultado en pantalla:

tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
cantidad_tres = tupla_ejercicio.count(3)
print("Cantidad de veces que aparece el valor 3:", cantidad_tres)

#20. Convierte la siguiente tupla en una lista y almacénala en una variable:

tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
lista_ejercicio = list(tupla_ejercicio)
print("Tupla convertida en lista:", lista_ejercicio)

#21. Extrae los elementos de la siguiente tupla en 6 variables a, b, c, d, e, f:

tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a, b, c, d, e, f = tupla_ejercicio
print("Variables extraídas de la tupla:", a, b, c, d, e, f)


#22. Une los siguientes sets en uno solo:

set1 = {8, 10, "once", "doce"}
set2 = {"once", 4, 5}
set_unido = set1.union(set2)
print("Unión de los sets:", set_unido)

#23. Elimina un elemento al azar del siguiente set utilizando métodos adecuados:

loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
elemento_eliminado = loteria.pop()
print("Elemento eliminado al azar:", elemento_eliminado)
print("Set actualizado:", loteria)

#24. Agrega el nombre de Lorenzo al siguiente set usando métodos adecuados:

nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add("Lorenzo")
print("Set con el nombre \"Lorenzo\" agregado:", nombres)

#25. Realiza una comparación que tenga como resultado un booleano y almacena el resultado en una variable llamada prueba.

prueba = (5 > 3)
print("Resultado de la comparación (5 > 3):", prueba)

#26. Verifica si 19238 / 38 es mayor que 92*59 y muestra el resultado en pantalla utilizando print. Recuerda que es un booleano.

resultado_26 = (19238 / 38 > 92 * 59)
print("¿19238 / 38 es mayor que 92 * 59?", resultado_26)

#27. Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado usando print.

resultado_27 = (25 ** 0.5 == 5)
print("¿La raíz cuadrada de 25 es igual a 5?", resultado_27)