'''
CS 4308 Section 02 Spring 2021
Donna Young, Alex Jarvis, Ly Pham
Project 1st Deliverable
Date: 02/22/2021
'''
class Token:
	def __init__(self, word, Toktype):
		self.word = word
		self.Toktype = Toktype
		

	def printToken(self):
		return ("Token: " + self.word + ", " + self.Toktype)