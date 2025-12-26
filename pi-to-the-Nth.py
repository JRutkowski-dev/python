import mpmath

Pi = mpmath.pi


n = int(input("podaj do ktorej liczby po przecinku chcialbys wyliczyc z Pi(max 14):"))

mpmath.mp.dps = n + 1


print (mpmath.mp.pi)
