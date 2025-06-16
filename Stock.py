


def menu():
    print ("""
    ------------- TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE -------------
    1.- Comprar entrada a “los Fortificados” en Concepción.
    2.- Comprar entrada a “los Fortificados” en Puente Alto. 
    3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.
    4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.
    5.- Salir.
        """) 
# Concepcion 500 entradas 1 letra mayuscula y un numero,  Puente alto 1300 entradas y 3 entradas por persona
# Muelle baron entrada tipo G y 100 entradas, Viña tipo de entradad Sun o Ni y 50 entradas
    
def ValNombre (Nombre,Lis_Compr):
    for Comp in Lis_Compr:
        if Comp == Nombre:
            return False 
        return True

# Codigos de entrada 
def ValTipEntMuelleBaron(tipo):
    return tipo == "G" or tipo == "V"

def ValTipEntVinha(tipo):
    return tipo == "Sun" or tipo == "Ni"

def ValTipEntConce(tipo):
    return tipo == "CONCEP1"

# Validar Codigos
def ValCodConfMuelleBar(Cod):
    if len (Cod) < 6:
        return False
    if "" in Cod:
        return False
    Mayusculas = False
    Numero = False
    for c in Cod:
        if "A" <= c <= "Z":
            Mayusculas = True
        if "0" <= c <= "9":
            Numero = True
            return Mayusculas and Numero

def ValCodConConce(Cod):
    if len (Cod)< 7:
        return False 
    if "" in Cod:
        return False
    Mayusculas = 0
    Numero = False
    for c in Cod:
        if "A" <= c <= "Z":
            Mayusculas += 1
        if  "0" <= c <= "9":
            Numero = True
            return Mayusculas >= 5 and Numero

def ValCodConVinha(Cod):
    if len (Cod) < 4:
        return False
    if "" in Cod:
        return False
    Mayusculas = 0
    Numero = False
    for c in Cod:
        if "A" <= c <= "Z":
            Mayusculas += 1
        if  "0" <= c <= "9":
            Numero = True
            return Mayusculas and Numero
        
# Entradas

def CompEntMuelleBar(Compradores_f, Entradas_f,StockToc):
    Nombre = input ("Nombre: ").strip()
    if not ValNombre(Nombre, Compradores_f):
        print ("ERROR | Nombre ya registrado")
        return Entradas_f,StockToc
    tipo = input ("Ingrese tipo de entrada (Solo disponible G): ")
    if not ValCodConfMuelleBar(tipo):
        print ("ERROR | Tipo de entrada no valido")
        return Entradas_f, StockToc
    Cod = input ("Ingrese codigo de confirmacion: ")
    if not ValCodConfMuelleBar(Cod):
        print ("ERROR | Codigo de confirmacion invalido")
        return Entradas_f, StockToc
    if StockToc <= 0:
        print ("No hay Stock disponible")
        return Entradas_f, StockToc
    
    # Registro Exitoso 
    Compradores_f.append(Nombre)
    Entradas_f.append({"Nombre":Nombre, "tipo":tipo, "Codigo":Cod })
    StockToc -= 1
    print ("Compra exitosa")
    return Entradas_f,StockToc

def ComEntConce(Compradores_c, Entradas_c,StockToc):
    Nombre = input ("Nombre: ").strip()
    if not ValNombre(Nombre, Compradores_c):
        print ("ERROR | Nombre ya registrado")
        return Entradas_c,StockToc
    Cod = input ("Ingrese codigo de confirmacion: ")
    if not ValCodConfMuelleBar(Cod):
        print ("ERROR | Codigo de confirmacion invalido")
        return Entradas_c, StockToc
    if StockToc <= 0:
        print ("No hay Stock disponible")
        return Entradas_c, StockToc
    
    # Registro Exitoso 
    Compradores_c.append(Nombre)
    Entradas_c.append({"Nombre":Nombre,"Codigo":Cod })
    StockToc -= 1
    print ("Compra exitosa")
    return Entradas_c,StockToc


def CompEntVinha(Compradores_v, Entradas_v,StockToc):
    Nombre = input ("Nombre: ").strip()
    if not ValNombre(Nombre, Compradores_v):
        print ("ERROR | Nombre ya registrado")
        return Entradas_v,StockToc
    tipo = input ("Ingrese tipo de entrada (Sun y Ni): ")
    if not ValCodConfMuelleBar(tipo):
        print ("ERROR | Tipo de entrada no valido")
        return Entradas_v, StockToc
    Cod = input ("Ingrese codigo de confirmacion: ")
    if not ValCodConfMuelleBar(Cod):
        print ("ERROR | Codigo de confirmacion invalido")
        return Entradas_v, StockToc
    if StockToc <= 0:
        print ("No hay Stock disponible")
        return Entradas_v, StockToc
    
    # Registro Exitoso 
    Compradores_v.append(Nombre)
    Entradas_v.append({"Nombre":Nombre, "tipo":tipo, "Codigo":Cod })
    StockToc -= 1
    print ("Compra exitosa")
    return Entradas_v,StockToc

def MostStock(entradas_f,entradas_v,entradas_c, StockToc):
    print ("\n Entradas compradas para 'Los Fortificados':")
    if entradas_f:
        for e in entradas_f:
            print (f"Nombre:  {e['Nombre']}, Tipo {e["tipo"]}, Codigo: {e["Cod"]} ")
        else:
            print ("No hay entradas vendidas para este concierto")
    
    
    if entradas_v:
        for e in entradas_v:
            print (f"Nombre:  {e['Nombre']}, Tipo {e["tipo"]}, Codigo: {e["Cod"]} ")
        else:
            print ("No hay entradas vendidas para este concierto")

        
        print (f"\n Stock disponible para ambos conciertos: {StockToc} entradas")

    if entradas_c:
        for e in entradas_c:
            print (f"Nombre:  {e['Nombre']}, Tipo {e["tipo"]}, Codigo: {e["Cod"]} ")
        else:
            print ("No hay entradas vendidas para este concierto")
        
        print (f"\n Stock disponible para ambos conciertos: {StockToc} entradas")

def main():
    Compradores_f = []
    Compradores_c = []
    Compradores_v = []
    Entradas_f = []
    Entradas_c = []
    Entradas_v = []
    while True:
        menu()
        Opc = input ("Opcion: ")
        if Opc == 1: 
            Entradas_c, StockToc = ComEntConce(Compradores_f,Entradas_f,StockToc)
        if Opc == 3: 
            Entradas_m, StockToc = CompEntMuelleBar(Compradores_f,Entradas_f,StockToc)
        if Opc == 4: 
            Entradas_f, StockToc = CompEntMuelleBar(Compradores_f,Entradas_f,StockToc)

        if __name__=="__main__":
            main()