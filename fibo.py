
n = int(input("podaj jak dlugi ma byc ciag: "))
a = 0
b = int(input("od jakiej liczby powinien sie ciag zaczynac: "))
next = b
count = 1


while count <= n:
	print (next, end=" ")
	count += 1
	a, b = b, next
	next = a + b
print ()
