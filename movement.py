
#Function containing movement statements
def move(x_val, y_val, direction, currentMap):
	if direction == "d":
		x_val += 1
	elif direction == "a":
		x_val -= 1
	elif direction == "w":
		y_val -= 1
	elif direction == "s":
		y_val += 1
	return x_val, y_val

#F Functions containing wall boundaries
def wallCheck(x_val, y_val, currentMap):
	if currentMap[y_val][x_val] == "#":
		value = 0
	else:
		value = 1
	return value

# Function for updating Map after move
def updateMap(x_val, y_val, x_val_last, y_val_last, currentMap):
	if x_val != x_val_last or y_val != y_val_last:
		currentMap[y_val_last][x_val_last] = " "
		currentMap[y_val][x_val] = "0"
	for row in currentMap:
		for val in row:
			print '{:4}'.format(val),
		print
	return currentMap

# Function for checking traps
def trapCheck(x_val, y_val, currentMap):
	if currentMap[y_val][x_val] == "_":
		currentMap[y_val][x_val] = "^"
		value = 0
	else:
		value = 1
	return value

# Function for Levers
def leverCheck(x_val, y_val, currentMap, level, stage):
	if currentMap[y_val][x_val] == "L":
		if level == "4":
			if stage == 1:
				currentMap[2][4] = " "
			elif stage == 2:
				currentMap[5][2] = " "
			elif stage == 3:
				currentMap[10][2] = " "
			elif stage == 4:
				currentMap[15][2] = " "
			elif stage == 5:
				currentMap[17][4] = " "
			elif stage == 6:
				currentMap[5][6] = " "
			elif stage == 7:
				currentMap[15][6] = " "
			elif stage == 8:
				currentMap[10][7] = " "
				currentMap[11][7] = "#"
			stage += 1
		elif level == "5":
			if stage == 1:
				currentMap[3][1] = " "
			elif stage == 2:
				currentMap[3][5] = " "
			elif stage == 3:
				currentMap[13][5] = " "
			elif stage == 4:
				currentMap[13][2] = " "
			elif stage == 5:
				currentMap[8][5] = " "
			elif stage == 6:
				currentMap[10][7] = "#"
			stage += 1
	return currentMap, stage
