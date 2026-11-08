import almacen
# Buscar productos
while True:
   print("1. Buscar productos en el almacén")
   print("2. Vender articulo")
   print("3. Agregar articulo")
   print("4. salir")

   opcion = input("Ingrese una opción: ")
   if opcion == "1":
      buscar = input("Ingrese el nombre del producto a buscar: ")
      if buscar in almacen.inventario:
         print(f"El producto {buscar} se encuentra en el inventario.")
         print(f"En total de unidades son: {almacen.strock[buscar]}") # busca la cantidad de unidades del producto
         input("Presione Enter para continuar...")
      else:
         print(f"El producto {buscar} no se encuentra en el inventario.")
         repuesta = input("¿Desea agregarlo al inventario? (s/n): ")
         if repuesta == "s":
            almacen.inventario.append(buscar)
            print(f"El producto {buscar} ha sido agregado al inventario.")
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
         print(f"Se han agregado {cantidad} unidades de {agregar}.")
         print(f"Ahora hay {almacen.strock[agregar]} unidades de {agregar}.")
         input("Presione Enter para continuar...")
      else: 
         print(f"El producto {agregar} no se encuentra en el inventario.")
         repuesta = input("¿Desea agregarlo al inventario? (s/n): ")
         if repuesta == "s":
            almacen.inventario.append(agregar)
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            almacen.strock[agregar] = cantidad
            print(f"El producto {agregar} ha sido agregado al inventario con {cantidad} unidades.")
            input("Presione Enter para continuar...")
         else:
            print("No se ha agregado el producto al inventario.")
            input("Presione Enter para continuar...")         
      
        
      


