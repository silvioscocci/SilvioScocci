#Clase de categorias
class Categoria(object):
    nombre = ""
    id = 0
    #constructor
    def __init__(self,nombre, id):
        self.nombre = nombre
        if(id):
            self.id = id
        else:
            self.id = self.get_id()
    #Funcion para crear ids
    def get_id(self):
        id = 0
        with open('categorias.txt', 'r+') as archivo:
            lines = archivo.readlines()
            id = int(lines[len(lines)-1].split(';')[0]) + 1
        return id
    #funcion para escribir en el archivo
    def write(self):
        with open("categorias.txt",'w') as archivo:
            archivo.write("\n{0};{1}".format(self.id, self.nombre))
