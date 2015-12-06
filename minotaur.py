#Function dictating the minotaurs movement
def minNextLoc(thes_x, thes_y, minotaur_x, minotaur_y):
	if (abs(thes_x - minotaur_x) >= abs (thes_y - minotaur_y))
		if (thes_x - minotaur_x) > 0
			minotaur_x += 1
		elif (thes_x - minotaur_x) < 0
			minotaur_x -= 1
	elif (abs(thes_y - minotaur_y) > abs (thes_x - minotaur_x))
		if (thes_y - minotaur_y) > 0
			minotaur_y += 1
		elif (thes_y - minotaur_y) < 0
			minotaur_y -= 1

		return minotaur_x, minotaur_y
