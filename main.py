from Producto import Producto
from Ventas import Ventas
from Tasa import Tasa
from Categoria import Categoria
import os
import datetime

# Variables globales
products = list()
ventas = list()
categorias = list()
tasa = Tasa('1')
codes = []

#Funcion para limpiar la pantalla dependiendo del sistema operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Funcion para listar todos los productos
def listar():
    clear() #Limpio
    #Armo la tabla
    titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    for product in products:
        print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                product.codigo, 
                product.nombre, 
                product.description,
                product.categoria,
                product.precio,
                product.cantidad_disponible
            ))
    print("-"*len(titles))
    input("Presione cualquier tecla para volver...")

#Funcion para listar por categoria
def listar_categoria():
    opcion = 0
    while opcion != "x":
        cont = 1
        clear()
        #Pinto todas las categorias disponibles
        print("--------------Seleccione la categoria a revisar------------------\n\n")
        for cat in categorias:
            print("{0}. {1}".format(cont, cat.nombre))
            cont +=1
        opcion = input("Eliga una opcion, x para salir: ")
        if(opcion!="x"):  
            #mando a pintar la tabla
            dibujar_lista(int(opcion))
            input("Presione cualquier tecla para volver...")

#Funcion para pintar las listas de productos por categoria
def dibujar_lista(pos):
    clear()
    cat = categorias[pos - 1].id
    titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    for product in products:
        if product.categoria == cat:
            print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                    product.codigo, 
                    product.nombre, 
                    product.description,
                    product.categoria,
                    product.precio,
                    product.cantidad_disponible
                ))
    print("-"*len(titles))
    
# Funcion para crear una categoria
def crear_categoria():
    print("--------------Crea otra categoria------------------\n\n")
    nombre = input("Nombre: ")
    cat = Categoria(nombre)
    cat.write()
    clear()
    print("--------------Categoria creada------------------\n\n")
    print("Presiona una tecla para regresar...")


#Funcion para crear producto
def crear_producto():
    clear()
    print("--------------Introduzca los datos del nuevo producto------------------\n\n")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    desc = input("Descripcion: ")
    print("Seleccione la categoria del producto \n")
        for t in categorias:
            print("\t{0}. {1}".format(indice, t.nombre))
            indice +=1
        tag = input("tag: ")
        try:
            tag = int(tag)
            if tag > indice:
                tag = 0
            else:
                tag = categorias[tag-1].id
        except ValueError:
            tag = 1
    categoria = input("Categoria: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad inicial: ")
    
    #valido que el codigo no este usado ya
    if (codigo in codes):
        clear()
        print("XXXXXX El codigo de producto ya esta en uso XXXXXX\n\n")
        input()
        crear_producto()
    #Valido que no esten vacios algunos campos
    elif (codigo == '') or (nombre == '') or (desc == '') or (categoria == ''):
        clear()
        print("XXXXXX Algun dato esta vacio completelo por favor XXXXXX\n\n")
        input()
        crear_producto()
    else:
        #Guardo el producto
        newProduct = Producto(codigo,nombre,desc,categoria,precio,cantidad)
        newProduct.write()
        products.append(newProduct)
        clear()
        print("--------------Producto creado correctamente------------------\n\n")
        input("Presione cualquier tecla para volver...")

#Editar producto
def editar_producto():
    clear()
    print("--------------Introduzca el codigo del producto a editar------------------\n\n")
    codigo = input("Codigo: ")
    #Verifico que exista el codigo al que quieren modificar
    if not codigo in codes:
        clear()
        print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
        editar_producto()
    else:
        #Mustro el producto
        index = codes.index(codigo)
        print("--------------Editando producto------------------\n\n")
        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
            products[index].codigo, 
            products[index].nombre, 
            products[index].description,
            products[index].categoria,
            products[index].precio,
            products[index].cantidad_disponible
        ))
        print("-"*len(titles)+"\n")
        nombre = input("Nombre: ")
        desc = input("Descripcion: ")
        categoria = input("Categoria: ")
        precio = input("Precio: ")
        cantidad = input("Cantidad: ")

        #Guardo los datos introducidos
        if nombre != "": products[index].nombre = nombre
        if desc != "": products[index].descripcion = desc
        if categoria != "": products[index].categoria = categoria
        if precio != "": products[index].precio = precio
        if cantidad != "": products[index].cantidad_disponible = cantidad

        products[index].write()
        print("--------------Producto editado------------------\n\n")
        print("Presiona una tecla para regresar...")

