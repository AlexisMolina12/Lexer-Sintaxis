ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_sentencia(lexema):
    estado = 0
    estados_finales = [1,2,3]
    delta = {
            0:{'<':2, '>':1, '=':1},
            1: {'=':3,},
            2: {'>':3,'=':3},
            3: {},     
    }        
    for caracter in lexema:
        if caracter in delta[estado]:
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
