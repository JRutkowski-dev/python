import random

tajna = random.randint(1, 100)
proby = 0

print("Zgadnij liczbę od 1 do 100")

zgadniecie = int(input("Podaj swoją liczbe: "))
proby += 1

while zgadniecie != tajna:
    if zgadniecie < tajna:
        print("Za nisko!")
    else:
        print("Za wysoko!")
    
    zgadniecie = int(input("Spróbuj ponownie: "))
    proby += 1

print(f"Gratulacje! Zgadłeś liczbę {tajna} w {proby} próbach.")
