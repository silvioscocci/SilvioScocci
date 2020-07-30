#Clase para la tasa de las divisas
class Tasa(object):
    tasa = "1"
    #constructor
    def __init__(self, tasa):
        self.tasa = tasa
    #funcion de escritura
    def write(self):
        with open("tasa.txt",'w') as archivo:
            archivo.write(self.tasa)
