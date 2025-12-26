start = int(input("podaj liczbe pierwszą: "))
end = int(input("podaj liczbe drugą: "))

print ("liczby parzyste z podanego przedziału")
for i in range (start,end + 1):
	if i % 2==0:
	 print (i)

