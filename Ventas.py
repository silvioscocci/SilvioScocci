#Clase para llevar el control de las ventas de los productos
class Ventas(object):
    total_dolares = 0
    total_bolivares = 0
    fecha = ""
    codigo = ""
    cantidad = 0

    #constructor de la clase
    def __init__(self,  total_bs, total_dl, fecha, codigo, cantidad):
        self.total_dolares = total_dl
        self.total_bolivares = total_bs
        self.fecha = fecha
        self.codigo = codigo
        self.cantidad = cantidad
    
    #Funcion para escribir en el archivo
    def write(self):
        with open("ventas.txt",'a') as archivo:
            archivo.write("\n{0};{1};{2};{3};{4}".format(
                self.total_dolares, 
                self.total_bolivares, 
                self.fecha, 
                self.codigo,
                self.cantidad
            ))
