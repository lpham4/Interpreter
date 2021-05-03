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

		#lists to store the identifiers, operators and the actual values used for calculations
		identifiers = []
		operators = []
		storedValues = []

		# if a token in the tokens list is an identifier or operator it'll be stored into the identifiers/operators list
		for token in tokens:
			if token.Toktype == "identifier":
				identifiers.append(token.word)
			if token.Toktype == "operator":
				operators.append(token.word)
			
		# if the identifiers in the identifiers list are number, they'll be stored as values in the values list. numeric() is used to check if it's a number
		for x in identifiers:
			if x.isnumeric():
				storedValues.append(x)	

		# if a token in the tokens list is "display", then it's calling for the calculation. If the operator in the operators list is "+", then it'll add the identifiers from the values list
		for token in tokens:
			if token.word == "display":
				for op in operators:
					if op == "+":
						res1 = int(storedValues[0])
						res2 = int(storedValues[1])
						ans = res1 + res2
						print(ans)		

interpreter.execute()