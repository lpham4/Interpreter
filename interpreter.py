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

	def execute():
		testParse = parser(scanner("sclTest.scl"))


interpreter.execute()