#File containing movement funtions

def move(x_val, y_val, direction, currentMap):
	if direction == "d":
		x_val += 1
	elif direction == "a":
		x_val -= 1
	elif direction == "w":
		y_val += 1
	elif direction == "s":
		y_val -= 1
	return x_val, y_val

def wallCheck(x_val, y_val, currentMap):
	print(currentMap[x_val][y_val])
	if currentMap[x_val][y_val] == "#":
		value = 0
	else:
		value = 1
	return value
