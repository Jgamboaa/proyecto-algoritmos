import csv
import os
import getpass
from prettytable import PrettyTable

os.system("cls")

usuarios = {"admin": "admin", "cajero": "cajero"}

class Empleado:
    def __init__(self, nombre, apellido, dpi, telefono, direccion, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.dpi = dpi
        self.telefono = telefono
        self.direccion = direccion
        self.cargo = cargo

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.nombre, self.apellido, self.dpi, self.telefono, self.direccion, self.cargo)

empleados = []

class Producto:
    def __init__(self, nombre, precio, cantidad, proveedor):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor = proveedor

    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.precio, self.cantidad, self.proveedor)

productosBodega = []

productosTienda = []

clientes = []

class Cliente:
    def __init__(self, nombre, direccion, nit):
        self.nombre = nombre
        self.direccion = direccion
        self.nit = nit

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.direccion, self.nit)


def input_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Ingrese un número válido.")
            
def cargar_empleados_desde_archivo():
    try:
        with open("empleados.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            for row in reader:
                nombre, apellido, dpi, telefono, direccion, cargo = row
                empleado = Empleado(nombre, apellido, dpi, telefono, direccion, cargo)
                empleados.append(empleado)
    except FileNotFoundError:
        # El archivo no existe, lo creamos vacío
        with open("empleados.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Apellido", "DPI", "Teléfono", "Dirección", "Cargo"])

