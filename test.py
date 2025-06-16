from Lexer import*



entrada1 = "()();"
esperado1 = [
    ('TOKEN_PARENTESIS_A', '('),
    ('TOKEN_PARENTESIS_B', ')'),
    ('TOKEN_PARENTESIS_A', '('),
    ('TOKEN_PARENTESIS_B', ')'),
    ('TOKEN_PUNTO_Y_COMA', ';')
]

entrada2 = "if then else end"
esperado2 = [
    ('TOKEN_IF', 'if'),
    ('TOKEN_ID', 'then'),  # Suponiendo que "then" no es palabra reservada en tu AFD
    ('TOKEN_ELSE', 'else'),
    ('TOKEN_END', 'end')
]

entrada3 = "< <= > >= = == <>"
esperado3 = [
    ('TOKEN_IGUAL', '<'),
    ('TOKEN_IGUAL', '<='),
    ('TOKEN_IGUAL', '>'),
    ('TOKEN_IGUAL', '>='),
    ('TOKEN_IGUAL', '='),
    ('TOKEN_IGUAL', '=='),
    ('TOKEN_IGUAL', '<>')
]

entrada4 = "+ - *"
esperado4 = [
    ('TOKEN_SUMA_RESTA', '+'),
    ('TOKEN_SUMA_RESTA', '-'),
    ('TOKEN_MULTIPLICACION', '*')
]

entrada5 = "true false"
esperado5 = [
    ('TOKEN_TRUE', 'true'),
    ('TOKEN_FALSE', 'false')
]

entrada6 = "and or not"
esperado6 = [
    ('TOKEN_AND', 'and'),
    ('TOKEN_OR', 'or'),
    ('TOKEN_NOT', 'not')
]

entrada7 = "var x y1 abc123"
esperado7 = [
    ('TOKEN_VAR', 'var'),
    ('TOKEN_ID', 'x'),
    ('TOKEN_ID', 'y1'),
    ('TOKEN_ID', 'abc123')
]

entrada8 = "123 0 45678"
esperado8 = [
    ('TOKEN_NUM', '123'),
    ('TOKEN_NUM', '0'),
    ('TOKEN_NUM', '45678')
]

entrada9 = "begin var x; x := 5; end"
esperado9 = [
    ('TOKEN_BEGIN', 'begin'),
    ('TOKEN_VAR', 'var'),
    ('TOKEN_ID', 'x'),
    ('TOKEN_PUNTO_Y_COMA', ';'),
    ('TOKEN_ID', 'x'),
    ('TOKEN_DOS_PUNTOS_IGUAL', ':='),
    ('TOKEN_NUM', '5'),
    ('TOKEN_PUNTO_Y_COMA', ';'),
    ('TOKEN_END', 'end')
]

entrada10 = "@"
esperado10 = "ERROR: TOKEN NO CONOCIDO: @"

tests = [
    (entrada1, esperado1),
    (entrada2, esperado2),
    (entrada3, esperado3),
    (entrada4, esperado4),
    (entrada5, esperado5),
    (entrada6, esperado6),
    (entrada7, esperado7),
    (entrada8, esperado8),
    (entrada9, esperado9),
    (entrada10, esperado10)
]

for i, (entrada, esperado) in enumerate(tests, 1):
    try:
        resultado = lexer(entrada)
        if resultado == esperado:
            print(f"Test {i}: OK")
        else:
            print(f"Test {i}: ERROR")
            print(f"Esperado: {esperado}")
            print(f"Obtenido: {resultado}")
    except Exception as e:
        if isinstance(esperado, str) and esperado in str(e):
            print(f"Test {i}: OK (error esperado)")
        else:
            print(f"Test {i}: ERROR inesperado")
            print(f"Esperado: {esperado}")
            print(f"Obtenido: {e}")
