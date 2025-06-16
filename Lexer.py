#Importamos los automatas
from Automatas.aand import *
from Automatas.begin import *
from Automatas.bool import *
from Automatas.dos_puntos_igual import *
from Automatas.eelse import *
from Automatas.end import *
from Automatas.false import *
from Automatas.id import *
from Automatas.iif import *
from Automatas.sentencia import *
from Automatas.int import *
from Automatas.multiplicacion import *
from Automatas.nnot import *
from Automatas.num import *
from Automatas.oor import *
from Automatas.parentesisA import *
from Automatas.parentesisB import *
from Automatas.punto_y_coma import *
from Automatas.punto import *
from Automatas.suma_resta import *
from Automatas.trespuntos import *
from Automatas.true import *
from Automatas.var import *

ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"
ESTADOS_POSIBLES = [('TOKEN_AND',automata_and), 
                   ('TOKEN_BEGIN',automata_begin), 
                   ('TOKEN_BOOL',automata_bool),
                   ('TOKEN_DOS_PUNTOS_IGUAL',automata_dosPuntosIgual),
                   ('TOKEN_ELSE',automata_else),
                   ('TOKEN_END',automata_end),
                   ('TOKEN_FALSE',automata_false),
                   ('TOKEN_ID',automata_id),
                   ('TOKEN_IF',automata_if),
                   ('TOKEN_IGUAL',automata_sentencia),
                   ('TOKEN_INT',automata_int),
                   ('TOKEN_MULTIPLICACION',automata_multiplicacion),
                   ('TOKEN_NOT',automata_not),
                   ('TOKEN_NUM',automata_num),
                   ('TOKEN_OR',automata_or),
                   ('TOKEN_PARENTESIS_A',automata_parentesisA),
                   ('TOKEN_PARENTESIS_B',automata_parentesisB),
                   ('TOKEN_PUNTO_Y_COMA',automata_puntoYcoma),
                   ('TOKEN_PUNTO',automata_punto),
                   ('TOKEN_SUMA_RESTA',automata_sumaresta),
                   ('TOKEN_TRES_PUNTOS',automata_trespuntos),
                   ('TOKEN_TRUE',automata_true),
                   ('TOKEN_VAR',automata_var),
                   ]

def lexer(codigo_fuente):
    tokens = [] # listado de tokens que devolvera el lexer correspondiente al cod.fuente ingresado
    pos_actual = 0 # posicion actual del lexema
    while pos_actual < len(codigo_fuente):
        comienzo_lexema = pos_actual # el siguiente lexema comienza en la posicion actual
        posibles_tokens = [] # listado de tokens posibles que se pueden formar a partir del lexema
        posibles_token_mas_caracter = [] #categorias de tokens que se pueden formar a partir del lexema mas un caracter
        lexema = ""
        var_aux_estado_trampa = False

        while not var_aux_estado_trampa:
            var_aux_estado_trampa = True
            final_lexema = lexema
            lexema = codigo_fuente[comienzo_lexema:pos_actual+1] # lexema es el codigo fuente desde el comienzo del lexema hasta la posicion actual
            posibles_tokens = posibles_token_mas_caracter
            posibles_token_mas_caracter = []
        
        if final_lexema != lexema:
            for (un_token, automata) in ESTADOS_POSIBLES:
                simulacion_automata = automata(lexema)
                if simulacion_automata == ESTADO_FINAL:
                    posibles_tokens.append(un_token)
                    var_aux_estado_trampa = False
                elif simulacion_automata == ESTADO_NO_FINAL:
                    var_aux_estado_trampa = False
            pos_actual = codigo_fuente[comienzo_lexema:pos_actual-1]
        
        lexema = codigo_fuente[comienzo_lexema:pos_actual-1]


    if len(posibles_tokens) == 0:
        raise Exception("ERROR: TOKEN NO CONOCIDO: " + lexema)
    
    if posibles_tokens[0] != 'TOKEN_ESPACIO':
        un_token = posibles_tokens[0] #mientras que el lexema tenga la posibilidad de avanzar, ya sea si esta en un estado final o no, 
                                      #el algoritmo va a seguir avanzando, entonces va a devolver el lexema mas largo que coincide con un token

        token = (un_token, lexema) #creamos el token con el nombre del token y el lexema
        tokens.append(token)

    pos_actual = comienzo_lexema + len(lexema) #actualizamos la posicion actual del lexema
    return tokens #devolvemos el listado de tokens

print(lexer('()()()()'))
                                      
                    


