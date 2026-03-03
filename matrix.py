import random
import time

width = 70
flipsPerLine = 5
sleepTime = 0.1

ch = "1234567890qwertyuiopasdfghjklzxcvbnm,./';[]!@#$%^&*()-=_+"

switches = [0]*width

while True:
	for i in range(0, width, 2):
		if switches[i]:
			print (ch[random.randint(0, len(ch)-1)], end=" ")
		else:
			print (" ", end=" ")
	for _ in range(flipsPerLine):
		x = random.randint(0, width-1)
		switches[x] = not switches [x]
	print ()

	time.sleep(sleepTime)