def guardar_empleado_en_archivo(empleado):
    with open("empleados.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([empleado.nombre.upper(), empleado.apellido.upper(), empleado.dpi.upper(), empleado.telefono.upper(), empleado.direccion.upper(), empleado.cargo.upper()])

def cargar_productosBodega_desde_archivo():
    try:
        with open("productosBodega.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            for row in reader:
                nombre, precio, cantidad, proveedor = row
                producto = Producto(nombre, float(precio), int(cantidad), proveedor)
                productosBodega.append(producto)
    except FileNotFoundError:
        # El archivo no existe, lo creamos vacío
        with open("productosBodega.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])

def guardar_productoBodega_en_archivo(producto):
    with open("productosBodega.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([producto.nombre.upper(), producto.precio, producto.cantidad, producto.proveedor.upper()])

def cargar_productosTienda_desde_archivo():
    try:
        with open("productosTienda.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            for row in reader:
                nombre, precio, cantidad, proveedor = row
                producto = Producto(nombre, float(precio), int(cantidad), proveedor)
                productosTienda.append(producto)
    except FileNotFoundError:
        # El archivo no existe, lo creamos vacío
        with open("productosTienda.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])

def guardar_productoTienda_en_archivo(producto):
    with open("productosTienda.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([producto.nombre.upper(), producto.precio, producto.cantidad, producto.proveedor.upper()])

def menu():
    os.system("cls")
    print("Sistema de Facturación")
    print("SUPER TIENDA MAS")
    print("1. Administrador")
    print("2. Cajero")
    print("3. Bodega")
    print("4. Salir")
    opcion = input_entero("Ingrese la opción: ")
    return opcion

def menu_admin():
    os.system("cls")
    print("1. Crear Empleado")
    print("2. Eliminar Empleado")
    print("3. Editar Empleado")
    print("4. Reportes")
    print("5. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def crear_empleado():
    os.system("cls")
    print("Crear Empleado")
    nombre = input("Ingrese el nombre del empleado: ").upper()
    apellido = input("Ingrese el apellido del empleado: ").upper()
    dpi = input("Ingrese el DPI del empleado: ").upper()
    telefono = input("Ingrese el teléfono del empleado: ").upper()
    direccion = input("Ingrese la dirección del empleado: ").upper()
    cargo = input("Ingrese el cargo del empleado: ").upper()
    empleado = Empleado(nombre, apellido, dpi, telefono, direccion, cargo)
    empleados.append(empleado)
    print("Empleado creado")
    guardar_empleado_en_archivo(empleado)
    input("Presione enter para continuar")

def editar_empleado():
    os.system("cls")
    print("Editar Empleado")
    nombre = input("Ingrese el nombre del empleado a editar: ")
    for empleado in empleados:
        if empleado.nombre == nombre:
            nombre = input("Ingrese el nuevo nombre del empleado: ").upper()
            apellido = input("Ingrese el nuevo apellido del empleado: ").upper()
            dpi = input("Ingrese el nuevo DPI del empleado: ").upper()
            telefono = input("Ingrese el nuevo teléfono del empleado: ").upper()
            direccion = input("Ingrese la nueva dirección del empleado: ").upper()
            cargo = input("Ingrese el nuevo cargo del empleado: ").upper()

            empleado.nombre = nombre
            empleado.apellido = apellido
            empleado.dpi = dpi
            empleado.telefono = telefono
            empleado.direccion = direccion
            empleado.cargo = cargo

            # Actualizar el archivo CSV de empleados
            with open("empleados.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Apellido", "DPI", "Teléfono", "Dirección", "Cargo"])
                for empleado in empleados:
                    escritor.writerow([empleado.nombre, empleado.apellido, empleado.dpi, empleado.telefono, empleado.direccion, empleado.cargo])

            print("Empleado editado")
            break
    else:
        print("Empleado no encontrado")

    input("Presione enter para continuar")

def eliminar_empleado():
    os.system("cls")
    print("Eliminar Empleado")
    nombre = input("Ingrese el nombre del empleado a eliminar: ")
    for empleado in empleados:
        if empleado.nombre == nombre:
            empleados.remove(empleado)

            # Actualizar el archivo CSV de empleados
            with open("empleados.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Apellido", "DPI", "Teléfono", "Dirección", "Cargo"])
                for empleado in empleados:
                    escritor.writerow([empleado.nombre, empleado.apellido, empleado.dpi, empleado.telefono, empleado.direccion, empleado.cargo])

            print("Empleado eliminado")
            break
    else:
        print("Empleado no encontrado")

    input("Presione enter para continuar")

def reporte_usuarios():
    os.system("cls")
    print("Reporte de Usuarios")
    # Abre el archivo CSV en modo lectura
    with open("empleados.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)
        # Lee la primera fila que contiene los encabezados
        encabezados = next(lector)
        # Creamos una tabla con los encabezados
        tabla = PrettyTable(encabezados)
        # Lee y muestra los datos de los empleados
        for row in lector:
            # Agrega cada fila de datos a la tabla
            tabla.add_row(row)
        # Imprime la tabla
        print(tabla)
    input("Presione enter para regresar al menú")

def reporte_productos_bodega():
    os.system("cls")
    print("Reporte de Productos")
    # Abre el archivo CSV en modo lectura
    with open("productosBodega.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)
        # Lee la primera fila que contiene los encabezados
        encabezados = next(lector)
        # Creamos una tabla con los encabezados
        tabla = PrettyTable(encabezados)
        # Lee y muestra los datos de los productos
        for row in lector:
            # Agrega cada fila de datos a la tabla
            tabla.add_row(row) 
        # Imprime la tabla
        print(tabla)
    input("Presione enter para regresar al menú")
    return menu_bodega()

def menu_bodega():
    os.system("cls")
    print("1. Crear Producto")
    print("2. Eliminar Producto")
    print("3. Editar Producto")
    print("4. Trasladar Productos a Tienda")
    print("5. Reportes")
    print("6. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def producto_existente(producto_nombre, lista_productos):
    for producto in lista_productos:
        if producto.nombre == producto_nombre:
            return True
    return False

def crear_producto():
    os.system("cls")
    print("Crear Producto")
    nombre = input("Ingrese el nombre del producto: ").upper()

    # Verificar si el producto ya existe en la bodega o tienda
    if producto_existente(nombre, productosBodega) or producto_existente(nombre, productosTienda):
        print("El producto ya existe en la bodega o tienda.")
        input("Presione enter para continuar")
        return

    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    proveedor = input("Ingrese el proveedor del producto: ").upper()
    producto = Producto(nombre, precio, cantidad, proveedor)
    productosBodega.append(producto)
    print("Producto creado")
    guardar_productoBodega_en_archivo(producto)
    input("Presione enter para continuar")

def editar_productoBodega():
    os.system("cls")
    print("Editar Producto en Bodega")
    nombre = input("Ingrese el nombre del producto a editar: ")
    for producto in productosBodega:
        if producto.nombre == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").upper()
            precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            proveedor = input("Ingrese el nuevo proveedor del producto: ").upper()

            producto.nombre = nuevo_nombre
            producto.precio = precio
            producto.cantidad = nueva_cantidad
            producto.proveedor = proveedor

            # Actualizar el archivo CSV de productos en la bodega
            with open("productosBodega.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                for producto_bodega in productosBodega:
                    escritor.writerow([producto_bodega.nombre, producto_bodega.precio, producto_bodega.cantidad, producto_bodega.proveedor])

            print("Producto editado en la bodega")
            break
    else:
        print("Producto no encontrado en la bodega")

    input("Presione enter para continuar")

def eliminar_productoBodega():
    os.system("cls")
    print("Eliminar Producto de Bodega")
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productosBodega:
        if producto.nombre == nombre:
            productosBodega.remove(producto)

            # Actualizar el archivo CSV de productos en la bodega
            with open("productosBodega.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                for producto_bodega in productosBodega:
                    escritor.writerow([producto_bodega.nombre, producto_bodega.precio, producto_bodega.cantidad, producto_bodega.proveedor])

            print("Producto eliminado de la bodega")
            break
    else:
        print("Producto no encontrado en la bodega")

    input("Presione enter para continuar")

def trasladar_productoTienda():
    os.system("cls")
    print("Trasladar Producto a Tienda")
    nombre = input("Ingrese el nombre del producto a trasladar: ")

    producto_traslado = None  # Variable para almacenar el producto a trasladar

    # Buscar el producto en la lista de productos en la bodega
    for producto in productosBodega:
        if producto.nombre == nombre:
            producto_traslado = producto
            break

    if producto_traslado is not None:
        cantidad_existente = producto_traslado.cantidad
        print(f"Cantidad en existencia en la bodega: {cantidad_existente}")

        while True:
            cantidad_a_trasladar_str = input("Ingrese la cantidad que desea trasladar: ")

            try:
                cantidad_a_trasladar = int(cantidad_a_trasladar_str)  # Convertir a entero

                if cantidad_a_trasladar > 0 and cantidad_a_trasladar <= cantidad_existente:
                    # Actualizar la cantidad del producto en la bodega
                    producto_traslado.cantidad -= cantidad_a_trasladar

                    # Buscar el producto en la lista de productos en la tienda
                    producto_tiendas = [p for p in productosTienda if p.nombre == nombre]

                    if len(producto_tiendas) > 0:
                        # El producto ya existe en la tienda, actualiza la cantidad
                        producto_tienda = producto_tiendas[0]
                        producto_tienda.cantidad += cantidad_a_trasladar
                    else:
                        # El producto no existe en la tienda, crea un nuevo registro
                        producto_tienda = Producto(producto_traslado.nombre, producto_traslado.precio, cantidad_a_trasladar, producto_traslado.proveedor)
                        productosTienda.append(producto_tienda)

                    # Actualizar el archivo CSV de productos en la bodega
                    with open("productosBodega.csv", "w", newline="") as archivo_bodega:
                        escritor_bodega = csv.writer(archivo_bodega)
                        escritor_bodega.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                        for producto_bodega in productosBodega:
                            escritor_bodega.writerow([producto_bodega.nombre, producto_bodega.precio, producto_bodega.cantidad, producto_bodega.proveedor])

                    # Actualizar el archivo CSV de productos en la tienda
                    with open("productosTienda.csv", "w", newline="") as archivo_tienda:
                        escritor_tienda = csv.writer(archivo_tienda)
                        escritor_tienda.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                        for producto_tienda in productosTienda:
                            escritor_tienda.writerow([producto_tienda.nombre, producto_tienda.precio, producto_tienda.cantidad, producto_tienda.proveedor])

                    print(f"{cantidad_a_trasladar} unidades del producto trasladadas a la tienda")
                    break
                else:
                    print("La cantidad a trasladar debe ser mayor que 0 y no mayor que la cantidad en existencia en la bodega.")
            except ValueError:
                print("La cantidad ingresada no es válida.")
    else:
        print("Producto no encontrado en la bodega")

    input("Presione enter para continuar")

def menu_cajero():
    os.system("cls")
    print("1. Productos")
    print("2. Clientes")
    print("3. Venta")
    print("4. Reportes")
    print("5. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def menu_productos():
    os.system("cls")
    print("1. Buscar Producto")
    print("2. Trasladar Producto a Bodega")
    print("3. Editar Producto")
    print("4. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def buscar_producto():
    os.system("cls")
    print("Buscar Producto")
    nombre = input("Ingrese el nombre del producto a buscar: ")
    for producto in productosBodega:
        if producto.nombre == nombre:
            print("Producto encontrado en la bodega:")
            print(producto)
            break
    else:
        for producto in productosTienda:
            if producto.nombre == nombre:
                print("Producto encontrado en la tienda:")
                print(producto)
                break
        else:
            print("Producto no encontrado")

    input("Presione enter para continuar")

def trasladar_productoBodega():
    os.system("cls")
    print("Trasladar Producto a Bodega")
    nombre = input("Ingrese el nombre del producto a trasladar: ")

    producto_traslado = None  # Variable para almacenar el producto a trasladar

    # Buscar el producto en la lista de productos en la tienda
    for producto in productosTienda:
        if producto.nombre == nombre:
            producto_traslado = producto
            break

    if producto_traslado is not None:
        cantidad_existente = producto_traslado.cantidad
        print(f"Cantidad en existencia en la tienda: {cantidad_existente}")

        while True:
            cantidad_a_trasladar_str = input("Ingrese la cantidad que desea trasladar a la bodega: ")

            try:
                cantidad_a_trasladar = int(cantidad_a_trasladar_str)  # Convertir a entero

                if cantidad_a_trasladar > 0 and cantidad_a_trasladar <= cantidad_existente:
                    # Actualizar la cantidad del producto en la tienda
                    producto_traslado.cantidad -= cantidad_a_trasladar

                    # Buscar el producto en la lista de productos en la bodega
                    producto_bodegas = [p for p in productosBodega if p.nombre == nombre]

                    if len(producto_bodegas) > 0:
                        # El producto ya existe en la bodega, actualiza la cantidad
                        producto_bodega = producto_bodegas[0]
                        producto_bodega.cantidad += cantidad_a_trasladar
                    else:
                        # El producto no existe en la bodega, crea un nuevo registro
                        producto_bodega = Producto(producto_traslado.nombre, producto_traslado.precio, cantidad_a_trasladar, producto_traslado.proveedor)
                        productosBodega.append(producto_bodega)

                    # Actualizar el archivo CSV de productos en la tienda
                    with open("productosTienda.csv", "w", newline="") as archivo_tienda:
                        escritor_tienda = csv.writer(archivo_tienda)
                        escritor_tienda.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                        for producto_tienda in productosTienda:
                            escritor_tienda.writerow([producto_tienda.nombre, producto_tienda.precio, producto_tienda.cantidad, producto_tienda.proveedor])

                    # Actualizar el archivo CSV de productos en la bodega
                    with open("productosBodega.csv", "w", newline="") as archivo_bodega:
                        escritor_bodega = csv.writer(archivo_bodega)
                        escritor_bodega.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                        for producto_bodega in productosBodega:
                            escritor_bodega.writerow([producto_bodega.nombre, producto_bodega.precio, producto_bodega.cantidad, producto_bodega.proveedor])

                    print(f"{cantidad_a_trasladar} unidades del producto trasladadas a la bodega")
                    break
                else:
                    print("La cantidad a trasladar debe ser mayor que 0 y no mayor que la cantidad en existencia en la tienda.")
            except ValueError:
                print("La cantidad ingresada no es válida.")
    else:
        print("Producto no encontrado en la tienda")

    input("Presione enter para continuar")
    return opcion
    
def editar_productoTienda():
    os.system("cls")
    print("Editar Producto en Tienda")
    nombre = input("Ingrese el nombre del producto a editar: ")
    for producto in productosTienda:
        if producto.nombre == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").upper()
            precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            proveedor = input("Ingrese el nuevo proveedor del producto: ").upper()

            producto.nombre = nuevo_nombre
            producto.precio = precio
            producto.cantidad = nueva_cantidad
            producto.proveedor = proveedor

            # Actualizar el archivo CSV de productos en la tienda
            with open("productosTienda.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Precio", "Cantidad", "Proveedor"])
                for producto_tienda in productosTienda:
                    escritor.writerow([producto_tienda.nombre, producto_tienda.precio, producto_tienda.cantidad, producto_tienda.proveedor])

            print("Producto editado en la tienda")
            break
    else:
        print("Producto no encontrado en la tienda")

    input("Presione enter para continuar")

def menu_clientes():
    os.system("cls")
    print("1. Crear Cliente")
    print("2. Eliminar Cliente")
    print("3. Editar Cliente")
    print("4. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def cargar_clientes_desde_archivo():
    try:
        with open("clientes.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            for row in reader:
                nombre, direccion, nit = row
                cliente = Cliente(nombre, direccion, nit)
                clientes.append(cliente)
    except FileNotFoundError:
        # El archivo no existe, lo creamos vacío
        with open("clientes.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Direccion", "NIT"])

def guardar_cliente_en_archivo(cliente):
    with open("clientes.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([cliente.nombre, cliente.direccion, cliente.nit])

def cliente_existente(cliente_nombre):
    for cliente in clientes:
        if cliente.nombre == cliente_nombre:
            return cliente
    return None

def crear_o_cargar_cliente():
    os.system("cls")
    print("Crear o Cargar Cliente")
    nombre = input("Ingrese el nombre completo del cliente: ").upper()
    direccion = input("Ingrese la dirección del cliente: ").upper()
    nit = input("Ingrese el NIT del cliente: ").upper()

    # Verificar si el cliente ya existe
    cliente_exist = cliente_existente(nombre)

    if cliente_exist:
        print(f"El cliente ya existe: {cliente_exist}")
        input("Presione enter para continuar")
    else:
        # Si el cliente no existe, se crea y se guarda en el archivo CSV
        cliente = Cliente(nombre, direccion, nit)
        clientes.append(cliente)
        guardar_cliente_en_archivo(cliente)
        print("Cliente creado exitosamente")
        input("Presione enter para continuar")
        return opcion
    
def eliminar_cliente():
    os.system("cls")
    print("Eliminar Cliente")
    nombre = input("Ingrese el nombre del cliente a eliminar: ").upper()
    for cliente in clientes:
        if cliente.nombre == nombre:
            clientes.remove(cliente)

            # Actualizar el archivo CSV de clientes
            with open("clientes.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Direccion", "NIT"])
                for cliente in clientes:
                    escritor.writerow([cliente.nombre, cliente.direccion, cliente.nit])

            print("Cliente eliminado")
            break
    else:
        print("Cliente no encontrado")

    input("Presione enter para continuar")
    return opcion

def editar_cliente():
    os.system("cls")
    print("Editar Cliente")
    nombre = input("Ingrese el nombre del cliente a editar: ").upper()
    for cliente in clientes:
        if cliente.nombre == nombre:
            nombre = input("Ingrese el nuevo nombre del cliente: ").upper()
            direccion = input("Ingrese la nueva dirección del cliente: ").upper()
            nit = input("Ingrese el nuevo NIT del cliente: ").upper()

            cliente.nombre = nombre
            cliente.direccion = direccion
            cliente.nit = nit

            # Actualizar el archivo CSV de clientes
            with open("clientes.csv", "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre", "Direccion", "NIT"])
                for cliente in clientes:
                    escritor.writerow([cliente.nombre, cliente.direccion, cliente.nit])

            print("Cliente editado")
            break
    else:
        print("Cliente no encontrado")

    input("Presione enter para continuar")
    return opcion

def menu_reportes():
    os.system("cls")
    print("1. Reporte de Productos")
    print("2. Reporte de Clientes")
    print("3. Reporte de Facturas")
    print("4. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def reporte_productos():
    os.system("cls")
    print("Reporte de Productos")

    # Abre el archivo CSV en modo lectura
    with open("productosTienda.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)

        # Lee la primera fila que contiene los encabezados
        encabezados = next(lector)
        tabla = PrettyTable(encabezados) 
        # Lee y muestra los datos de los productos
        for row in lector:
            # Agrega cada fila de datos a la tabla
            tabla.add_row(row)
        # Imprime la tabla
        print(tabla)
    input("Presione enter para regresar al menú")
    return menu_reportes()

def reporte_clientes():
    os.system("cls")
    print("Reporte de Clientes")
    
    # Abre el archivo CSV en modo lectura
    with open("clientes.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)

        # Lee la primera fila que contiene los encabezados
        encabezados = next(lector)

        # Imprime los títulos de las columnas
        print(", ".join(encabezados))

        # Lee y muestra los datos de los clientes
        for row in lector:
            print(", ".join(row))
            
    input("Presione enter para regresar al menú")
    return menu_reportes()

def reporte_facturas():
    os.system("cls")
    print("Reporte de Facturas")
    
    # Abre el archivo CSV en modo lectura
    with open("facturas.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)

        # Lee la primera fila que contiene los encabezados
        encabezados = next(lector)

        # Imprime los títulos de las columnas
        print(", ".join(encabezados))

        # Lee y muestra los datos de las facturas
        for row in lector:
            print(", ".join(row))
            
    input("Presione enter para regresar al menú")
    return menu_reportes()

def menu_venta():
    os.system("cls")
    print("1. Facturar")
    print("2. Anular factura")
    print("3. Salir")
    opcion = int(input("Ingrese la opción: "))
    return opcion

def facturar():
    os.system("cls")

def anular_factura():
    os.system("cls")

cargar_empleados_desde_archivo()
cargar_productosBodega_desde_archivo()
cargar_productosTienda_desde_archivo()

def main():
    opcion = menu()

    while opcion != 4:
        if opcion == 1:  # Administrador
            usuario = input("Ingrese el usuario: ")
            contrasena = getpass.getpass("Ingrese la contraseña: ")
            os.system("cls")
            if usuarios.get(usuario) == contrasena:
                while True:
                    opcion = menu_admin()
                    if opcion == 1:
                        crear_empleado()
                    elif opcion == 2:
                        eliminar_empleado()
                    elif opcion == 3:
                        editar_empleado()
                    elif opcion == 4:
                        reporte_usuarios()
                    elif opcion == 5:
                        break
                    else:
                        print("Opción no válida")
            else:
                print("Usuario o contraseña incorrectos")
            opcion = menu()

        elif opcion == 2:  # Cajero
            while True:
                opcion = menu_cajero()
                if opcion == 1:
                    while True:
                        opcion = menu_productos()
                        if opcion == 1:
                            buscar_producto()
                        elif opcion == 2:
                            trasladar_productoBodega()
                        elif opcion == 3:
                            editar_productoTienda()
                        elif opcion == 4:
                            break
                        else:
                            print("Opción no válida")
                elif opcion == 2:
                    while True:
                        opcion = menu_clientes()
                        if opcion == 1:
                            crear_o_cargar_cliente()
                        elif opcion == 2:
                            eliminar_cliente()
                        elif opcion == 3:
                            editar_cliente()
                        elif opcion == 4:
                            break
                        else:
                            print("Opción no válida")
                elif opcion == 3:
                    while True:
                        opcion = menu_venta()
                        if opcion == 1:
                            facturar()
                        elif opcion == 2:
                            anular_factura()
                        elif opcion == 3:
                            break
                        else:
                            print("Opción no válida")
                elif opcion == 4:
                    while True:
                        opcion = menu_reportes()
                        if opcion == 1:
                            reporte_productos()
                        elif opcion == 2:
                            reporte_clientes()
                        elif opcion == 3:
                            reporte_facturas()
                        elif opcion == 4:
                            break
                        else:
                            print("Opción no válida")
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida")
            opcion = menu()

        elif opcion == 3:  # Bodega
            while True:
                opcion = menu_bodega()
                if opcion == 1:
                    crear_producto()
                elif opcion == 2:
                    eliminar_productoBodega()
                elif opcion == 3:
                    editar_productoBodega()
                elif opcion == 4:
                    trasladar_productoTienda()
                elif opcion == 5:
                    reporte_productos_bodega()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida")
            opcion = menu()

    print("Gracias por usar el sistema de facturación. ¡Hasta luego!")

opcion = main()