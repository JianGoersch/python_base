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

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!" 
elif current_language == "es_SP":
    msg = "Hola, Mondo!"       
print(msg)