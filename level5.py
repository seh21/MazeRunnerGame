# Level 5 for Maze Runner Game
def makeLevel5():
	# Definition of Range
	maze = [[ " " for j in range(9)] for i in range(20)]
	
	# Use of '#' for Boundary
	for j in range(0, 19):
		maze[j][8] = "#"
	for j in range(0, 19):
		maze[j][0] = "#"
	for j in range(0, 9):
		maze[0][j] = "#"
	for j in range(0, 9):
		maze[19][j] = "#"
	
	# Hard Coded Traps
	maze[2][2] = "_"
	maze[2][4] = "_"
	maze[2][6] = "_"
	maze[3][1] = "#"
	maze[3][3] = "_"
	maze[3][5] = "#"
	maze[4][1] = "L"
	maze[4][2] = "_"
	maze[4][5] = "_"
	maze[4][6] = "L"
	maze[4][7] = "_"
	maze[5][1] = "_"
	maze[5][3] = "_"
	maze[5][6] = "_"
	maze[6][4] = "_"
	maze[6][7] = "_"
	maze[7][1] = "L"
	maze[7][2] = "_"
	maze[7][6] = "_"
	maze[8][1] = "_"
	maze[8][4] = "_"
	maze[8][5] = "#"
	maze[9][3] = "_"
	maze[9][5] = "_"
	maze[10][1] = "_"
	maze[10][6] = "_"
	maze[11][3] = "_"
	maze[11][5] = "_"
	maze[11][6] = "L"
	maze[12][2] = "_"
	maze[12][6] = "_"
	maze[13][2] = "#"
	maze[13][3] = "_"
	maze[13][5] = "#"
	maze[13][7] = "_"
	maze[14][1] = "_"
	maze[14][4] = "_"
	maze[14][7] = "_"
	maze[15][2] = "_"
	maze[15][5] = "_"
	maze[16][2] = "L"
	maze[16][3] = "_"
	maze[16][6] = "_"
	maze[17][2] = "_"
	maze[17][5] = "_"
	maze[18][4] = "_"
	maze[18][5] = "L"
	
	# Use of ' ' to show Exit
	maze[10][8] = " "
	
	# Use of '0' to show player
	maze[1][1] = "0"
	
	return maze
