#!/usr/bin/env python
import os

from level1 import makeLevel1
from level2 import makeLevel2
from level3 import makeLevel3
from level4 import makeLevel4
from level5 import makeLevel5
from movement import move, wallCheck, trapCheck, leverCheck, updateMap

state = 0 # states of state machine
diff = 1
goGame = 0
endGame = 0 # boolean for end of game 
key = -1 # user input key selection
lastLev = 0
# Loop until game ends (player loses the game)
while endGame == 0:
	if state == 0:
		# clear screen
		os.system("clear");
		# print welcome screen 
		print("**************************\n    THE MAZE RUNNER")
		print("By: Steph, Zach, and Greg\n**************************")
		print("Use the keys A, S, W, and D to navigate\nthrough the maze. You must")
		print("move the 0 to the exit (wall opening).")
		print("To exit, press E.")
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
	if state == 1:
		# initialize and display map
		player_x = 1
		player_y = 1	
		leverStage = 1	
		os.system("clear")
		if diff == "1":
			currentMap = makeLevel1()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
			
		elif diff == "2":
			currentMap = makeLevel2()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print

		elif diff == "3":
			currentMap = makeLevel3()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		elif diff == "4":
			currentMap = makeLevel4()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print	
		elif diff == "5":
			currentMap = makeLevel5()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
			lastLev = 1
		state = 2
	if state == 2:
		player_x_prev = player_x
		player_y_prev = player_y
		
		direction = raw_input()
		if direction == "E":
			endGame = 1
		player_x, player_y = move(player_x, player_y, direction, currentMap)
			
		if wallCheck(player_x, player_y, currentMap) == 0:
			player_x = player_x_prev
			player_y = player_y_prev
		if trapCheck(player_x, player_y, currentMap) == 0:
			state = 4
		if diff == "4" or diff == "5":
			currentMap, leverStage = leverCheck(player_x, player_y, currentMap, diff, leverStage)
		os.system("clear")	
		currentMap = updateMap(player_x, player_y, player_x_prev, player_y_prev, currentMap)
		
		if player_x == 8 and player_y == 10:
			state = 3
	 
	endGame = 0	
	if state == 3:
		if lastLev == 0:
			choice = raw_input("Nice Work!\nPress any key to continue or E to exit\n")
		else:
			print("You Win!")
			break
		if choice == "E":
			endGame = 1
		else:
			diff = int(diff) + 1
			diff = str(diff)
			state = 1
	if state == 4:
		print("You Died!\nPress any key to  exit\n")
		endGame = 1
			
