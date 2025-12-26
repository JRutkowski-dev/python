import mpmath import mp

Pi = math.pi


n = int(input("podaj do ktorej liczby po przecinku chcialbys wyliczyc z Pi(max 14)"))

mp.dps = n + 1


print (mp.pi)