#Vender un producto
def vender():
    clear()
    print("--------------Introduzca el codigo del producto a vender------------------\n\n")
    codigo = input("Codigo: ")
    #Verifico que el producto a vender este en la base de datos
    if not codigo in codes:
        clear()
        print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
        vender()
    else:
        #Muestro el producto
        index = codes.index(codigo)
        print("--------------Editando producto------------------\n\n")
        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format(
            products[index].codigo, 
            products[index].nombre, 
            products[index].description,
            products[index].categoria,
            products[index].precio,
            products[index].cantidad_disponible
        ))
        print("-"*len(titles)+"\n")
        cantidad = float(input("Cantidad a vender: "))
        #Verifico que la cantidad este
        if cantidad > float(products[index].cantidad_disponible):
            clear()
            print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
            vender()
        else:
            #Muestro la factura
            clear()
            titles = "| {:<10} | {:<15} | {:<20} | {:<20} | {:<20}|".format("Total Bs.","Total $", "Codigo", "Fecha", "Cantidad")
            print("-"*len(titles))
            print(titles)
            print("-"*len(titles))
            date = datetime.datetime.now()
            print("| {:<10} | {:<15} | {:<20} | {:<20} | {:<20}|".format(
                products[index].price_in_bs(float(tasa.tasa)), 
                products[index].precio, 
                products[index].codigo,
                date.strftime('%x'),
                cantidad
            ))
            print("-"*len(titles))
            aceptado = input("Presione x para cancelar o cualquier tecla para aceptar...  ")
            #Guardo la venta
            if aceptado != "x" and aceptado != "X":
                products[index].cantidad_disponible = float(products[index].cantidad_disponible) - cantidad
                products[index].write()
                venta = Ventas(
                    products[index].price_in_bs(float(tasa.tasa)), 
                    products[index].precio, 
                    products[index].codigo,
                    datetime.datetime.now(),
                    cantidad
                )
                venta.write()
                ventas.append(venta)
                clear()
                print("--------------Venta realizada exitosamente------------------\n\n")
                input("Presione cualquier tecla para volver...")
#Funcion para mostrar las estadisticas
def estadisticas():
    opcion = 0
    while opcion != 5:
        clear()
        print("--------------Estadisticas------------------\n\n")
        print("1. Total en ventas  2. Productos agotados 3. Producto mas costoso 4.Producto mas economico 5. Volver\n")
        opcion = int(input("Eliga una opcion: "))
        if opcion == 1:
            total_ventas()
        elif opcion == 2:
            productos_agotados()
        elif opcion == 3:
            producto_mas_caro()
        elif opcion == 4:
            producto_mas_barato()

#Mostrar el total en dolares y bolivares
def total_ventas():
    clear()
    total_dolares = 0
    total_bolivares = 0
    for venta in ventas:
        total_bolivares += float(venta.total_bolivares)
        total_dolares += float(venta.total_dolares)
    titles = "| {:<10} | {:<15}|".format("Total Bolivares.","Total Dolares")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    print("| {:<16} | {:<15}|".format(total_bolivares, total_dolares))
    input("Presiona cualquier tecla...")

#Mostrar productos en existencia 0
def productos_agotados():
    titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    for product in products:
        if float(product.cantidad_disponible) <= 0:
            print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                product.codigo, 
                product.nombre, 
                product.description,
                product.categoria,
                product.precio,
                product.cantidad_disponible
            ))
    print("-"*len(titles))
    input("Presiona cualquier tecla...")

