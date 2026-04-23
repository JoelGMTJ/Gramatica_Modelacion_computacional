import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> Oracion_simple | Pregunta_s/n | Pregunta_abierta
    Oracion_simple -> Sujeto Verbo Objeto
    Pregunta_s/n -> Oracion_simple 'ma'
    Pregunta_abierta -> Oracion_simple
    Sujeto -> Sujeto Conector Sujeto | Sujeto
    Verbo -> 'shi' | 'chi' | 'xue xi'
    Objeto -> 'moxiguren'
    Sujeto -> 'wo' | 'ta' | 'women' | 'tamen'
    Conector -> 'he'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = "wo shi moxiguren"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()