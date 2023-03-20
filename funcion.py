#Variables Globales
ARS= 282.81
COL= 4849.99
MEX= 18.74

def vista(): #Esta funcion es la vista global
    print(ingresar_nombre())
    return menu()

def ingresar_nombre(): #Funcion permite ingresar nombre
    nombre=input("Ingresa Tu Nombre: ")
    return f"hola: {nombre} Bienvenodo al conversor de moneda"

def menu(): #Permite elegir el menú de opciones
    print("Seleccione una de las opciones de conversion")
    print("1. Dolares a pesos argentinos")
    print("2. Dolares a pesos colombianos")
    print("3. Dolares a pesos argentinos")
    opcion=int(input("Seleccione la Opcion: "))
    return calcular_moneda(opcion)

def calcular_moneda(opcion): #Realiza la conversion de dolares a pesos.
    if opcion==1:       
        dolares=int(input("Cuantos dolares tiene: "))
        pesos=dolares*ARS
        return F"Tiene: {pesos} argentinos"
    else:
         if opcion==2:
            dolares=int(input("Cuantos dolares tiene:"))
            pesos=dolares*COL
            return F"Tiene: {pesos} colombianos"
         else:
            dolares=int(input("Cuantos dolares tiene:"))
            pesos=dolares*MEX
            return F"Tiene: {pesos} mexicanos"
       
print(vista())

    