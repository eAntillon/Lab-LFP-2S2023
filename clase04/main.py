# ubicacion = {
#     "bodegaA": {
#         "ProductoA": {
#             "Cantidad": 0,
#             "Precio": 10
#         },
#         "ProductoB": {
#             "Cantidad": 0,
#             "Precio": 10
#         }
#     },
#     "bodegab": {
#         "ProductoA": {
#             "Cantidad": 0,
#             "Precio": 10
#         }
#     }
# }


ubicaciones = {}

# cargar inventario
with open("inventario.inv", encoding="utf-8") as file:
    for linea in file:
        producto, cantidad, precio, ubicacion = linea.strip().split(" ")[1].split(";")
        if ubicacion in ubicaciones:
            ubicaciones[ubicacion][producto] = {
                "cantidad": float(cantidad),
                "precio": float(precio),
            }
        else:
            ubicaciones[ubicacion] = {
                producto: {"cantidad": float(cantidad), "precio": float(precio)}
            }

# cargar movimientos

with open("movimientos.mov", encoding="utf-8") as file:
    for linea in file:
        # ["vender_producto","Plátanos;5;BodegaC"]
        instrucion, informacion =  linea.strip().split(" ")
        # ["Plátanos", "5", "BodegaC"]
        producto, cantidad, ubicacion = informacion.split(";")
        
        if instrucion == "agregar_stock": 
            if ubicacion not in ubicaciones:
                print("Esa ubicacion no existe")
                continue
            if producto not in ubicaciones[ubicacion]:
                print("Ese producto no existe ahi")
                continue
            ubicaciones[ubicacion][producto]['cantidad'] += float(cantidad)
        elif instrucion == "vender_producto":
            if ubicacion not in ubicaciones:
                print("Esa ubicacion no existe")
                continue
            if producto not in ubicaciones[ubicacion]:
                print("Ese producto no existe ahi")
                continue
            ubicaciones[ubicacion][producto]['cantidad'] -= float(cantidad)
        else: 
            print("Error")


print(ubicaciones)

with open("resultado.txt", "w", encoding="utf-8") as file:
    for key, value in ubicaciones.items():
        file.write("ubicacion:" + key + "\n")
        for nombre, valores in value.items():
            file.write(nombre + " "+ str(valores["cantidad"]*valores["precio"])) 
            file.write("\n")

