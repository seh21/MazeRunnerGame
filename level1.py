def makeLevel1():
	maze = [[ " " for j in range(9)] for i in range(20)]

	for j in range(0, 19):
		maze[j][8] = "#"
	for j in range(0, 19):
		maze[j][0] = "#"
	for j in range(0, 9):
		maze[0][j] = "#"
	for j in range(0, 9):
		maze[19][j] = "#"
	for j in range(1, 5):
		maze[10][j] = "#"
	for j in range(1, 5):
		maze[j][2] = "#"
	for j in range(2, 6):
		maze[7][j] = "#"
	for j in range(7, 13):
		maze[j][6] = "#"
	for j in range(3, 7):
		maze[j][4] = "#"
	maze[9][7] = "#"

	for j in range(5,7):
		maze[3][j] = "#"
	for j in range(3, 7):
		maze[13][j] = "#"
	for j in range(15, 19):
		maze[j][2] = "#"
	for j in range(14, 17):
		maze[j][4] = "#"
	for j in range(15, 19):
		maze[j][6] = "#"
	maze[10][8] = " "
	maze[1][1] = "0"

	for row in maze:
		for val in row:
			print '{:4}'.format(val),
		print
	return maze
 	
