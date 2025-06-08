ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_program(lexema):
    estado = 0
    estados_finales = [7]
    delta = {0:{'p':1},1:{'r':2},2:{'o':3},3:{'g':4},4:{'r':5},5:{'a':6},6:{'m':7},7:{}}
        
    for caracter in lexema:
        if caracter in delta[estado].keys():
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
    
    