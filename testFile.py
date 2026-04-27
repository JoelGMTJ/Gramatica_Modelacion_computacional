import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar
grammar = CFG.fromstring("""
    Start -> OC | P
    
    OC -> OS 'he' OS | OS
    OS -> S V O | S 'bu' V O
    
    P -> PSN | POM | PAB
    PSN -> OS 'ma' '?'
    POM -> OS 'haishi' OS '?'
    PAB -> S V PRNI '?'
    
    PRNI -> 'shenme' | 'nali' | 'zenme' | 'weishenme'
    S -> S 'he' S | S 'men' | 'wo' | 'ta'
    V -> 'shi' | 'chi' | 'xue_xi' | 'he' | 'kan' | 'ting' | 'shuo' | 'xie' | 'qu' | 'lai' | 'zuo' | 'mai' | 'gong_zuo'
    O -> O 'he' O | 'fan' | 'hanpaopao' | 'bingqilin' | 'shui' | 'cha' | 'kafei' | 'pijiu' | 'shu' | 'quianbi' | 'dianying' | 'yinyue' | 'hanzi' | 'moxiguwen' | 'ingwen' | 'dongxi' | 'mianbao' | 'pingguo' | 'kaoshi'
""")
# OC -> Oracion compleja
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
oraciones = [
    "wo xue_xi moxiguwen haishi wo xue_xi yinyue ?",
    "",
    "wo chi fan",
    "wo chi fan",
    "wo chi fan"
    ]

# Tokenize the sentence
i = 0
while (i < 5):
    tokens = nltk.word_tokenize(oraciones[i])
    # Parse the sentence
    for tree in parser.parse(tokens):
        tree.pretty_print()
        i += 1
