#!/usr/bin/env python

import getch 

# Declare initial positions of the Minotaur and Theseus 
minotaur_x = 1
minotaur_y = 1

thes_x = 1
thes_y = 7

state = 0 # states of state machine
endGame = 0 # boolean for end of game 
key = -1 # user input key selection

# Loop until game ends (player loses the game)
while endGame == 0:
	if state == 0:
		# print welcome screen 
		print("**************************\n  THE MINOTAUR GAME  \n")
		print("By: Steph, Zach and Greg\n**************************\n")
		print("Use the keys A, S, W, and D to navigate\nthrough the maze. You must\n")
		print("move Theseus (~) to the exit '>'\nwithout getting eaten by the Minotaur (<).\n")
		print("To begin, press G. To exit, press E.")
		key = getch.getch() # gets user input 
		if key == 'G':
			# clear the screen 
			state = 1
		elif key = 'E':
			endGame = 1
			break
		else;
			state = 0 
	if state == 1:
		# initialize and generate map 
		state = 2
	if state == 2:
		thes_x_prev = thes_x
		thes_y_prev = thes_y
		
		dir = getch.getch()
		
		if dir == 'd'
			thes_x = thes_x + 1 
		elif dir == 's'
			thes_y = thes_y - 1 
		elif dir == 'a'
			thes_x = thes_x - 1
		elif dir == 'w'
			thes_y = thes_y + 1
		elif dir == 'E'
			# exit game 
			break 
		
		
		
