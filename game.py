#!/usr/bin/env python

import getch 

# Declare initial positions of the Minotaur and Theseus 
minotaur_x = 1
minotaur_y = 1

thes_x = 1
thes_y = 7

state = -1 # states of state machine
endGame = 0
key = -1

# Loop until game ends (player loses the game)
while endGame == 0:
	if choice == 1:
		# print welcome screen 
		print("**************************\n  THE MINOTAUR GAME  \n")
		print("By: Steph, Zach and Greg\n**************************\n")
		print("Use the keys A, S, W, and D to navigate\nthrough the maze. You must\n")
		print("move Theseus (~) to the exit '>'\nwithout getting eaten by the Minotaur (<).\n")
		print("To begin, press G. To exit, press E.")
	key = getch.getch() # gets user input 
	if key == 'G':
		state = 1
	elif key = 'E':
		endGame = 1
		break
	else;
		state = 0 
