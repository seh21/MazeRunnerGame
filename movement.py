#File containing movement funtions
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

def wallCheck(x_val, y_val, currentMap):
	if currentMap[y_val][x_val] == "#":
		value = 0
	else:
		value = 1
	return value

def updateMap(x_val, y_val, x_val_last, y_val_last, currentMap):
	if x_val != x_val_last or y_val != y_val_last:
		currentMap[y_val_last][x_val_last] = " "
		currentMap[y_val][x_val] = "0"
	for row in currentMap:
		for val in row:
			print '{:4}'.format(val),
		print
	return currentMap	
