# Level 3 for Maze Runner Game
def makeLevel3():
	# Definition of Range
	maze = [[ " " for j in range(9)] for i in range(20)]
	
	# Use of '#' to show Boundary
	for j in range(0, 19):
		maze[j][8] = "#"
	for j in range(0, 19):
		maze[j][0] = "#"
	for j in range(0, 9):
		maze[0][j] = "#"
	for j in range(0, 9):
		maze[19][j] = "#"
	for j in range(1, 3):
		maze[j][2] = "#"
	for j in range(1, 7):
		maze[4][j] = "#"
	for j in range(2, 4):
		maze[j][6] = "#"
	for j in range(2, 8):
		maze[9][j] = "#"
	maze[5][5] = "#"
	maze[8][5] = "#"
	for j in range(2, 7):
		maze[15][j] = "#"
	for j in range(10, 14):
		maze[j][4] = "#"
	maze[10][5] = "#"
	
	# Use of '_' to show Traps/Landmines
	for j in range(11, 15):
		maze[j][6] = "_"
	for j in range(10, 14):
		maze[j][2] = "_"
	for j in range(2, 7):
		maze[16][j] = "_"
	maze[17][6] = "_"
	maze[6][3] = "_"
	maze[7][2] = "_"
	maze[8][2] = "_"
	maze[6][5] = "_"
	maze[6][7] = "_"
	maze[2][4] = "_"
	
	# Use of ' ' to show exit
	maze[10][8] = " "
	
	# Use of '0' to show player
	maze[1][1] = "0"
		
	return maze
 
