import math

a = int(input("podaj liczbe: "))
b = int(input("podaj liczbe druga: "))
c = int(input("podaj trzecia liczbe: "))

delta = b**2 - 4*a*c
print (delta)

if delta > 0:
   x1 = (-b - delta**0.5) / (2*a)
   x2 = (-b + delta**0.5) / (2*a)
   print ("dwa rozwiazania")
   print (x1)
   print (x2)
elif delta == 0:
   x = -b / (2*a)
   print (x)
else:
   print ("brak rozwiazania") 

