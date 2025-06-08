ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_sentencia(lexema):
    estado = 0
    estados_finales = [1,2]
    delta = {
            0:{'<':2, '>':1, '=':1},
            1: {'=':4},
            2: {'>':3},
            3: {'=':4},
            4:{}             
    }        
    for caracter in lexema:
        if caracter in delta and estado in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
    