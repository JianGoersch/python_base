#!/usr/bin/env python3

"""
Hello world multilinguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a varialvel LANG devidamente configurada:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__="0.0.1"
__author__="Jian Goersch"
__license__="unlicense"

# Dunder == __ 2 undelines
#snake_case
#PascalCase

import os

current_language = os.getenv("LANG", "pt_BR")[:5] #Fatia valor da variavel do 0 À 5

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# sets (hash table) - 0(1) - constante
# dicts( hash table)
       
print(msg[current_language])