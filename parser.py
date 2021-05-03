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
		#scanner is used with the parser
		testScan = scanner("sclTest.scl")
		testScan.scanning()

	# function to display token with the word and token type. Used in the case there's an error in parsing
	def display_token(token):
		return f"token:[type:{token.Toktype} value:{token.word}]"


	# function to read in the import statement of the scl program. If the index next to "import" is a string literal, then it is recognized as an import statement.
	def import_stmt(index):
		if tokens[index + 1].Toktype == "string literal":
			print("<imports> -> <import_file> -> ", tokens[0].word, " -> <header_file_name> -> <fname>", tokens[1].word)
			return index + 2
		else:
			print(f"Error: Invalid import statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the implement statement of the scl program. If the token is a keyword, then it is recognized.
	def implement_stmt(index):
		if tokens[index + 1].Toktype == "keyword":
			print("<implement>", tokens[2].word)
			return index + 1
		else:
			print(f"Error: Invalid implement statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the function statement of the scl program. If the index next to "function" is a keyword, and the index next to that is "is", then it is recognized as a function statement.
	def func_stmt(index):
		if tokens[index + 1].Toktype == "keyword" and tokens[index + 2].word == "is":
			print("<function_main>", tokens[3].word, tokens[4].word, " -> <funct_body>", tokens[5].word)
			return index + 3
		else:
			print(f"Error: Invalid function statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read the variable declarations statement of the scl program. If the token is a keyword, then it is recognized as a variable declarations statement.
	def var_stmt(index):
		if tokens[index].Toktype == "keyword":
			print("<var> -> <var_declare>", tokens[6].word)
			return index + 1
		else:
			print(f"Error: Invalid variables statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the define statements of the scl programs. If the next index is an identifier, and the index after that is "type", and the index after that is a keyword, then it is recognized as a define statement.
	def def_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].word == "type" and tokens[index + 3].Toktype == "keyword":
			print("<data_declarations> -> <identifier> -> <data_type>")
			return index + 4
		else:
			print(f"Error: Invalid define statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the begin statement of the scl program. If the token is a keyword, then it is recognized as a begin statement.
	def begin_stmt(index):
		if tokens[index].Toktype == "keyword":
			print("<begin>", tokens[19].word)
			return index + 1
		else:
			print(f"Error: Invalid begin statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the set staements of the scl program. If next index is an identifier, and the index next to that is an operator, and the next indext to that is an indentifier, then it is recognized as a set statment.
	def set_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].Toktype == "operator" and tokens[index + 3].Toktype == "identifier":
			print("<set> -> <identifier> -> <operator> -> <identifier>")
			return index + 4
		else:
			print(f"Error: Invalid set statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the display statement of the scl program. If the next index is an identifier, and the next index to that is an operator, and the next index to that is an identifier, then it is recognized as a display statement.
	def display_stmt(index):
		if tokens[index + 1].Toktype == "identifier" and tokens[index + 2].Toktype == "operator" and tokens[index + 3].Toktype == "identifier":
			print("<display> -> <identifier> ->", tokens[29].word, " -> <operator> ->", tokens[30].word, "-> <identifier ->", tokens[31].word)
			return index + 4
		else:
			print(f"Error: Invalid display statement syntax. Unexpected token {display_token(tokens[index + 1])}")

	# function to read in the end function statement of the scl program. If the token is a keyword, then it is recognized as an end function statement.
	def endfunc_stmt(index):
		if tokens[index + 1].Toktype == "keyword":
			print("<endfunct> ->", tokens[32].word, "-> <function_main> ->", tokens[33].word)
			return index + 2
		else:
			print(f"Error: Invalid end statement syntax. Unexpected token {display_token(tokens[index + 1])}")
			

p = parser(scanner("sclTest.scl"))
p.parse()

# index used to parse through the tokens list and used along with the functions in the parser class
index = 0
while index < len(tokens):
	# check for the first token in the tokens list. If it is "import", then it'll check the import statement function to determine if it's recognized
	if tokens[index].word == "import":
		index = parser.import_stmt(index)
		continue
	# check if the next line is implementations
	if tokens[index].word == "implementations":
		index = (parser.implement_stmt(index))
		continue
	# check for the first word of the line and if it's "function", then it'll check the function statement function to determine if it's recognized
	if tokens[index].word == "function":
		index = (parser.func_stmt(index))
		continue
	# check for the first word of line and if it's "variables", then it'll check the variables statement function to determine if it's recognized
	if tokens[index].word == "variables":
		index = (parser.var_stmt(index))
		continue
	# check if the first word of the line is "define", then it'll check the define statement function to determine if it's recognized
	if tokens[index].word == "define":
		index = (parser.def_stmt(index))
		continue
	# check if the first word of the line is "begin", then it'll check if the begin statement function to determine if it's recognized
	if tokens[index].word == "begin":
		index = (parser.begin_stmt(index))
	# check if the first word is "set", then it'll check if the set statment function to determine if it' recognized
	if tokens[index].word == "set":
		index = (parser.set_stmt(index))
		continue
	# check if the first word is "display", then it'll check if the display statement function is recognized
	if tokens[index].word == "display":
		index = (parser.display_stmt(index))
		continue
	# check if the first word of line is "endfun", then it'll check if the end function statement is recognized
	if tokens[index].word == "endfun":
		index = (parser.endfunc_stmt(index))
		continue
	# if the first words of lines are not above, then it is considered as wrong start of statement
	else:
		print(f"Error: Unexpected start {display_token(tokens[index])}, please check the syntax of your file.")
		break






