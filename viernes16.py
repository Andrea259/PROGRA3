#clases abstractas
#el encapsulamiento se utiliza para restringir el acceso directo a algunas variables y metodos.

class Padre():
    atributos1 = "valor"
    atributos2 = "valor2"
    atributos3 = "valor3"

    def metodo1():
        pass

    def metodo2():
        pass
#clase hija hereda de padre
class Hija(Padre):
    atributoh = "hija"

    def metodoh(self):
        print("est metodo es de la clase hija")

    Padre = Padre()
    Padre.metodo1()
    Hija = Hija()
    Hija.metodo1()

    #overriding y super
    