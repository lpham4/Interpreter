'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''
from Token import *
from lexAnalyze import *

testFile = open("/Users/lypham/Desktop/Interpreter/sclTest.scl", "r")
for line in testFile:
	for word in line.split():
		print(tokenize(word))