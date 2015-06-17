## Python tictactoe

#player A is X 
#player B is O

def checker(player_list): 
	# check rows (numbers)
	ones = 0
	twos = 0
	threes = 0
	for s in player_list:
		if s[0] == "1":
			ones += 1
		elif s[0] == "2":
			twos += 1
		elif s[0] == "3":
			threes += 1
		if ones == 3 or twos == 3 or threes == 3:
			print ("Horizontal win!")
			return True
	# check columns (letters)
	As = 0
	Bs = 0
	Cs = 0
	for s in player_list:
		if s[1] == "a":
			As += 1
		elif s[1] == "b":
			Bs += 1
		elif s[1] == "c":
			Cs+= 1
		if As == 3 or Bs == 3 or Cs == 3:
			print ("Vertical win!")
			return True
	# check diagonals
	if "1a" in player_list and "2b" in player_list and "3c" in player_list:
		print ("Diagonal win!")
		return True
	if "1c" in player_list and "2b" in player_list and "3a" in player_list:
		print ("Diagonal win!")
		return True
	return False
	
def input_validate(loc):
	if len(loc) == 2:
		if loc[0] == "1" or loc[0] == "2" or loc[0] == "3":
			if loc[1] == "a" or loc[1] == "b" or loc[1] == "c": 
				return True
			else:
				return False
		else:
			return False
	else:
		return False 
	
def move_validate(tiledict, loc):
	#loc must be free
	if tiledict[loc] == " ":
		return True
	else:
		return False
	
def marker(tiledict, player, loc): #tiledict is dictionary, player and loc are strings
	if player == "a":
		tilestate = "X" #optimize/clean later!!!
		list_player_X.append(loc)
	elif player == "b":
		tilestate = "O"
		list_player_O.append(loc)
	else:
		print ("Problem in player")
		tilestate = " "
	tiledict[loc] = tilestate
	##print (list_player_O)
	##print (list_player_X)
	
def displayer(tiledict):
	print ("-------------")
	print ("|", tiledict['1a'], "|", tiledict['1b'], "|", tiledict['1c'], "|")
	print ("-------------")
	print ("|", tiledict['2a'], "|", tiledict['2b'], "|", tiledict['2c'], "|")
	print ("-------------")
	print ("|", tiledict['3a'], "|", tiledict['3b'], "|", tiledict['3c'], "|")
	print ("-------------")

def starter_display():
	print ("----------------")
	print ("| 1a | 1b | 1c |")
	print ("----------------")
	print ("| 2a | 2b | 2c |")
	print ("----------------")
	print ("| 3a | 3b | 3c |")
	print ("----------------")
	
list_player_X = []
list_player_O = []

tiles = {"1a":" ", "1b":" ", "1c":" ", "2a":" ", "2b":" ", "2c":" ", "3a":" ", "3b":" ", "3c":" "}

#start the game
print ("Welcome to Tic Tac Toe")
starter_display()

i = 0

while i <= 8:
	position = raw_input("Where would you like to play?")
	##print (input_validate(position))
	while not input_validate(position):
		position = raw_input("Please input a valid position. Type SHOW to see the positions.")
		if position == "SHOW":
			starter_display()
	while not move_validate(tiles, position):
		position = raw_input("That spot is already taken. Please choose another.")
	if i%2 == 0: 
		player = "a"
	else:
		player = "b"
	marker(tiles, player, position)
	displayer(tiles)
	if checker(list_player_X) or checker(list_player_O):
			break
	i += 1	
if i == 8:
	print ("Draw!")
