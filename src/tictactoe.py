Spielfeld = [["N", "N", "N"],["N", "N", "N"],["N", "N", "N"]]

Spieler1 = "X"
Spieler2 = "O"

def readInputFromPlayer(player):
	print "Player "+player+"ist am zug. Gib was ein: "
	x = input("X: ")
	y = input("Y: ")
	return x, y

def setField(x, y, player):
	if Spielfeld[x][y] != "N":
		print "Dieses Feld ist schon besetzt!"
		x, y = readInputFromPlayer(player)
		setField(x, y, player)
	Spielfeld[x][y] = player

def gameOver():

	h = h_check()
	v = v_check()
	d = d_check()

	if h != "N":
		print h+" hat gewonnen!"
		return True

	if v != "N":
		print v+" hat gewonnen!"
		return True

	if d != "N":
		print d+" hat gewonnen!"
		return True

	return False
	
def h_check():
	for line in Spielfeld:
		if line.count(Spieler1) == 3:
			return Spieler1
		if line.count(Spieler2) == 3:
			return Spieler2
	return "N"

def v_check():

	if (Spielfeld[0][0] == Spielfeld[1][0] == Spielfeld[2][0]):
		return Spielfeld[0][0]

	if (Spielfeld[0][1] == Spielfeld[1][1] == Spielfeld[2][1]):
		return Spielfeld[0][1]

	if (Spielfeld[0][2] == Spielfeld[1][2] == Spielfeld[2][2]):
		return Spielfeld[0][2]

	return "N"

def d_check():

	if (Spielfeld[0][0] == Spielfeld[1][1] == Spielfeld[2][2]):
		return Spielfeld[1][1]

	if (Spielfeld[0][2] == Spielfeld[1][1] == Spielfeld[2][0]):
		return Spielfeld[1][1]

	return "N"

CurrentPlayer = Spieler1

while(gameOver() == False):

	x, y = readInputFromPlayer(CurrentPlayer)
	setField(x, y, CurrentPlayer)

	if (CurrentPlayer == Spieler1):
		CurrentPlayer = Spieler2
	else:
		CurrentPlayer = Spieler1