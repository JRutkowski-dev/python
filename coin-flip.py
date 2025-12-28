import random

def coinflip():
	number = int(input("ile razy chcesz rzucic moneta: "))
	recordlist = []
	orzel = 0
	reszka = 0
	for i in range(number):
		flip = random.randint(0, 1)
		if (flip == 0):
			print ("orzel")
			recordlist.append("orzel")
		else:
			print ("reszka")
			recordlist.append("reszka")
	print (str(recordlist))
	print (str(recordlist.count("orzel")) + str(recordlist.count("reszka")))
coinflip()
