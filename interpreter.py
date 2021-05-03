'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 3rd Deliverable
Date: 05/01/2021
'''

from scanner import *
from lexAnalyze import *
from Token import *
from parser import *

class interpreter:
	
	
	def __init__(self,parser):
		self.parser = parser

	# executor for the interpreter
	def execute():
		#parser is used f
		testParse = parser(scanner("sclTest.scl"))

		#lists to store the identifiers and the actual values used for calculations
		identifiers = []
		storedValues = []
		index = 0
	
		for token in tokens:
			# if a token in the tokens list is an identifier it'll be stored into the identifiers and stored values list
		    if token.Toktype == "identifier" and tokens[index + 1].word == "=":
		        if token.word not in identifiers:
		            res = int(tokens[index + 2].word)
		            storedValues.append(res)
		        identifiers.append(token.word)
		    # if a token in the tokens list is "display", then it's calling for the calculation. If the operator in the operators list is "+", then it'll add the identifiers from the values list
		    if token.word == "display":
		        if tokens[index + 1].Toktype == "string literal":
		            str = tokens[index + 1].word
		            print(str[1:len(str) - 1])
		        elif tokens[index + 1].Toktype == "identifier" and tokens[index + 2].word == "+" and tokens[index + 3].Toktype == "identifier":
		            if tokens[index + 1].word not in identifiers or tokens[index + 3].word not in identifiers:
		                print("Error, unrecognized variable name")
		            else:
		                res1 = identifiers.index(tokens[index + 1].word)
		                res2 = identifiers.index(tokens[index + 3].word)
		                print(storedValues[res1] + storedValues[res2])
		        elif tokens[index + 1].Toktype == "identifier" and tokens[index + 2].word == "-" and tokens[index + 3].Toktype == "identifier":
		            if tokens[index + 1].word not in identifiers or tokens[index + 3].word not in identifiers:
		                print("Error, unrecognized variable name")
		            else:
		                res1 = identifiers.index(tokens[index + 1].word)
		                res2 = identifiers.index(tokens[index + 3].word)
		                print(storedValues[res1] - storedValues[res2])
		    index += 1
	
interpreter.execute()