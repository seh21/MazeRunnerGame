#!/usr/bin/env python
import os
# Declare initial positions of the Minotaur and Theseus 
minotaur_x = 1
minotaur_y = 1

thes_x = 1
thes_y = 7

state = 0 # states of state machine
diff = 1
goGame = 0
endGame = 0 # boolean for end of game 
key = -1 # user input key selection

# Loop until game ends (player loses the game)
while endGame == 0:
	if state == 0:
		# clear screen
		os.system("clear");
		# print welcome screen 
		print("**************************\n  THE MINOTAUR GAME")
		print("By: Steph, Zach, and Greg\n**************************")
		print("Use the keys A, S, W, and D to navigate\nthrough the maze. You must")
		print("move Theseus (~) to the exit '>'\nwithout getting eaten by the Minotaur (<).")
		print("To exit, press E.")
		while goGame == 0:
			print("There are 3 Levels: 1-Easiest 3-Hardest")
			diff = raw_input("Enter a difficulty: ")
			if diff < "4" and diff > "0":
				goGame = 1
			if diff == "E":
				goGame = 1
				endgame = 1
			if goGame == 0:
				print("Invalid difficulty!")
	#	os.system("clear") 	# clear screen
		state = 1
	if state == 1:
		# initialize and display map			
		if diff == "1":
			filename = "Level1.txt"
			map_contents = open(filename)
			print map_contents.read()
		elif diff == 2:
			filename = "Level1.txt"
			map_contents = open(filename)
			print map_contents.read()
		elif diff == 3:
			filename = "Level1.txt"
			map_contents = open(filename)
			print map_contents.read()
		
		state = 2
		endGame = 1
#	if state == 2:
#		thes_x_prev = thes_x
#		thes_y_prev = thes_y
#		
#		dir = getch.getch()
#		
#		if dir == 'd'
#			thes_x = thes_x + 1 
#		elif dir == 's'
#			thes_y = thes_y - 1 
#		elif dir == 'a'
#			thes_x = thes_x - 1
#		elif dir == 'w'
#			thes_y = thes_y + 1
#		elif dir == 'E'
#			# exit game 
#			break 
