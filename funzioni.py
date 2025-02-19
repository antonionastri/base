# una funzione è un blocco di codice pensato per essere ripetuto

def mia_funzione():
    print("================")
    print("Ciao da Python!")
    print("================")
    
for n in range(5):
    mia_funzione()  
    
# parametro (argomento) di una funzione 
def saluta(nome):
    """Funzione che saluta

    Args:
        nome (str): il nome da salutare
    """
    print(f"Ciao {nome}!")
    
saluta("Paolo")

#parametri multipli
def presentati(nome, cognome, anni):
    mag_min = ""
    
    if anni >= 18:
        mag_min = "maggiorenne"
    else:
        mag_min = "minorenne"
        
    print(f"ciao {nome} {cognome}, hai {anni} anni e sei {mag_min}")
    
presentati("Paolo", "Rossi", 25)

# torna un valore che posso mettere in una variabile e riusare
def somma(n1, n2):
    return n1 + n2

risultato = somma(5, 3)
print(f"il risultato è: {risultato}")
print(f"il risultato al quadrato è: {risultato**2}")

# parametri di default/opzionali
def spedisci(prodotto, paese="Italia"):
    print(f"il prodotto {prodotto} è stato spedito in {paese}")
    
spedisci("libro", "Italia")
spedisci("bro")
spedisci("tuta", "Francia")

# args: accetta un numero variabile di argomenti
def somma_multipla(*numeri):
    totale = 0
    
    for n in numeri:
        totale += n
    return totale

print(somma_multipla(1, 2, 3, 4, 5))
print(somma_multipla(1, 254, 63, 34))

# print
print("ciao", "mario", "saluti", 69, True)

print("---------------------------")

# scope delle variabili
pippo = "pluto"
def saluta_pippo():
    global pippo
    pippo = "pippo"
    print(f"ciao {pippo}")

saluta_pippo()
print(pippo)

# lambda

# è un modo per definire funzioni anonime che ritornano un valore
# e il cui corpo possiamo scriverlo su una sola riga

def quadrato2(x):
    return x**2

quadrato = lambda x: x**2

print(quadrato(3))

numeri = [1, 2, 3, 4, 5]

maggiori_2 = filter(lambda x: x > 2, numeri)
print(list(maggiori_2))