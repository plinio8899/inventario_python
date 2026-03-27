inventario = []

def agregar():
    try:
        nombre = input("Nombre del producto -> ")
        precio = int(input("Precio del producto -> "))
        cantidad = int(input("Cantidad del producto -> "))
        inventario.append({
            "Nombre" : nombre,
            "Precio" : precio,
            "Cantidad" : cantidad
        })
    except:
        print("Ha ocurrido un error al agregar el producto")

def mostrar():
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        for item in inventario:
            print(item)

def estadisticas():
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        precio_total = 0
        cantidad_total = 0
        for item in inventario:
            precio_total += item["Precio"] * item["Cantidad"]
            cantidad_total += item["Cantidad"]
        print(f"El valor total del inventario es de {precio_total}")
        print(f"La cantidad total de articulos en inventario es de {cantidad_total}")

        


