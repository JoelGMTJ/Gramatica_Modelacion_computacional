import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar
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
    # Oraciones Simples (OS)
    "ta chi pingguo",
    "wo men bu xie hanzi",
    "ta men mai mianbao",
    "wo kan dianying he ta ting yinyue",
    "wo men zuo kaoshi he ta men gong_zuo",
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