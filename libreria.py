"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

# Escribe tu código aquí
def agregar_libro(titulo, autor):
    diccionario = {}
    diccionario[titulo] = autor
    return diccionario
# Prueba la función con algunos valores
print(agregar_libro("python","anonimo"))

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

# Escribe tu código aquí
def listar_libros(libros):
    lista = [libro for libro in libros]
    
    return lista
# Prueba la función con algunos valores
print(listar_libros({"python":"anonimo","javascript":"anonimo"}))

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

# Escribe tu código aquí
def buscar_libro(libros, titulo):
    autor = libros[titulo]
    if autor:
        return {titulo:autor}
    return
# Prueba la función con algunos valores
libros = {"python":"anonimo","javascript":"anonimo"}
print(buscar_libro(libros, "python"))
"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

# Escribe tu código aquí
def quitar_libro(libros, titulo):
    if titulo in libros:
        del libros[titulo]
        return libros
    return
    
# Prueba la función con algunos valores
print(quitar_libro(libros, "python3"))

"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

# Escribe tu código aquí
def crear_inventario(libros):
    return len([autor for autor in libros.values()])
# Prueba la función con algunos valores
print(crear_inventario(libros))

"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

# Escribe tu código aquí
def libros_por_autor(libros, autor):
    listar_titulos = []
    for titulo in libros:
        if autor == libros[titulo]:
            listar_titulos.append(titulo)
    return listar_titulos
    

# Prueba la función con algunos valores
print(libros_por_autor(libros, "anonimo"))
"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

# Escribe tu código aquí
def existe_libro(libros, titulo):
    if titulo in libros:
        return True
    return False
# Prueba la función con algunos valores
print(existe_libro(libros, "python"))
