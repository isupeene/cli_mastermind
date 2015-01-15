#!/usr/bin/python

from sys import stdin
from random import randrange

readline = lambda: stdin.readline().strip()

PERFECT_GUESS_MARKER = ">"
PARTIAL_GUESS_MARKER = "X"
INCORRECT_GUESS_MARKER = " "

class Board:

	def __init__(self, solution, number_of_guesses=10):
		self.solution = solution
		self.guesses = [Board.empty_guess()] * number_of_guesses
		self.reveal_solution = False
		
	def guess(self, guess):
		i = self.guesses.index(Board.empty_guess())
		self.guesses[i] = guess

	def __str__(self):
		return "{}\n{}\n{}\n{}".format(*[self.format_row(i) for i in range(4)])

	def format_row(self, i):
		return "{} | {}".format(self.format_guesses(i), self.solution[i] if self.reveal_solution else "?")

	def format_guesses(self, i):
		return " - ".join([self.format_guess(guess, i) for guess in self.guesses])

	def format_guess(self, guess, i):
		if guess[i] == self.solution[i]:
			clue = PERFECT_GUESS_MARKER
		elif guess[i] in self.solution and not self.partial_markers_saturated(guess, i):
			clue = PARTIAL_GUESS_MARKER
		else:
			clue = INCORRECT_GUESS_MARKER
			
		return "{}{}".format(clue, guess[i])
	
	def partial_markers_saturated(self, guess, i):
		already_used = len([x for x in guess[:i] if x == guess[i]])
		reserved = len([x for x, y in zip(guess[i + 1:], self.solution[i + 1:]) if x == y and x == guess[i]])
		capacity = len([x for x in self.solution if x == guess[i]])
		
		return already_used + reserved >= capacity
		
	def victory(self):
		return self.solution in self.guesses
		
	def game_over(self):
		return self.guesses[-1] != Board.empty_guess()

	@staticmethod
	def empty_guess():
		return [" "]*4


def random_board(number_of_guesses=10):
	return Board([randrange(1, 7) for _ in range(4)], number_of_guesses)
	
def play_turn(board, first_time=True):
	if first_time:
		print("Enter your guess (4 numbers from 1-6):")
	else:
		print("Invalid guess.  Try again:")
		
	guess = [int(x) for x in readline()]
	
	if len(guess) != 4 or not all(number in range(1, 7) for number in guess):
		play_turn(board, first_time=False)
	else:
		board.guess(guess)
	
	
def play():
	board = random_board()
	print(board)
	while True:
		play_turn(board)
		if board.victory():
			board.reveal_solution = True
			print(board)
			print("Congratulations!  You win!")
			break
		elif board.game_over():
			board.reveal_solution = True
			print(board)
			print("Sorry, you lose.")
			break
		else:
			print(board)
		
def finished(first_time=True):
	if first_time:
		print("Play again? (y/n)")
	else:
		print("Please input 'y' or 'n'")
		
	response = readline()
	if response in ["y", "Y"]:
		return False
	elif response in ["n", "N"]:
		return True
	else:
		return finished(first_time=False)

while True:
	play()
	if finished():
		break

print("Thanks for playing!")