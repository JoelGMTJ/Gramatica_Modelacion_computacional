import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar
grammar = CFG.fromstring("""
    Start -> OC | P
    
    OC -> OC 'he' OS | OS
    OS -> SP V OP | SP 'bu' V OP
    
    P -> PSN | POM | PAB
    PSN -> OS 'ma' '?'
    POM -> OC 'haishi' OS '?'
    PAB -> SP V PRNI '?'
    
    PRNI -> 'shenme' | 'nali' | 'zenme' | 'weishenme'
    SP -> SP 'he' SS | SS
    SS -> SS 'men' | 'wo' | 'ta'
    V -> 'shi' | 'chi' | 'xue_xi' | 'hei' | 'kan' | 'ting' | 'shuo' | 'xie' | 'qu' | 'lai' | 'zuo' | 'mai' | 'gong_zuo'
    OP -> OP 'he' O | O
    O -> 'fan' | 'hanpaopao' | 'bingqilin' | 'shui' | 'cha' | 'kafei' | 'pijiu' | 'shu' | 'quianbi' | 'dianying' | 'yinyue' | 'hanzi' | 'moxiguwen' | 'zongwen' | 'ingwen' | 'dongxi' | 'mianbao' | 'pingguo' | 'kaoshi' | 'moxiguren'
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

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Ejemplos de oraciones
oracionesPinyin = [
    "wo xue_xi moxiguwen haishi wo xue_xi yinyue ?",
    "ta men bu chi hanpaopao",                      
    "wo he ta chi fan he bingqilin",                
    "ta men kan dianying ma ?",                     
    "ta zuo shenme ?",
    "wo he ta men shi moxiguren",
    "wo men hei pijiu he shui",
    "ta men kan shenme ?",
    "ta men he wo chi hanpaopao haishi ta men he wo chi bingqilin ?",
    "wo shuo moxiguwen he ta shuo ingwen he ta men shuo zongwen"                               
]

def ejemplosOraciones():
    for oracion in oracionesPinyin:
        print()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        tokens = nltk.word_tokenize(oracion)
        # Parse the sentence
        print("Arbol de la oracion: " + oracion)
        for tree in parser.parse(tokens):
            tree.pretty_print()

ejemplosOraciones()