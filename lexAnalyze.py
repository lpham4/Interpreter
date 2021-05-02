'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''
from Token import *
tokens = []

# This is the dictionary that contains the keywords and operators used
lexAnalyze = {
    "keywords": {
        'begin': 11,
        'define': 12,
        'display': 13,
        'endfun': 14,
        'for': 15,
        'function': 16,
        'import': 17,
        'integer': 18,
        'main': 19,
        'set': 20,
        'type': 21,
        'variables': 22,
        'implementations': 23,
        'is': 24
    },

    "operators": {
        '+': 25,
        '=': 26
    },

    "others": {
        ',': 27,
        '\"': 28,
        'identifier': 29
    }


}

def getRules():
    return lexAnalyze


# Method to turn a word from the file into a Token
def tokenize(word):
    # Test to see if word is a keyword
    if word in lexAnalyze["keywords"]:
        newToken = Token(word, "keyword", lexAnalyze["keywords"][word])
        tokens.append(newToken)
        return (newToken.printToken())

    # Test to see if word is an operator
    elif word in lexAnalyze["operators"]:
        newToken = Token(word, "operator", lexAnalyze["operators"][word])
        tokens.append(newToken)
        return (newToken.printToken())

    # Test to see if word is a string
    elif("\"" in word):
        newToken = Token(word, "string literal", lexAnalyze["others"]["\""])
        tokens.append(newToken)
        return (newToken.printToken())

    # Else, word is an identifier
    else:
        newToken = Token(word, "identifier", 29)
        tokens.append(newToken)
        return (newToken.printToken())

def getDict():
    return lexAnalyze
