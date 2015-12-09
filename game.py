#!/usr/bin/env python
import os

# Import Maze Maps: Level1 - Level5
from level1 import makeLevel1
from level2 import makeLevel2
from level3 import makeLevel3
from level4 import makeLevel4
from level5 import makeLevel5

# Import needed functions
from movement import move, wallCheck, trapCheck, leverCheck, updateMap

state = 0 # Variable to track state machine
diff = 1 # Variable to track difference
goGame = 0 # Variable to track start of game
endGame = 0 # boolean for end of game 
key = -1 # user input key selection
lastLev = 0 # Variable to track leveling

# Loop until game ends (player loses the game)
while endGame == 0:
	# First State in state machine
	if state == 0:
		# clear screen
		os.system("clear");
		# print welcome screen 
		print("**************************\n    THE MAZE RUNNER")
		print("By: Steph, Zach, and Greg\n**************************")
		print("Use the keys A, S, W, and D to navigate\nthrough the maze. You must")
		print("move the 0 to the exit (wall opening).")
		print("To exit, press E.")
		
		# Loop for user difficulty select
		while goGame == 0:
			print("There are 5 Levels: 1-Easiest 5-Hardest")
			diff = raw_input("Enter a difficulty: ")
			if diff < "6" and diff > "0":
				goGame = 1
			if diff == "E":
				goGame = 1
				endgame = 1
			if goGame == 0:
				print("Invalid difficulty!")
		os.system("clear") 	# clear screen
		state = 1
	# Second State in State Machine
	if state == 1:
		# initialize and display map
		player_x = 1
		player_y = 1	
		leverStage = 1	
		os.system("clear")
		# Load Map 1
		if diff == "1":
			currentMap = makeLevel1()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		# Load Map 2
		elif diff == "2":
			currentMap = makeLevel2()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		# Load Map 3
		elif diff == "3":
			currentMap = makeLevel3()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		# Load Map 4
		elif diff == "4":
			currentMap = makeLevel4()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		# Load Map 5
		elif diff == "5":
			currentMap = makeLevel5()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
			lastLev = 1
		state = 2
	# Third State in state machine
	if state == 2:
		# Variables to track previous location
		player_x_prev = player_x
		player_y_prev = player_y
		
		# User Input
		direction = raw_input()
		
		# Condition for Exit
		if direction == "E":
			endGame = 1
		# Call to Move Function
		player_x, player_y = move(player_x, player_y, direction, currentMap)
			
		# Check for wall or boundary
		if wallCheck(player_x, player_y, currentMap) == 0:
			player_x = player_x_prev
			player_y = player_y_prev
		# Check for trap
		if trapCheck(player_x, player_y, currentMap) == 0:
			state = 4
		if diff == "4" or diff == "5":
			currentMap, leverStage = leverCheck(player_x, player_y, currentMap, diff, leverStage)
		os.system("clear")	
		
		# Update of map with player
		currentMap = updateMap(player_x, player_y, player_x_prev, player_y_prev, currentMap)
		
		# Check for win Condition
		if player_x == 8 and player_y == 10:
			state = 3
	 
	endGame = 0
	# Forth State in state Machine
	if state == 3:
		# Condition for Level Win
		if lastLev == 0:
			choice = raw_input("Nice Work!\nPress any key to continue or E to exit\n")
		else:
			print("You Win!")
			break
		# Condition for Exit
		if choice == "E":
			endGame = 1
		else:
			diff = int(diff) + 1
			diff = str(diff)
			state = 1
	# Fifth State in state machine
	if state == 4:
		# Dislay for lose
		print("You Died!\nPress any key to  exit\n")
		endGame = 1
			
