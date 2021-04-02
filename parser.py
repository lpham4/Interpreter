'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 2nd Deliverable
Date: 03/30/2021
'''
from scanner import *
from lexAnalyze import *
from Token import *


# Description: The parse rules are stored in a dictionary where each key corresponds to the first
# key word in each statement, and its values are those which are the tokens that follow. For this
# dictionary we have only included the combinations which are relevant to the grammar of our file.
parse = {
	17: [28],
	23: [],
	16: [19, 24],
	22: [],
	12: [29, 21, 18],
	11: [],
	20: [29, 26, 29],
	13: [29, 25, 29],
	14: [19]
}

class parser:

	def __init__(self, scanner):
		self.scanner = scanner


	def parse(self):
		testScan = scanner("sclTest.scl")
		testScan.scanning()
		
		isValid = True
		for i in range(len(tokens)):
			if tokens[i].id in parse.keys():
				ret = tokens[i].word
				count = i + 1
				for value in parse[tokens[i].id]:
					if value == tokens[count].id:
						ret += " " + tokens[count].word
					else:
						isValid = False
					count += 1
				if not isValid:
					print("Error: Invalid Statement")
					break
				else:
					print(ret)


testParser = parser(scanner("sclTest.scl"))
testParser.parse()

