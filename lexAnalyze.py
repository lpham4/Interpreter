'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''
from token import *

# This is the dictionary that contains the keywords and operators used
lexAnalyze = {
    "keywords": {
        'array': 1,
        'begin': 2,
        'define': 3,
        'display': 4,
        'do': 5,
        'endfor': 6,
        'endfun': 8,
        'exit': 9,
        'for': 10,
        'function': 11,
        'import': 12,
        'input': 13,
        'integer': 14,
        'is': 15,
        'main': 16,
        'return': 17,
        'set': 18,
        'symbol': 19,
        'to': 20,
        'type': 21,
        'variables': 22,
        'implementations': 23
    },

      "operators": {
        '+': 24,
        '-': 25,
        '=': 26
    }
}


# Method to turn a word from the file into a Token
def tokenize(word):

    # Test to see if word is a keyword
    if word in lexAnalyze["keywords"]:
        newToken = token(word, "keyword", lexicalAnalyzer["keywords"][word])
        return newToken

    # Test to see if word is an operator
    if word in lexAnalyze["operators"]:
        newToken = token(word, "arithmetic operator", lexicalAnalyzer["arithOps"][word])
        return newToken

    # Test to see if word is a string
    if(word.contains("\"")):
        newToken = token(word, "string literal", 27)
        return newToken

    # Else, word is an identifier
    newToken = token(word, "identifier", 28)
    return newToken
