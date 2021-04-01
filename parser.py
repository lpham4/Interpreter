'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 2nd Deliverable
Date: 03/27/2021
'''
from scanner import *
from lexAnalyze import *
from Token import *

class parser:

	def __init__(self, scanner):
		self.scanner = scanner


	def parse(self):
		testScan = scanner("sclTest.scl")
		testScan.scanning() 
		print("Tokens in list: ", len(tokens))







testParser = parser(scanner("sclTest.scl"))
testParser.parse()