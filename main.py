import almacen
#achirvo txt para guardar el inventario
try:
    with open("inventario.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo.read().splitlines():
            nombre, separador, unidades = linea.partition("|")
            nombre = nombre.strip()
            if not nombre:
                continue
            if nombre not in almacen.inventario:
                almacen.inventario.append(nombre)
            if separador:
                try:
                    almacen.strock[nombre] = int(unidades.strip())
                except ValueError:
                    almacen.strock[nombre] = 0
except FileNotFoundError:
    # Si el archivo aún no existe, se queda con lo que tenga o vacío
    pass

# Los productos antiguos del TXT pueden no tener cantidad guardada.
for producto in almacen.inventario:
    almacen.strock.setdefault(producto, 0)

try:
    with open("precios.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo.read().splitlines():
            nombre, separador, precio = linea.partition("|")
            nombre = nombre.strip()
            if nombre and separador:
                try:
                    almacen.precios[nombre] = float(precio.strip())
                except ValueError:
                    print(f"Precio inválido para {nombre}: {precio}")
except FileNotFoundError:
    pass

def guardar_inventario():
    with open("inventario.txt", "w", encoding="utf-8") as archivo:
        for producto in almacen.inventario:
            archivo.write(f"{producto}|{almacen.strock[producto]}\n")
def guardar_precios():
    with open("precios.txt", "w", encoding="utf-8") as archivo:
        for producto in almacen.precios:
            precio = almacen.precios[producto]
            archivo.write(f"{producto}|{precio}\n")

# Buscar productos
while True:
   print("1. Buscar productos en el almacén")
   print("2. Vender articulo")
   print("3. Agregar articulo")
   print("4. poner precio a un producto")
   print("5. ver precio de un producto")
   print("6. salir")

   opcion = input("Ingrese una opción: ")
   if opcion == "1":
      buscar = input("Ingrese el nombre del producto a buscar: ").strip()
      if buscar in almacen.inventario:
         print(f"El producto {buscar} se encuentra en el inventario.")
         print(f"En total de unidades son: {almacen.strock[buscar]}")
         input("Presione Enter para continuar...")
      else:
         print(f"El producto {buscar} no se encuentra en el inventario.")
         repuesta = input("¿Desea agregarlo al inventario? (s/n): ")
         if repuesta == "s":
            almacen.inventario.append(buscar)
            almacen.strock[buscar] = 0
            print(f"El producto {buscar} ha sido agregado al inventario.")
            guardar_inventario()
            input("Presione Enter para continuar...")
         else:
            print("No se ha agregado el producto al inventario.")
            input("Presione Enter para continuar...")

   elif opcion == "2":
      vender = input("Ingrese el nombre del producto a vender: ")
      if vender in almacen.strock:
         cantidad = int(input("Ingrese la cantidad a vender: "))
         if cantidad <= almacen.strock[vender]:
            almacen.strock[vender] -= cantidad
            guardar_inventario()
            print(f"Se han vendido {cantidad} unidades de {vender}.") # Aqui vende el producto y resta la cantidad en el strock
            print(f"Quedan {almacen.strock[vender]}") # Aqui muestra la cantidad de unidades que quedan del producto
            input("Presione Enter para continuar...")
         else: 
            print(f"No hay suficiente stock de {vender}. Solo quedan {almacen.strock[vender]} unidades.")
            input("Presione Enter para continuar...")
   elif opcion == "3":
      agregar = input("Ingrese el nombre del producto a agregar: ")
      if agregar in almacen.strock:
         cantidad = int(input("Ingrese la cantidad a agregar: "))
         almacen.strock[agregar] += cantidad
         guardar_inventario()
         print(f"Se han agregado {cantidad} unidades de {agregar}.")
         print(f"Ahora hay {almacen.strock[agregar]} unidades de {agregar}.")
         input("Presione Enter para continuar...")
      else: 
         print(f"El producto {agregar} no se encuentra en el inventario.")
         repuesta = input("¿Desea agregarlo al inventario? (s/n): ")
         if repuesta == "s":
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            almacen.inventario.append(agregar)
            almacen.strock[agregar] = cantidad
            guardar_inventario()
            print(f"El producto {agregar} ha sido agregado al inventario con {cantidad} unidades.")
            input("Presione Enter para continuar...")
         else:
            print("No se ha agregado el producto al inventario.")
            input("Presione Enter para continuar...")         
   elif opcion == "4":
      producto = input("Ingrese el nombre del producto al que desea ponerle precio: ").strip()
      if producto in almacen.inventario:
         precio = float(input("Ingrese el precio del producto: "))
         almacen.precios[producto] = precio
         guardar_precios()
         print(f"El precio del producto {producto} ha sido actualizado a {precio}.")
         input("Presione Enter para continuar...")
      else:
         print(f"El producto {producto} no se encuentra en el inventario.")
         input("Presione Enter para continuar...")
   elif opcion == "5":
      producto = input("Ingrese el nombre del producto para ver su precio: ").strip()
      if producto in almacen.precios:
         precio = almacen.precios[producto]
         print(f"El precio del producto {producto} es: {precio}")
         input("Presione Enter para continuar...")
      else:
         print(f"El producto {producto} no tiene un precio asignado.")
         respuesta = input("¿Desea asignarle un precio? (s/n): ")
         if respuesta == "s":
             precio = float(input("Ingrese el precio del producto: "))
             almacen.precios[producto] = precio
             guardar_precios()
             print(f"El precio del producto {producto} a sido asignado a {precio}.")
             input("Presione Enter para continuar...")
         else:
             print("No se ha asignado un precio al producto.")
             input("Presione Enter para continuar...")
       
        
      
