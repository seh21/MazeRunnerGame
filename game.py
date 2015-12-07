#!/usr/bin/env python
import os

from level1 import makeLevel1
from movement import move, wallCheck, updateMap
# Declare initial positions of the Minotaur and Theseus 
minotaur_x = 1
minotaur_y = 1

player_x = 1
player_y = 1

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
			currentMap = makeLevel1()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
			
		elif diff == "2":
			currentMap = makeLevel1()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print

		elif diff == "3":
			currentMap = makeLevel1()
			for row in currentMap:
				for val in row:
					print '{:4}'.format(val),
				print
		
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
		os.system("clear")	
		currentMap = updateMap(player_x, player_y, player_x_prev, player_y_prev, currentMap)
		
		break