#Mostrar producto mas economico
def producto_mas_barato():
    mas_barato = products[0]
    for producto in products:
        if float(producto.precio) < float(mas_barato.precio):
            mas_barato = producto

    titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
        mas_barato.codigo, 
        mas_barato.nombre, 
        mas_barato.description,
        mas_barato.categoria,
        mas_barato.precio,
        mas_barato.cantidad_disponible
    ))
    print("-"*len(titles)+"\n")
    input("Presiona cualquier tecla...")

#Mostrar producto mas caro
def producto_mas_caro():
    mas_caro = products[0]
    for producto in products:
        if float(producto.precio) > float(mas_caro.precio):
            mas_caro = producto

    titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "Categoria", "Precio", "Cantidad")
    print("-"*len(titles))
    print(titles)
    print("-"*len(titles))
    print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
        mas_caro.codigo, 
        mas_caro.nombre, 
        mas_caro.description,
        mas_caro.categoria,
        mas_caro.precio,
        mas_caro.cantidad_disponible
    ))
    print("-"*len(titles)+"\n")
    input("Presiona cualquier tecla...")

#Cambiar la tasa de la divisa
def editar_tasa():
    clear()
    print("La tasa actual es: " + tasa.tasa)
    new_tasa = input("Defina una nueva tasa: ")
    if new_tasa == "" or float(new_tasa) <= 0:
        print("XXXXXX La tasa es invalida, vuelva a intentarlo XXXXXX\n")
        input()
        editar_tasa()
    else:
        tasa.tasa = new_tasa
        tasa.write()

## Funciones para setear las variables globales
def getProducts():
    with open('productos.txt', 'r') as archivo:
        for line in archivo:
            row = line.split(';')
            products.append(Producto(row[0],row[1],row[2],row[3],row[4],row[5].split('\n')[0]))
            codes.append(row[0])

def getVentas():
    with open('ventas.txt', 'r+') as archivo:
        for line in archivo:
            row = line.split(';')
            ventas.append(Ventas(row[0],row[1],row[2],row[3],row[4].split('\n')[0]))

def setTasa():
    with open("tasa.txt", 'r+') as archivo:
        line = archivo.readline()
        tasa.tasa = line

def getCategorias():
    with open('categorias.txt', 'r') as archivo:
        for line in archivo:
            row = line.split(';')
            categorias.append(Categoria(row[1].split('\n')[0], row[0]))

def main():
    opcion = 0;
    getProducts()
    getVentas()
    setTasa()
    getCategorias()
    while(opcion != 9):
        clear()
        print("|| Sistema de control de inventario y ventas de Flacco y Asociados C.A ||".upper())
        head = "| {:<25} |".format("Opcion")
        print("-"*len(head))
        print(head)
        print("-"*len(head))
        print("| {:<25} |".format("1. Listar productos"))
        print("| {:<25} |".format("2. Listar x categoria"))
        print("| {:<25} |".format("3. Crear producto"))
        print("| {:<25} |".format("4. Crear categoria"))
        print("| {:<25} |".format("5. Editar producto"))
        print("| {:<25} |".format("6. Vender"))
        print("| {:<25} |".format("7. Estadisticas"))
        print("| {:<25} |".format("8. Divisa"))
        print("| {:<25} |".format("9. Salir"))
        print("-"*len(head))
        opcion = input("Seleccione una opcion: ")
        try:
            opcion = int(opcion)
            if opcion == 1:
                listar()
            elif opcion == 2:
                listar_categoria()
            elif opcion == 3:
                crear_producto()
            elif opcion == 4:
                crear_categoria()
            elif opcion == 5:
                editar_producto()
            elif opcion == 6:
                vender()
            elif opcion == 7:
                estadisticas()
            elif opcion == 8:
                editar_tasa()
        except ValueError:
            pass
        
        

if __name__ == "__main__":
    main()
