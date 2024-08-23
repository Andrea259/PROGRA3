"""
creare un sistema para gestionar una pequeña biblioteca. 
y que se pueda agregar nuevos libros, buscar libros por título o autor, y mostrar 
información sobre los libros que esten disponibles disponibles.
"""
#crear clase libro con los atributos del titulo, autor y año del libro
class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}"
    
#creacion clase biblio con el atributo libro
class biblio:
    def __init__(self):
        self.libros = []
#agregamos un metodo para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)
#utilizamos un metodo para buscar un libro
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
#usamos un metodo para mostrar los libros
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

#crear un menu de 4 opciones en donde se puede escoger entre agregar libro,
#buscar libro y mostrar todos los libros

if __name__ == "__main__":
    biblioteca = biblio()

    while True:
        print("\nOpciones:")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")
            año = int(input("Ingrese el año: "))
            nuevo_libro = libro(titulo, autor, año)
            biblioteca.agregar_libro(nuevo_libro)
            print("Libro agregado exitosamente.")
        elif opcion == 2:
            titulo = input("Ingrese el título a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print(libro)
            else:
                print("Libro no encontrado.")
        elif opcion == 3:
            biblioteca.mostrar_libros()
        elif opcion == 4:
            break
        else:
            print("Opción inválida.")