from libreria import existe_libro, libros_por_autor, listar_libros

# Añade una colección de libros
coleccion_libros = {
    "Cien años de soledad":"Gabriel García Márquez",
    "Don Quijote de la Mancha":"Miguel de Cervantes",
    "El principito":"Antoine de Saint-Exupéry"
    }


# Muestra la colección de libros creada
print()
print(listar_libros(coleccion_libros))
# Busca un libro por el autor
print(libros_por_autor(coleccion_libros,"Miguel de Cervantes"))

# Verifica si un libro está disponible
print(existe_libro(coleccion_libros, "El principito"))