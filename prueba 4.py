
compradores_fortificados = []
compradores_iluminados = []




stock = {"fortificados": 500, "iluminados": 500}



def codigovalidadorf(codigo):

    if len(codigo) > 6 or " " in codigo:
        return False
    tiene_mayus = any(c.isupper()for c in codigo)
    tiene_num = any(c.isdigit()for c in codigo)
    return tiene_mayus and tiene_num



def codigovalidadori(codigo):
    if len(codigo) > 5 or " " in codigo:
        return False
    mayusculas = sum(1 for c in codigo if c.isupper())
    tiene_num = any(c.isdigit() for c in codigo)
    return mayusculas >= 3 and tiene_num

def entradaf():
    global stock
    if stock["fortificados"] <= 0:
        print("no queda stock de entradas para fortificados.")
        return
    nombre = input("ingrese nombre del comprador: ")
    if any(comp["nombre"] == nombre for comp in compradores_fortificados):
        print("este nombre esta usado.")
        return
    
    tipo = input("ingrese tipo de entrada. G/V:" )
    if tipo not in ["G", "V"]:
        print("tipo de entrada inválida.")
        return
    codigo = input("ingrese el codigo verificador. este debe tener 6 caracteres, una mayúscula y una letra: ")
    if not codigovalidadorf(codigo):
        print("codigo inválido, debe tener las 3 características.")
        return
    compradores_fortificados.append ({"nombre": nombre, "tipo": tipo, "codigo": codigo})
    stock ["fortificados"] -=1
    print("entrada ingresada correctamente para los fortificados.")



def entradai():
    global stock
    if stock["iluminados"] <= 0:
        print("no queda stock de entradas para iluminados.")
        return
    nombre = input("ingrese nombre del comprador: ")
    if any(comp["nombre"] == nombre for comp in compradores_iluminados):
        print("este nombre esta usado.")
        return
    
    tipo = input("ingrese tipo de entrada. PAL/CV:" )
    if tipo not in ["PAL", "CV"]:
        print("tipo de entrada inválida.")
        return
    codigo = input("ingrese el codigo verificador. este debe tener 5 caracteres, tres mayúsculas y un numero: ")
    if not codigovalidadori(codigo):
        print("codigo inválido, debe tener las 3 características.")
        return
    compradores_iluminados.append ({"nombre": nombre, "tipo": tipo, "codigo": codigo})
    stock ["iluminados"] -=1
    print("entrada ingresada correctamente para los iluminados.")


def vers():
        print("---stock actual---")
        print(f"el stock actual para los fortificados es: {stock["fortificados"]}")
        print(f"el stock actual para los iluminados es:{stock["iluminados"]}")




def menu():
    while True:
        print("---TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE---")
        print("1.- Comprar entrada a “los Fortificados”.")
        print("2.- Comprar entrada a “los Iluminados”.")
        print("3.- Stock de entradas para ambos conciertos.")
        print("4.- Salir.")

        op = input ("que opción desea elegir?: ")

        if op == "1":
            entradaf()
        elif op =="2":
            entradai()
        elif op =="3":
            vers()
        elif op == "4":
            print("---terminando programa---")
            break
        else:
            print("debe ingresar una opción válida.")





menu()


















