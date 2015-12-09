# Level 4 for Maze Runner Game
def makeLevel4():
	# Definition of Range
	maze = [[ " " for j in range(9)] for i in range(20)]

	# Use of '#' to show boundary
	for j in range(0, 19):
		maze[j][8] = "#"
	for j in range(0, 19):
		maze[j][0] = "#"
	for j in range(0, 9):
		maze[0][j] = "#"
	for j in range(0, 9):
		maze[19][j] = "#"
	for j in range(1, 8):
		maze[5][j] = "#"
	for j in range(1, 8):
		maze[10][j] = "#"
	for j in range(1, 8):
		maze[15][j] = "#"
	for j in range(1, 19):
		maze[j][4] = "#"
	
	# Use of 'L' to show Lever
	maze[3][2] = "L"
	maze[3][6] = "L"
	maze[8][2] = "L"
	maze[8][6] = "L"
	maze[13][2] = "L"
	maze[13][6] = "L"
	maze[17][2] = "L"
	maze[17][6] = "L"
	
	# Use of ' ' to show exit
	maze[10][8] = " "
	
	# Use of '0' to show player
	maze[1][1] = "0"

	return maze
