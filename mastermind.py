#!/usr/bin/python


class Board:
	def __init__(self, solution, number_of_guesses=10):
		self.solution = solution
		self.guesses = empty_guess * number_of_guesses

	def __str__(self):
		return "{}\n{}\n{}\n{}".format(*[self.format_row(i) for i in range(4)])

	def format_row(self, i):
		return "{} | {}".format(*self.format_guesses(i), self.solution(i))

	def format_guesses(self, i):
		return " - ".join(*[Board.format_guess(guess, i) for guess in self.guesses])

	@staticmethod
	def format_guess(guess, i):
		if guess[i] == solution[i]

	@staticmethod
	def empty_guess():
		return [None]*4	
