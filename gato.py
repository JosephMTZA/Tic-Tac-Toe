"""
def choose():
    f = int(input("Seleccione ficha: 0 = o, 1 = x: "))
    if (f == 0):
        return "O"
    elif (f == 1):
        return "x" 
    while(f != 0 or f!= 1):
        f = int(input("Seleccione ficha: 0 = o, 1 = x: "))
        if (f == 0):
            return "o"
        elif (f == 1):
            return "x"
"""

def show_matrix():
    for row in matriz:
        for val in row:
            print("|",val, end=" ")
        print("|")
    
#show_matrix()

def input_user(jugador):
    h,v = map(int,input(("Jugador:", jugador,"Inserte un valor horizontal (0-2) y uno vertical(0-2): ")).strip().split())
    while (h < 0 or h > 2 or v < 0 or v > 2):
        h,v = map(int,input("Rangos invalidos. Ingrese valores validos: ").strip().split())
    return h, v
#h,v = input_user()

def occupied_space(h,v):
    if (matriz[h][v] == "x" or matriz[h][v] == "o"):
        return True
    else:
        return False

def insert_into_matrix(h,v,jugador):
    if (occupied_space(h,v)):
        print("Espacio ocupado. Inserte otras posiciones: ")
        h,v = input_user(jugador)
        while(occupied_space(h,v)):
            print("Espacio ocupado. Inserte otras posiciones: ")
            h,v = input_user(jugador)
        matriz[h][v] = jugador
    else:
        matriz[h][v] = jugador

def win(jugador, i):
    #posibles combinaciones por renglon para el jugador 
    if (matriz[0][0] == jugador and matriz[0][1] == jugador and matriz[0][2] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    elif (matriz[1][0] == jugador and matriz[1][1] == jugador and matriz[1][2] == jugador ):
        print("gana el jugador: ", jugador)
        return True
    elif (matriz[2][0] == jugador and matriz[2][1] == jugador and matriz[2][2] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    
    #posibles combinaciones por columna para el jugador 
    elif (matriz[0][0] == jugador and matriz[1][0] == jugador and matriz[2][0] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    elif (matriz[0][1] == jugador and matriz[1][1] == jugador and matriz[2][1] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    elif (matriz[0][2] == jugador and matriz[1][2] == jugador and matriz[2][2] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    

    #posibles combinaciones en diagonal para el jugador
    elif (matriz[0][0] == jugador and matriz[1][1] == jugador and matriz[2][2] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    elif (matriz[0][2] == jugador and matriz[1][1] == jugador and matriz[2][0] == jugador ):
        print("gana el jugador: ",jugador)
        return True
    elif(i == 9):
        print("empate")
        return True
matriz = [[" "," "," "],[" "," "," "],[" "," "," "]]
i = 0

while(True):
    jugador = "x"
    #jugador1 = "o"
    show_matrix()
    h,v = input_user(jugador)
    insert_into_matrix(h, v, jugador)
    i += 1
    if(win(jugador,i)):
        show_matrix()
        break

    jugador = "o"
    show_matrix()
    h,v = input_user(jugador)
    insert_into_matrix(h, v, jugador)
    i += 1
    if(win(jugador,i)):
        show_matrix()
        break