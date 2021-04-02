'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''


from lexAnalyze import *

class scanner:
	def __init__(self, fileName):
		self.fileName = fileName

	def getfileName(self):
		return self.fileName

	def scanning(self):
		fileName = open("sclTest.scl", "r")
		for line in fileName:
			for word in line.split():
				print(tokenize(word))

#testScan = scanner("sclTest.scl")
#testScan.scanning()
