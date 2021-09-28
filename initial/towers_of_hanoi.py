def printMove(fr, to):
	print('move from ' + str(fr) + ' to ' + str(to))

def tower_of_hanoi(disks, fr, to, spare):
	if disks == 1:
		return printMove(fr, to)
	else:
		tower_of_hanoi(disks - 1, fr, spare, to)
		tower_of_hanoi(1, fr, to, spare)
		tower_of_hanoi(disks - 1, spare, to, fr)


print(tower_of_hanoi(2, "P1", "P2", "P3"))