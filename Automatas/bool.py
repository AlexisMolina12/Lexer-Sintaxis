ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_bool(lexema):
    estado = 0
    estados_finales = [4]
    delta = {0:{'b':1},1:{'o':2},2:{'o':3},3:{'l':4},4:{}}#Diccionario de diccionarios: Diccionario estados -> Diccionario caracteres
                                                            #solo muestra las transiciones para llegar al estado aceptado
    for caracter in lexema:
        if caracter in delta[estado].keys(): #Dada la entrada caracter, si tiene transiciones que pueden terminar en estados aceptados,es true
            estado = delta[estado][caracter] #movemos el automata al siguiente estado
        else:
            estado = -1 #esto seeria como mover el automata a un estado trampa
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
    