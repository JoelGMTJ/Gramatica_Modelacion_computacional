import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    PP -> P NP
    VP -> V NP | VP PP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'park'
    P -> 'in' | 'with'
    V -> 'saw' | 'ate' | 'walked'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = "the dog saw a man in the park"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()