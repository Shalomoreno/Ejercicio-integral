print("-----Ejercicio integral: Sistema de ventas para una librería escolar-----")
inventario=("Útiles escolares", "Lectura", "Arte", "Tecnología")
print(f"Las categorías de productos disponibles son:{inventario}")

print("PARA UTILES ESCOLARES INGRESAR:")

UEp1=input("Ingrese el nombre del producto 1: ")
UEpu1=float(input(f"Ingrese el precio unitario del producto {UEp1} :"))
UEcp1=int(input(f"Ingrese la cantidad de productos del {UEp1}: "))
UEv1=UEpu1*UEcp1
print(f"El valor total del producto es: {UEv1}")

UEp2=input("Ingrese el nombre del producto 2: ")
UEpu2=float(input(f"Ingrese el precio unitario del producto {UEp2}: "))
UEcp2=int(input(f"Ingrese la cantidad de productos del {UEp2}: "))
UEv2=UEpu2*UEcp2
print(f"El valor total del producto es: {UEv2}")

utiles_escolares = {
    "Producto 1": {"Nombre": UEp1, "Precio Unitario": UEpu1, "Cantidad": UEcp1, "Valor Total": UEv1},
    "Producto 2": {"Nombre": UEp2, "Precio Unitario": UEpu2, "Cantidad": UEcp2, "Valor Total": UEv2}
}

print("PARA LECTURA INGRESAR:")
LEp1=input("Ingrese el nombre del libro 1: ")
LEpu1=float(input(f"Ingrese el precio unitario del libro  {LEp1}: "))
LEcp1=int(input(f"Ingrese la cantidad de libros del {LEp1}: "))
LEv1=LEpu1*LEcp1
print(f"El valor total del libro es: {LEv1}")

LEp2=input("Ingrese el nombre del libro 2: ")
LEpu2=float(input(f"Ingrese el precio unitario del libro {LEp2}: "))
LEcp2=int(input(f"Ingrese la cantidad de libros del {LEp2}: "))
LEv2=LEpu2*LEcp2
print(f"El valor total del libro es: {LEv2}")

lectura = {
    "Libro 1": {"Nombre": LEp1, "Precio Unitario": LEpu1, "Cantidad": LEcp1, "Valor Total": LEv1},
    "Libro 2": {"Nombre": LEp2, "Precio Unitario": LEpu2, "Cantidad": LEcp2, "Valor Total": LEv2}
}

print("PARA ARTE INGRESAR:")
AEp1=input("Ingrese el nombre del producto 1: ")
AEpu1=float(input(f"Ingrese el precio unitario del producto  {AEp1} :"))
AEcp1=int(input(f"Ingrese la cantidad de productos del {AEp1} :"))
AEv1=AEpu1*AEcp1
print(f"El valor total del producto es: {AEv1}")

AEp2=input("Ingrese el nombre del producto 2: ")
AEpu2=float(input(f"Ingrese el precio unitario del producto {AEp2} :"))
AEcp2=int(input(f"Ingrese la cantidad de productos del {AEp2} :"))
AEv2=AEpu2*AEcp2
print(f"El valor total del producto es: {AEv2}")

arte = {
    "Producto 1": {"Nombre": AEp1, "Precio Unitario": AEpu1, "Cantidad": AEcp1, "Valor Total": AEv1},
    "Producto 2": {"Nombre": AEp2, "Precio Unitario": AEpu2, "Cantidad": AEcp2, "Valor Total": AEv2}
}

print("PARA TECNOLOGÍA INGRESAR:")
TEp1=input("Ingrese el nombre del producto 1: ")
TEpu1=float(input(f"Ingrese el precio unitario del producto {TEp1} :"))
TEcp1=int(input(f"Ingrese la cantidad de productos del {TEp1} :"))
TEv1=TEpu1*TEcp1
print(f"El valor total del producto es: {TEv1}")

TEp2=input("Ingrese el nombre del producto 2: ")
TEpu2=float(input(f"Ingrese el precio unitario del producto {TEp2} :"))
TEcp2=int(input(f"Ingrese la cantidad de productos del {TEp2} :"))
TEv2=TEpu2*TEcp2
print(f"El valor total del producto es: {TEv2}")

