import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Definicion de la gramatica
grammar = CFG.fromstring("""
    Start -> OC | P
    
    OC -> OS OC_A
    OC_A -> 'he' OS OC_A | 
    
    OS -> SP V OP | SP 'bu' V OP
    
    P -> PSN | POM | PAB
    PSN -> OS 'ma' '?'
    POM -> OC 'haishi' OS '?'
    PAB -> SP V PRNI '?'
    
    PRNI -> 'shenme' | 'nali' | 'zenme' | 'weishenme'
    
    SP -> SS SP_A
    SP_A -> 'he' SS SP_A | 
    
    SS -> SB SS_A
    SS_A -> 'men' SS_A | 
    
    SB -> 'wo' | 'ta'
    
    V -> 'shi' | 'chi' | 'xue_xi' | 'hei' | 'kan' | 'ting' | 'shuo' | 'xie' | 'qu' | 'lai' | 'zuo' | 'mai' | 'gong_zuo'
    
    OP -> O OP_A 
    OP_A -> 'he' O OP_A |
    
    O -> 'fan' | 'hanpaopao' | 'bingqilin' | 'shui' | 'cha' | 'kafei' | 'pijiu' | 'shu' | 'quianbi' | 'dianying' | 'yinyue' | 'hanzi' | 'moxiguwen' | 'zongwen' | 'ingwen' | 'dongxi' | 'mianbao' | 'pingguo' | 'kaoshi' | 'moxiguren' | 'chang'
""")
# Definicion de las letras que estoy usando en mi gramatica
# OS -> Oracion simple

# P -> Pregunta
# PSN -> Pregunta si/no
# POM -> Pregunta opcion multiple
# PAB -> Pregunta abierta

# PRNI -> Pronombres interrogativos
# S -> Sujeto
# V -> Verbo
# O -> Objeto

parser = nltk.ChartParser(grammar)

# Ejemplos de oraciones correctas
oracionesCorrectas = [
    "ta chi pingguo",
    "wo men bu xie hanzi",
    "ta men mai mianbao",
    "wo kan dianying he ta ting yinyue",
    "wo men zuo kaoshi he ta men gong_zuo chang",
    "ta men shuo ingwen he wo men shuo zongwen",
    "wo shuo moxiguwen he ta shuo ingwen he ta men shuo zongwen",
    "ta chi bingqilin ma ?",
    "wo men xue_xi zongwen ma ?",
    "ta men hei kafei ma ?",
    "ta chi fan haishi ta chi hanpaopao ?",
    "wo men hei cha haishi wo men hei shui ?",
    "ta men kan shu haishi ta men kan dianying ?",
    "ta men xue_xi shenme ?",
    "wo men qu nali ?",
    "ta zuo zenme ?"
]

# Ejemplos de oraciones incorrectas
oracionesIncorrectas = [
    "chi ta pingguo",
    "wo bu men xie hanzi",
    "ta men bu",
    "wo xue_xi ingwen ma"
]

# Funcion que con las oraciones correctas
def generarArboles(oraciones):
    for oracion in oraciones:
        print()
        print("--------------------------------------------------------------------------------------------------")
        tokens = nltk.word_tokenize(oracion)
        trees = list(parser.parse(tokens))
        if trees:
            print("Arbol de la oracion: " + oracion)
            for tree in trees:
                tree.pretty_print()
        else:
            print("No se pudo generar un árbol para: " + oracion)

print("--------------------------------------------------------------------------------------------------")
print("Las siguiente oraciones deberian de generar el arbol correctamente")
generarArboles(oracionesCorrectas)
print("--------------------------------------------------------------------------------------------------")

print("Las siguientes oraciones no deberian de generar un arbol pues tienen algun defecto")
generarArboles(oracionesIncorrectas)
print("------------------------------------------------------------------------------------------------------")


print("\nIntenta escribir una oracion para ver su arbol")
try:
    while True:
        entrada = input("\n> ")
        if not entrada.strip():
            print("Oración vacía — ingresa texto o presiona Ctrl+C para salir.")
            continue
        tokens = nltk.word_tokenize(entrada)
        trees = list(parser.parse(tokens))
        if trees:
            for tree in trees:
                tree.pretty_print()
        else:
            print("No se pudo generar un árbol para: " + entrada)
except KeyboardInterrupt:
    print("\nSaliendo...")