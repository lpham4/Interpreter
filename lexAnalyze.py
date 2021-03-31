'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''
from Token import *

# This is the dictionary that contains the keywords and operators used
lexAnalyze = {
    "keywords": {
        'array': 'array',
        'begin': 'begin',
        'define': 'define',
        'display': 'display',
        'do': 'do',
        'endfor': 'endfor',
        'endfun': 'endfun',
        'exit': 'exit',
        'for': 'for',
        'function': 'function',
        'import': 'import',
        'input': 'input',
        'integer': 'integer',
        'is': 'is',
        'main': 'main',
        'return': 'return',
        'set': 'set',
        'symbol': 'symbol',
        'to': 'to',
        'type': 'type',
        'variables': 'variables',
        'implementations': 'implementations',
        'if': 'if',
        'endif': 'endif',
        'else': 'else',
        'constants': 'constants',
        'declarations': 'declarations',
        'global': 'global',
        'main': 'main',
        'parameters': 'parameters',
        'struct': 'struct',
        'then': 'then',
        'while': 'while'
    },

    "operators": {
        '+': '+',
        '-': '-',
        '=': '=',
        '*': '*',
        '>': '>',
        '<': '<',
        '>=': '>=',
        '<=': '<=',
        '==': '=='
    },

    "others": {
        ',': ','
    }


}


# Method to turn a word from the file into a Token
def tokenize(word):

    # Test to see if word is a keyword
    if word in lexAnalyze["keywords"]:
        newToken = Token(word, "keyword")
        return (newToken.printToken())

    # Test to see if word is an operator
    elif word in lexAnalyze["operators"]:
        newToken = Token(word, "operator")
        return (newToken.printToken())

    # Test to see if word is a string
    elif("\"" in word):
        newToken = Token(word, "string literal")
        return (newToken.printToken())

    # Else, word is an identifier
    else: 
    	newToken = Token(word, "identifier")
    	return (newToken.printToken())

def getDict():
    return lexAnalyze
