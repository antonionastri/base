# lista

# ordinate
# modificabili
# ammettono duplicati
# indicizzate ( base 0 )

frutta = ["mela", "banana", "pera"]
print(frutta)

# accedere all'elemento alla posizione 0 (primo elemento)
print(frutta[0])

frutta[0] = "fragola"
print(frutta)

# lista varia
lista2 = [1, "ciao", True]

# accesso agli elementi
frutta = ["apple", "banana", "cherry", "oragne", "kiwi", "melon", "mango"]

print(frutta[2:5])
print(frutta[:5])
print(frutta[2:])
print(frutta[-1])

indice = frutta.index("kiwi")
print(indice)

# indice = frutta.index("pera")
print(indice)

esiste_pera = "pera" in frutta
print(esiste_pera)

# creare una variabile di nome fr che contiene una stringa con un frutto
# verificare che il valore della variabile fr esista in frutta
# se esiste scrivere a terminale "[nome della frutta] trovato"
# se non esiste scrivere a terminale "[nome della frutta] non trovato"
# testare il tutto provando a cambiare il valore della variabile fr

fr = "pesca"
esiste_fr = fr in frutta
if esiste_fr == True:
    print(fr, "trovato")
else:
    print(fr, "non trovato")
    
#too easy


