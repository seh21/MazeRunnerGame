# Level 2 for Maze Runner Game
def makeLevel2():
	#Definition of Range
	maze = [[ " " for j in range(9)] for i in range(20)]
	
	# Use of '#' for boundary
	for j in range(0, 19):
		maze[j][8] = "#"
	for j in range(0, 19):
		maze[j][0] = "#"
	for j in range(0, 9):
		maze[0][j] = "#"
	for j in range(0, 9):
		maze[19][j] = "#"
	for j in range(1, 7):
		maze[3][j] = "#"
	for j in range(2, 7):
		maze[5][j] = "#"
	for j in range(2, 8):
		maze[8][j] = "#"
	maze[6][2] = "#"
	maze[7][2] = "#"
	maze[10][8] = " "
	for j in range(9, 18):
		maze[j][6] = "#"
	for j in range(2, 7):
		maze[10][j] = "#"
	for j in range(2, 7):
		maze[12][j] = "#"
	for j in range(2, 7):
		maze[14][j] = "#"
	for j in range(2, 7):
		maze[16][j] = "#"
	for j in range(2, 5):
		maze[18][j] = "#"

	# Use of ' 'to make openings and Exit
	maze[10][6] = " "
	maze[12][6] = " "
	maze[13][6] = " "
	maze[13][4] = "#"
	# Use of '0' to show player
	maze[1][1] = "0"

	return maze
