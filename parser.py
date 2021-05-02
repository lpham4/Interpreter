'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 3rd Deliverable
Date: 05/01/2021
'''
from scanner import *
from lexAnalyze import *
from Token import *

class parser:
	index = 0
	def __init__(self, scanner):
		self.scanner = scanner


	def parse(self):
		testScan = scanner("sclTest.scl")
		testScan.scanning()


	def display_token(token):
		return f"token:[type:{token.Toktype} value:{token.word}]"


	def import_stmt(index):
		if tokens[index + 1].Toktype == "string literal":
			print("<imports> -> <import_file> -> <header_file_name> -> <fname>")
			return index + 2
		else:
			print(f"Error: Invalid import statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	def implement_stmt(index):
		if tokens[index + 1].Toktype == "keyword":
			print("<implement>")
			return index + 1
		else:
			print(f"Error: Invalid implement statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	def func_stmt(index):
		if tokens[index + 1].Toktype == "keyword" and tokens[index + 2].word == "is":
			print("<function_main> -> <funct_body>")
			return index + 3
		else:
			print(f"Error: Invalid function statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	def var_stmt(index):
		if tokens[index].Toktype == "keyword":
			print("<var> -> <var_declare>")
			return index + 1
		else:
			print(f"Error: Invalid variables statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	def def_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].word == "type" and tokens[index + 3].Toktype == "keyword":
			print("<data_declarations> -> <data_type>")
			return index + 4
		else:
			print(f"Error: Invalid define statement syntax. Unexpected token {display_token(tokens[index + 1])}")
	def begin_stmt(index):
		if tokens[index].Toktype == "keyword":
			print("<begin>")
			return index + 1
		else:
			print(f"Error: Invalid begin statement syntax. Unexpected token {display_token(tokens[index + 1])}")
	def set_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].Toktype == "operator" and tokens[index + 3].Toktype == "identifier":
			print("<set>")
			return index + 4
		else:
			print(f"Error: Invalid set statement syntax. Unexpected token {display_token(tokens[index + 1])}")
	def display_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].Toktype == "operator" and tokens[index + 3].Toktype == "identifier":
			print("<display>")
			return index + 4
		else:
			print(f"Error: Invalid display statement syntax. Unexpected token {display_token(tokens[index + 1])}")
	def endfunc_stmt(index):
		if tokens[index + 1].Toktype == "keyword":
			print("<endfunc>")
			return index + 2
		else:
			print(f"Error: Invalid end statement syntax. Unexpected token {display_token(tokens[index + 1])}")
			

p = parser(scanner("sclTest.scl"))
p.parse()
index = 0
while index < len(tokens):
	if tokens[index].word == "import":
		index = parser.import_stmt(index)
		continue
	if tokens[index].word == "implementations":
		index = (parser.implement_stmt(index))
		continue
	if tokens[index].word == "function":
		index = (parser.func_stmt(index))
		continue
	if tokens[index].word == "variables":
		index = (parser.var_stmt(index))
		continue
	if tokens[index].word == "define":
		index = (parser.def_stmt(index))
		continue
	if tokens[index].word == "begin":
		index = (parser.begin_stmt(index))
	if tokens[index].word == "set":
		index = (parser.set_stmt(index))
		continue
	if tokens[index].word == "display":
		index = (parser.display_stmt(index))
		continue
	if tokens[index].word == "endfun":
		index = (parser.endfunc_stmt(index))
		continue
	else:
		print(f"Error: Unexpected start {display_token(tokens[index])}, please check the syntax of your file.")
		break






