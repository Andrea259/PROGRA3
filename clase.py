class carro():
   #propiedades
    color = ""
    modelo = ""
    year = ""
    cilindro = ""
    hp = ""

    #metodos
    def insd(self,color,modelo,year,cilindro,hp):
        self.color = color
        self.modelo = modelo
        self.year = year
        self.cilindro = cilindro
        self.hp = hp

    def mostrad(self):
        print("***datos del vehiculo***\n"+
              f"color: {self.color}\n"+
              f"modelo: {self.modelo}\n"+
              f"año: {self.year}\n"+
              f"cantidad de cilindro: {self.cilindro}\n"+
              f"caballos de fuerza: {self.hp}\n")
        
carro1 = carro()
carro1.insd("rojo anaranjado", "ford escape", 2011,
            4, 200)

carro1.mostrad()