tecnologia = {
    "Producto 1": {"Nombre": TEp1, "Precio Unitario": TEpu1, "Cantidad": TEcp1, "Valor Total": TEv1},
    "Producto 2": {"Nombre": TEp2, "Precio Unitario": TEpu2, "Cantidad": TEcp2, "Valor Total": TEv2}
}


np=input("Desea ingresar un nuevo producto? : ")

if np.lower() == "si":
    sc=input("Ingrese la categoría del producto: ")
    sn=input("Ingrese el nombre del producto: ")
    spu=float(input(f"Ingrese el precio unitario del producto {sn} :"))
    scp=int(input(f"Ingrese la cantidad de productos del {sn} :"))
    svf=spu*scp
    print(f"El valor total del producto {sn} es: {svf}")
    if sc.lower() == "utiles escolares":
        utiles_escolares[sn] = {"Nombre": sn, "Precio Unitario": spu, "Cantidad": scp, "Valor Total": svf}
    elif sc.lower() == "lectura":
        lectura[sn] = {"Nombre": sn, "Precio Unitario": spu, "Cantidad": scp, "Valor Total": svf}
    elif sc.lower() == "arte":
        arte[sn] = {"Nombre": sn, "Precio Unitario": spu, "Cantidad": scp, "Valor Total": svf}
    elif sc.lower() == "tecnología":
        tecnologia[sn] = {"Nombre": sn, "Precio Unitario": spu, "Cantidad": scp, "Valor Total": svf}
    else:
        print("Categoría no válida")
    
else:
    print("No se ingresó un nuevo producto.")
    
mp=input("Desea modificar un producto? : ")
if mp.lower() == "si":
    mc=input("Ingrese la categoría del producto a modificar: ")
    mn=input("Ingrese el nombre del producto a modificar: ")
    if mc.lower() == "utiles escolares":
        if mn in utiles_escolares:
            mpu=float(input(f"Ingrese el nuevo precio unitario del producto {mn}: "))
            mcp=int(input(f"Ingrese la nueva cantidad de productos del {mn}: "))
            mvf=mpu*mcp
            utiles_escolares[mn] = {"Nombre": mn, "Precio Unitario": mpu, "Cantidad": mcp, "Valor Total": mvf}
        else:
            print("Producto no encontrado en útiles escolares.")
    elif mc.lower() == "lectura":
        if mn in lectura:
            mpu=float(input(f"Ingrese el nuevo precio unitario del libro {mn}: "))
            mcp=int(input(f"Ingrese la nueva cantidad de libros del {mn}: "))
            mvf=mpu*mcp
            lectura[mn] = {"Nombre": mn, "Precio Unitario": mpu, "Cantidad": mcp, "Valor Total": mvf}
        else:
            print("Libro no encontrado en lectura.")
    elif mc.lower() == "arte":
        if mn in arte:
            mpu=float(input(f"Ingrese el nuevo precio unitario del producto {mn}: "))
            mcp=int(input(f"Ingrese la nueva cantidad de productos del {mn}: "))
            mvf=mpu*mcp
            arte[mn] = {"Nombre": mn, "Precio Unitario": mpu, "Cantidad": mcp, "Valor Total": mvf}
        else:
            print("Producto no encontrado en arte.")
    elif mc.lower() == "tecnología":
        if mn in tecnologia:
            mpu=float(input(f"Ingrese el nuevo precio unitario del producto {mn}: "))
            mcp=int(input(f"Ingrese la nueva cantidad de productos del {mn}: "))
            mvf=mpu*mcp
            tecnologia[mn] = {"Nombre": mn, "Precio Unitario": mpu, "Cantidad": mcp, "Valor Total": mvf}
        else:
            print("Producto no encontrado en tecnología.")
    else:
        print("Categoría no válida")
else:
    print("No se modificó ningún producto.")

"""total venta"""
total_venta= lectura["Libro 1"]["Valor Total"] + lectura["Libro 2"]["Valor Total"] + utiles_escolares["Producto 1"]["Valor Total"] + utiles_escolares["Producto 2"]["Valor Total"] + arte["Producto 1"]["Valor Total"] + arte["Producto 2"]["Valor Total"] + tecnologia["Producto 1"]["Valor Total"] + tecnologia["Producto 2"]["Valor Total"]

print(f"El total de la venta es: {total_venta}")
    
print(f"para productos escolares {utiles_escolares},\n para lectura {lectura}, \n para arte {arte} \n y para tecnologia {tecnologia}")