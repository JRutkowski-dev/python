def dec_to_bin(
	decimal = int(input("podaj liczbe dla konwertera do liczby binarnej: "))
	binary = format(decimal, 'b')
	print (f"Binarny z {decimal} to {binary}")
	)

def bin_to_dec(
	binary = int(input("podaj liczbe dla konwertera do liczny decymalnej: "))
	decimal = int(binary, 2)
	print (f"decymalny z {binary} to {decimal}")
	)

print ("wybierz konwerter")
print ("1. binary do decimal")
print ("2. decimal do binary")
print ("q to wyjscie")

while True:
	choice = input("wybierz operacje: ")
	if choice == '1':
		bin_to_dec()
	elif choice == '2':
		dec_to_bin()
	elif choice == 'q':
		print ("zakonczenie programu")
		break
	else:
		print ("Nieprawidlowy wybor, wybierz ponownie")
